from random import choice
from passlib.hash import pbkdf2_sha256 as sha256
from tkinter import Tk,Label,StringVar,Entry,Button,Frame,LabelFrame
from tkinter.font import Font
from tkinter.messagebox import showerror

'''KEYS = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 '^êâîôûïëè¨éà$,.-?`ü!öä£;:_+"*ç%&/()=´~[]{}§°<>\\"""

ALPHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUM = """1234567890+"*ç%&/()=?ü!öä£;:_'^è¨éà$,.-<>\{}[]¦@#°§¬|¢§°"""
'''
KEYS = """ 1234567890§+"*ç%&\()='^¨$,.-°?`!£;:_´~[]{}<>/¦@"#¬|¢abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZàèìòùáéíóúýäëïöüÿêâîôû"""
ALPHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZàèìòùáéíóúýäëïöüÿêâîôû"
NUM = """1234567890§+"*ç%&\()='^¨$,.-°?`!£;:_´~[]{}<>/¦@#¬"|¢"""


def encrypt(text):
    res = ""
    for k in text:
        try:
            v = int(KEYS.index(k))
            b = str(bin(v))[2:]
            for x in b:
                if x == "0":
                    res += choice(NUM)
                else:
                    res += choice(ALPHA)
            res += " "
        except ValueError:
                return f'\'{k}\' n\'est pas un caractère reconnu'
                print('Not in keys:',k)
    return res

def decrypt(text):
    res = ""
    for split in text.split(' '):
        if split == "\n":
            continue
        sr = ""
        for k in split:
            if k == "\n":
                continue
            if k in ALPHA:
                sr += "1"
            elif k in NUM:
                sr += "0"
            else:
                return f"Erreur: Décodage impossible pour le caractère: '{k}'"
        if sr == "":
            continue
        try:
            res += KEYS[int(sr,2)]
        except IndexError:
            return "Erreur: Decodage impossible."
    return res


class UI(Tk):

    def encode(self):
        self.decode_text.set(encrypt(self.encode_text.get()))

    def decode(self):
        self.encode_text.set(decrypt(self.decode_text.get()))

    def _submit(self):
        self.wm_geometry("800x700+20+20")
        self.mframe = Frame(self)
        self.mframe["bg"] = "white"

        self.encrypter_frame = LabelFrame(self.mframe,text="Encodeur",width=500,height=100)
        Label(self.encrypter_frame,text="Texte:",font=Font(size=13), fg="white").grid()
        self.encode_text = StringVar()
        Entry(self.encrypter_frame,textvar=self.encode_text,width=70).grid(column=1,row=0,ipady=5)
        Button(self.encrypter_frame,text="Encoder",command=self.encode).grid(column=0,row=1,pady=5)
        self.encrypter_frame.grid(padx=50,pady=20)
        self.encrypter_frame.grid_propagate(0)

        self.encrypter_frame = LabelFrame(self.mframe,text="Decodeur",width=500,height=100)
        Label(self.encrypter_frame,text="Texte:",font=Font(size=13)).grid()
        self.decode_text = StringVar()
        Entry(self.encrypter_frame,textvar=self.decode_text,width=70).grid(column=1,row=0,ipady=5)
        Button(self.encrypter_frame,text="Décoder",command=self.decode).grid(column=0,row=1,pady=5)
        self.encrypter_frame.grid(padx=50,pady=20)
        self.encrypter_frame.grid_propagate(0)

        self.mframe.place(x=0,y=0)

    def __init__(self):
        Tk.__init__(self)
        self.wm_geometry("280x100+500+300")
        self.wm_title("CB Encrypter")
        self["bg"] = "white"
        self._submit()


if __name__ == "__main__":
    ui = UI()
    ui.mainloop()


