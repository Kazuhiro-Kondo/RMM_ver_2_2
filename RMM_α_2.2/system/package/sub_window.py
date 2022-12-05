#==============================================================================
import tkinter as tk
from dynamic_global import Map, Chip, Set, Array
from static_global import Word, Mode
from menu import Menu, SubMenu
from canvas import Canvas
#==============================================================================
class SettingHolder:
    """
    Holderクラスの画面のサイズなどを設定するクラス,
    SettingBuilderクラスに依存する。
    """
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
        w = str(self.max_width() // 2 + 16)
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
    def set_domain(self, map_size):
        """"""
        self.map_size = map_size
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
        w = str(self.max_width()  // 2+ 16)
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
            self, master : tk.Tk, main_master : tk.Tk  =None) -> None:
        """windowの初期設定と各クラスのインスタンス化を行う"""
        super().__init__(master)
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self.delete_window)
        self.main_master = main_master
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
    def set_domain(self, map_size):
        """"""
        self.map_size = map_size
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