import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.geometry("300x300")       # ウィンドウサイズ(幅x高さ)

        # ウィンドウの x ボタンが押された時に呼ばれるメソッドを設定
        self.master.protocol("WM_DELETE_WINDOW", self.delete_window)

    def delete_window(self):
        print("ウィンドウのxボタンが押された")

        # 終了確認のメッセージ表示
        ret = messagebox.askyesno(
            title = "終了確認",
            message = "プログラムを終了しますか？")

        if ret == True:
            # 「はい」がクリックされたとき
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()

    app = Application(master = root)
    app.mainloop()