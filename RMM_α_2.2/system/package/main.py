#==============================================================================
from window import Builder, Holder, Writer
from editers import DivideImage
from dynamic_global import Set, Map
from static_global import Mode
import tkinter as tk
import threading
import os
#==============================================================================
class Main:
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    @ staticmethod
    def builer_window():
        builder_frame = tk.Tk()

        #
        builder = Builder(builder_frame)
        builder.init_note()
        builder.set_window()
        builder.set_menu()
        builder.set_canvas()
        #
        builder_frame.mainloop()
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    @ staticmethod
    def holder_window():
        holder_frame = tk.Tk()
        #
        holder = Holder(holder_frame)
        holder.set_domain()
        holder.set_window()
        holder.set_menu()
        holder.set_canvas()
        #
        holder_frame.mainloop()
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    @ staticmethod
    def writer_window():
        writer_frame = tk.Tk()
        #
        writer = Writer(writer_frame)
        writer.set_domain()
        writer.set_window()
        writer.set_menu()
        writer.set_canvas()
        #
        writer_frame.mainloop()
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    def __init__(self):
        # カレントディレクトリの変更
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        # 初期化処理
        Map.size = (100,100)            
        Set.layer = Mode.LAYER_5
        Set.open_window = Mode.OPEN_WRITER
        # DivideImage()
        
    def process(self):
        # マルチスレッド処理
        b = threading.Thread(target = self.main_window)
        h = threading.Thread(target = self.sub_window)
        b.start()
        h.start()
        h.join()
        h.join()
    def main_window(self):
        Main.builer_window()
    def sub_window(self):
        if Set.open_window == Mode.OPEN_HOLDER:
            Main.holder_window()
        elif Set.open_window == Mode.OPEN_WRITER:
            Main.writer_window()
        elif  Set.open_window == Mode.CLOSE_WINDOW:
            pass
        
        

        


if __name__ == "__main__":

    Main().process()