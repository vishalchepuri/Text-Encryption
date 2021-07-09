from tkinter import *
import string
import random


def stuffing(y):
    return ''.join(random.choice(string.ascii_letters) for _ in range(y))


def convert_to_number(key):
    SUM = 0
    for i in key:
        SUM = SUM + ord(i)
    return SUM


def enc_lst(key, ln):
    random.seed(key)
    lis = []
    for i in range(ln):
        lis.append(random.randint(0, ln + key))
    return lis


def get_key(pasw, ln):
    first_key = convert_to_number(pasw)
    second_key = ln
    third_key = ord(pasw[0])
    final_key = first_key + second_key + third_key
    return final_key


def encrypt_the_data(pasw, message):
    lis = enc_lst(get_key(pasw, len(message)), len(message))
    enc = stuffing(len(message))
    for i, j in zip(message, lis):
        enc = enc + chr(((ord(i) + j) % 94) + 32)
        enc = enc + chr(ord("!") + (ord(i) + j) // 94)
    enc = enc + stuffing(len(message))
    return enc


def decrypt_the_data(pasw, encmsg):
    encmsg = encmsg[(len(encmsg) // 4):-(len(encmsg) // 4)]
    lis = enc_lst(get_key(pasw, len(encmsg) // 2), len(encmsg) // 2)
    enc, ext = encmsg[::2], encmsg[1::2]
    msg = ""
    for i, j, k in zip(enc, ext, lis):
        msg = msg + chr(((ord(j) - 33) * 94) + (ord(i) - 32) - k)
    return msg


def final_enc(pas, message):
    return encrypt_the_data(pas, message)


def final_dec(pas, message):
    return decrypt_the_data(pas, message)


root = Tk()
root.title("Text Encrypt")
root.geometry("600x400")
root['bg'] = "#24252A"

pass_var = StringVar()


def encrypt():
    message = T_msg.get(1.0, "end-1c")
    password = pass_var.get()
    msg = final_enc(password, message)
    T_msg.delete(1.0, "end")
    T_msg.insert(1.0, msg)
    pass_var.set(password)


def decrypt():
    message = T_msg.get(1.0, "end-1c")
    password = pass_var.get()
    msg = final_dec(password, message)
    T_msg.delete(1.0, "end")
    T_msg.insert(1.0, msg)
    pass_var.set(password)



message_label = Label(root, text='Message:', font=('calibre', 10, 'bold'))
T_msg = Text(root, height=6, width=50, bg="#C2D6D5", relief="solid")
T_msg.place(width=6, height=50)
key_label = Label(root, text='Security Key:', font=('calibre', 10, 'bold'))
key_entry = Entry(root, textvariable=pass_var, font=('calibre', 10, 'normal'), show='*')

enc_btn = Button(root, text='Encrypt', command=encrypt, bg="#60859F")
dec_btn = Button(root, text='Decrypt', command=decrypt, bg="#60859F")

message_label.grid(row=3, column=0, padx=10, pady=10)
T_msg.grid(row=3, column=1, padx=10, pady=10)
key_label.grid(row=4, column=0, ipady=10, padx=10, pady=10)
key_entry.grid(row=4, column=1, padx=10, pady=10)
dec_btn.grid(row=5, column=0, padx=10, pady=10)
enc_btn.grid(row=5, column=1, padx=10, pady=10)
root.mainloop()
