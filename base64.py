
from tkinter import *
root = Tk()
root.configure(background="Red")
root.geometry("1080x1920")
root.title("Message Encryption and Decryption")
Tops = Frame(root, width=1601, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=1920, height=900,relief=SUNKEN,bg="Grey")
f1.pack(side='left')
lblInfo = Button(Tops, font=('fixedsys', 50, 'bold',),text="#Base 64 AES Encryption#",
                fg="Red",bg="Black", bd=10, anchor='w',relief="sunken")
lblInfo.grid(row=0, column=0)

lab1=Label(Tops,font=('fixedsys',28,'italic'),text="This application encodes any of your messages \n to a cipher text",fg="yellow",bg="black")
lab1.grid(row=1,column=0)
rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()

def qExit():
    root.destroy()


def Reset():
    rand.set("")
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")

lblMsg = Label(f1, font=('fixedsys', 16, 'bold'),text="Enter your Message here",fg="white",bg="grey", bd=16, anchor="w")

lblMsg.grid(row=1, column=1)

txtMsg = Entry(f1, font=('fixedsys', 16, 'bold'),
               textvariable=Msg, bd=10, insertwidth=4,
               bg="powder blue", justify='left')

txtMsg.grid(row=2, column=1)

lblkey = Label(f1, font=('fixedsys', 16, 'bold'),
               text="Enter the Key to Encrypt or Decrypt",fg="white",bg="grey", bd=16, anchor="w")

lblkey.grid(row=3, column=1)

txtkey = Entry(f1, font=('fixedsys', 16, 'bold'),
               textvariable=key, bd=10, insertwidth=4,
               bg="powder blue", justify='left')

txtkey.grid(row=4, column=1)

lblmode = Label(f1, font=('fixedsys', 16, 'bold'),fg="white",bg="grey",
                text="MODE(Type e to encrypt, d to decrypt)",
                bd=16, anchor="w")

lblmode.grid(row=5, column=1)

txtmode = Entry(f1, font=('fixedsys', 16, 'bold'),
                textvariable=mode, bd=10, insertwidth=4,
                bg="powder blue", justify='left')

txtmode.grid(row=6, column=1)

lblService = Label(f1, font=('fixedsys', 20, 'bold'),fg="yellow",bg="grey",text="The Result-", bd=16, anchor="w")

lblService.grid(row=2, column=2)

txtService = Entry(f1, font=('fixedsys', 16, 'bold'),
                   textvariable=Result,bd=6,width=40,
                   bg="powder blue", justify='left')

txtService.grid(row=3, column=2)


import base64



def encode(key, clear):
    enc = []

    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) +
                     ord(key_c)) % 256)

        enc.append(enc_c)

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()



def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
    return "".join(dec)


def Ref():
    print("Message= ", (Msg.get()))

    clear = Msg.get()
    k = key.get()
    m = mode.get()

    if (m == 'e'):
        Result.set(encode(k, clear))
    else:
        Result.set(decode(k, clear))




btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black",
                  font=('arial', 16, 'bold'), width=10,
                  text="Show Message", bg="powder blue",
                  command=Ref).grid(row=7, column=1)


btnReset = Button(f1, padx=16, pady=8, bd=16,
                  fg="black", font=('arial', 16, 'bold'),
                  width=10, text="Reset", bg="green",
                  command=Reset).grid(row=7, column=2)


btnExit = Button(f1, padx=16, pady=8, bd=16,
                 fg="black", font=('arial', 16, 'bold'),
                 width=10, text="Exit", bg="red",
                 command=qExit).grid(row=7, column=3)


root.mainloop()
