#==============================================================================
import tkinter as tk
from dynamic_global import Map, Chip, Set, Array
from static_global import Word, Mode
from menu import Menu, SubMenu
from canvas import Canvas
#==============================================================================

#==============================================================================
class SettingBuilder:
    """Builderクラスの画面のサイズなどを設定するクラス"""
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    def __init__(self, master : tk.Tk):
        self.master = master
        
    def screen_width(self) -> int:
        """パソコンの画面の最大横幅を返す"""
        return self.master.winfo_screenwidth()
    
    def screen_height(self) -> int:
        """パソコンの画面の最大縦幅を返す"""
        return self.master.winfo_screenheight()
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # ウインドウの最大と最小サイズの設定
    def max_width(self) -> int:
        """Builderウインドウ画面の最大横幅を返す"""
        return self.screen_width() // 2
    def max_height(self) -> int:
        """Builderウインドウ画面の最大縦幅を返す"""
        return self.screen_height() - 80

    def min_width(self) -> int:
        """Builderウインドウ画面の最小横幅を返す"""
        return self.screen_width() // 2
    def min_height(self) -> int:
        """Builderウインドウ画面の最小縦幅を返す"""
        return self.screen_height() // 2
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # ウインドウの初期サイズとポジション
    def width(self) -> int:
        """ウインドウの横幅"""
        return self.max_width()
    def height(self) -> int:
        """ウインドウの縦幅"""
        return self.max_height()
    def size(self) -> str:
        """ウインドウのサイズ"""
        w = self.width()
        h = self.height()
        return f"{w}x{h}"
    def position(self) -> str:
        """ウインドウのポジション"""
        return "0+0"
    def header_height(self) -> int:
        """ヘッダーの高さ"""
        return 32
    def mega_menu_height(self) -> int:
        return 24

#==============================================================================
class Builder(tk.Frame):
    """メインで描画処理を行うウインドウのクラス"""
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # コンストラクタ   
    def __init__(
            self, master : tk.Tk) -> None:
        """
        windowの初期設定と各クラスのインスタンス化を行う
       
        """
        super().__init__(master)
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self.delete_window)
    def delete_window(self):
        self.master.destroy()
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # noteの初期化設定
    def init_note(self):
        # 初期変数設定
        self.map_size = Map.size
        map_row, map_colume = self.map_size
        Map.layer_0 = "a0"
        Map.layer_1 = "a1"
        Map.layer_2 = "a2"
        Map.layer_3 = "a3"
        Map.layer_4 = "a4"
        Map.layer_5 = "a5"
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # ウインドウの設定, ウェジェットの配置はまだ。
    def set_window(self) -> None:
        """
        window_size:ウインドウの大きさ
        window_positon:ウインドウの初期位置
        window_title:ウィンドウのタイトル 
        """
        screen = SettingBuilder(self.master)
        # ウインドウのタイトルの設定
        self.window_title = Word.title
        # ウインドウの最大サイズ
        self.master.maxsize(
            width = screen.max_width(),
            height = screen.max_height())
        # ウインドウの最小サイズ
        self.master.minsize(
            width = screen.min_width(),
            height = screen.min_height())
        # ウインドウの初期サイズ
        self.window_width = screen.width()
        self.window_height = screen.height()
        self.window_size = screen.size()
        # ウインドウの表示と表示位置
        self.master.geometry(                       
            f"{self.window_size}+{screen.position()}") 
        self.screen = screen

    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # ヘッダーの設定
    def set_menu(self):
        """
        メニューの設定
        ヘッダーとメガメニューで構成されている
        """
        # メニューの設定
        self.menu = Menu(
            self.master,
            header_height= self.screen.header_height(),
            mega_height = self.screen.mega_menu_height())
        # メニューの高さ幅の設定
        self.menu_height \
            = self.screen.header_height() \
            + self.screen.mega_menu_height()
        # ヘッダーの設定
        self.menu.set_header()
        # メガメニューの設定
        self.menu.set_mega()
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # キャンバスの設定
    def set_canvas(self) -> None:
        """
        canvasの設定
        map_size:作成したいマップの大きさのマス目での縦横。
        canvas_position:window無いでのcanvasの場所
        """
        map_width, map_height = self.map_size
        map_width = Chip.pixel * map_width
        map_height = Chip.pixel * map_height 
        canvas = Canvas(
            master_frame = self.master,
            canvas_width = self.window_width,
            canvas_height = self.window_height - self.menu_height,
            canvas_postion_y = self.menu_height,
            map_width = map_width,
            map_height = map_height)
        # メインの描画処理
        canvas.main_draw()
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    def set_mouse(self) -> None:
        """マウス入力の設定"""

    def set_keybord(self) -> None:
        """キーボード入力の設定"""
#==============================================================================

#==============================================================================
class SettingHolder:
    """
    Holderクラスの画面のサイズなどを設定するクラス,
    SettingBuilderクラスに依存する。
    """
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    def __init__(self, master : tk.Tk):
        self.master = master
        self.builder = SettingBuilder(self.master)
    def screen_width(self) -> int:
        """パソコンの画面の最大横幅を返す"""
        return self.master.winfo_screenwidth()
    
    def screen_height(self) -> int:
        """パソコンの画面の最大縦幅を返す"""
        return self.master.winfo_screenheight()
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # ウインドウの最大と最小サイズの設定
    def max_width(self) -> int:
        """Builderウインドウ画面の最大横幅を返す"""
        return self.screen_width() // 4
    def max_height(self) -> int:
        """Builderウインドウ画面の最大縦幅を返す"""
        return self.screen_height() - 80

    def min_width(self) -> int:
        """Builderウインドウ画面の最小横幅を返す"""
        return self.screen_width() // 4
    def min_height(self) -> int:
        """Builderウインドウ画面の最小縦幅を返す"""
        return self.screen_height() // 2
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # ウインドウの初期サイズとポジション
    def width(self) -> int:
        """ウインドウの横幅"""
        return self.max_width() 
    def height(self) -> int:
        """ウインドウの縦幅"""
        return self.max_height()
    def size(self) -> str:
        """ウインドウのサイズ"""
        w = self.width()
        h = self.height()
        return f"{w}x{h}"
    def position(self) -> str:
        w = str(self.builder.max_width() + 16)
        pos = f"{w}+0"
        return pos        
    def header_height(self) -> int:
        """ヘッダーの高さ"""
        return 24
#==============================================================================
class Holder(tk.Frame):
    """Builderに入れる情報を表示させるウインドウのクラス"""
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # コンストラクタ   
    def __init__(
            self, master : tk.Tk) -> None:
        """windowの初期設定と各クラスのインスタンス化を行う"""
        super().__init__(master)
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self.delete_window)

    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    def delete_window(self):
        self.master.destroy()
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # ウインドウの設定, ウェジェットの配置はまだ。
    def set_window(self) -> None:
        """
        window_size:ウインドウの大きさ
        window_positon:ウインドウの初期位置
        window_title:ウィンドウのタイトル 
        """
        screen = SettingHolder(self.master)
        # ウインドウのタイトルの設定
        self.window_title = Word.title
        # ウインドウの最大サイズ
        self.master.maxsize(
            width = screen.max_width(),
            height = screen.max_height())
        # ウインドウの最小サイズ
        self.master.minsize(
            width = screen.min_width(),
            height = screen.min_height())
        # ウインドウの初期サイズ
        self.window_width = screen.width()
        self.window_height = screen.height()
        self.window_size = screen.size()
        # ウインドウの表示と表示位置
        self.master.geometry(                       
            f"{self.window_size}+{screen.position()}") 
        self.screen = screen
    def set_menu(self):
        """
        メニューの設定
        ヘッダーのみの構成
        """
        # メニューの設定
        self.menu_height = self.screen.header_height()
        self.menu = SubMenu(
            self.master,
            header_height = self.menu_height)
        self.menu.set_header()
    def set_domain(self):
        """"""
        self.map_size = Map.size
    def set_canvas(self):
        map_width, map_height = self.map_size
        map_width = Chip.pixel * map_width
        map_height = Chip.pixel * map_height 
        canvas = Canvas(
            master_frame = self.master,
            canvas_width = self.window_width,
            canvas_height = self.window_height - self.menu_height,
            canvas_postion_y = self.menu_height,
            map_width = map_width,
            map_height = map_height)
        # holderにmaster_chipを表示
#==============================================================================
class SettingWriter:
    """
    Holderクラスの画面のサイズなどを設定するクラス,
    SettingBuilderクラスに依存する。
    """
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    def __init__(self, master : tk.Tk):
        self.master = master
        self.builder = SettingBuilder(self.master)
    def screen_width(self) -> int:
        """パソコンの画面の最大横幅を返す"""
        return self.master.winfo_screenwidth()
    
    def screen_height(self) -> int:
        """パソコンの画面の最大縦幅を返す"""
        return self.master.winfo_screenheight()
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # ウインドウの最大と最小サイズの設定
    def max_width(self) -> int:
        """Builderウインドウ画面の最大横幅を返す"""
        return self.screen_width() // 2
    def max_height(self) -> int:
        """Builderウインドウ画面の最大縦幅を返す"""
        return self.screen_height() - 80

    def min_width(self) -> int:
        """Builderウインドウ画面の最小横幅を返す"""
        return self.screen_width() // 4
    def min_height(self) -> int:
        """Builderウインドウ画面の最小縦幅を返す"""
        return self.screen_height() // 2
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # ウインドウの初期サイズとポジション
    def width(self) -> int:
        """ウインドウの横幅"""
        return self.max_width() // 2
    def height(self) -> int:
        """ウインドウの縦幅"""
        return self.max_height()
    def size(self) -> str:
        """ウインドウのサイズ"""
        w = self.width()
        h = self.height()
        return f"{w}x{h}"
    def position(self) -> str:
        w = str(self.builder.max_width() + 16)
        pos = f"{w}+0"
        return pos        
    def header_height(self) -> int:
        """ヘッダーの高さ"""
        return 24
#==============================================================================
class Writer(tk.Frame):
    """Builderに入れる情報を表示させるウインドウのクラス"""
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # コンストラクタ   
    def __init__(
            self, master : tk.Tk) -> None:
        """windowの初期設定と各クラスのインスタンス化を行う"""
        super().__init__(master)
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self.delete_window)
 
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    def delete_window(self):
        self.master.destroy()
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # ウインドウの設定, ウェジェットの配置はまだ。
    def set_window(self) -> None:
        """
        window_size:ウインドウの大きさ
        window_positon:ウインドウの初期位置
        window_title:ウィンドウのタイトル 
        """
        screen = SettingHolder(self.master)
        # ウインドウのタイトルの設定
        self.window_title = Word.title
        # ウインドウの最大サイズ
        self.master.maxsize(
            width = screen.max_width(),
            height = screen.max_height())
        # ウインドウの最小サイズ
        self.master.minsize(
            width = screen.min_width(),
            height = screen.min_height())
        # ウインドウの初期サイズ
        self.window_width = screen.width()
        self.window_height = screen.height()
        self.window_size = screen.size()
        # ウインドウの表示と表示位置
        self.master.geometry(                       
            f"{self.window_size}+{screen.position()}") 
        self.screen = screen
    def set_menu(self):
        """
        メニューの設定
        ヘッダーのみの構成
        """
        # メニューの設定
        self.menu_height = self.screen.header_height()
        self.menu = SubMenu(
            self.master,
            header_height = self.menu_height)
        self.menu.set_header()
    def set_domain(self):
        """"""
        self.map_size = Map.size
    def set_canvas(self):
        map_width, map_height = self.map_size
        map_width = Chip.pixel * map_width
        map_height = Chip.pixel * map_height 
        canvas = Canvas(
            master_frame = self.master,
            bg = "red",
            canvas_width = self.window_width,
            canvas_height = self.window_height - self.menu_height,
            canvas_postion_y = self.menu_height,
            map_width = map_width,
            map_height = map_height)
        # holderにmaster_chipを表示
#==============================================================================

if __name__ == "__main__":
    map_size = (100, 100)
    root = tk.Tk()

    b = Builder(root)
    b.init_note(map_size)
    b.set_window()

    # b.set_domain(map_size)
    b.set_menu()
    b.set_canvas()
    root.mainloop()

    
