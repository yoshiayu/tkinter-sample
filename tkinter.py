from tkinter import *
from tkinter import messagebox as mb

# window作成
win = Tk()

# テキスト入力
mylabel = Label(win, text="名前を入力してください")
mylabel.pack()

# テキストBOXh作成
text = Entry(win)
text.pack()
#　初期設定
text.insert(END, "  ")

# OK関数


def ok_click():
    a = text.get()
    # OKクリックでメッセージ
    mb.showinfo("Hi!!", a + "さん、初めまして!")


# ボタン作成
okButton = Button(win, text="OK", command=ok_click)
okButton.pack()
# windowを起動
win, mainloop()
