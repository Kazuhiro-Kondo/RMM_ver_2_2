import tkinter as tk
from static_global import Word
#==============================================================================
class Img:
    """画像クラス"""
    class Filepath:
        """str, ファイルパスクラス"""
    class png:
        """拡張子png"""

#==============================================================================
class Color:
    bg = "#f0f0f0"

#==============================================================================
class Frame:
    """フレームウェジェットの作成クラス"""
    def __init__(
            self, master_frame : tk.Frame,
            bg = Color.bg, bd : int = None,
            width : int = None, height : int = None) -> None:
        """フレームのサイズを設定"""
        self.master_frame = master_frame
        self.sub_frame = tk.Frame(
            self.master_frame,
            bd = bd,
            width = width,
            height = height)
        self.sub_frame.config(bg = bg) 
        
    def pack(self, side : tk = tk.TOP, fill : tk = tk.X) -> None:
        """フレームの設置"""
        self.sub_frame.pack(
            side = side,            # どこからフレームを設置していくか
            fill = fill,            # フレームをどこまで伸ばすか
            anchor = tk.NW)         # 左上を基準にする
    def grid(
            self, matrix : tuple[int, int] = None, 
            row : int = None, column :int = None,
            columnspan : int = None,
            ) -> None:
        """フレームの設置"""
        if matrix != None:
            row, column = matrix
        self.sub_frame.grid(
            row = row, column = column,
            columnspan = columnspan
        )
    def place(self, x : int = 0, y : int = None) -> None:
        """フレームの設置"""
        self.sub_frame.place(x = x, y = y, anchor = tk.NW)
    
    def destroy(self):
        """フレームの破棄"""
        self.sub_frame.destroy()

    def forget(self):
        """フレームを隠す"""
        self.sub_frame.forget()
    def set_sub_frame(self) -> tk.Frame:
        """サブフレームを返す"""
        return self.sub_frame        
    
#==============================================================================
class Label:
    """ラベルウェジェットの作成クラス"""
    def __init__(
            self, frame : tk.Frame,
            text : Word = None, image : Img = None,
            width : int = None, height : int = None,
            bg : str = None,):
        self.label = tk.Label(
            master = frame,
            text = text, image = image,
            width = width, height = height,
            pady = 6 ,bg = bg)
        
    def grid(
            self, matrix :tuple[int, int] = None,
            row : int = None, column :int = None,
            columnspan : int = None):
        row, column = matrix
        self.label.grid(
            row = row, column = column,
            sticky = tk.N+tk.S,
            columnspan = columnspan 
        )
    def pack(self,side : tk = tk.LEFT):
        self.label.pack(side = side ,fill = tk.Y)
#==============================================================================
class Button:
    """
    ボタンの設定
    """
    def __init__(
            self, frame : tk.Frame = None,
            text : Word = None, image : Img = None,
            width : int = None, height : int = None,
            style : tk = tk.FLAT,
            command = None):
        """コンストラクタ"""
        self.frame = frame
        self.button = tk.Button(
            master = self.frame,                # ボタンを設置するフレーム
            relief = style,                     # ボタンのスタイルの変更
            text = text,                        # テキスト文の挿入
            image = image,                      # 画像
            width = width, height = height,     # 大きさの設定
            padx = 0, pady = 0,                 # ボタンの内部感覚の設定
            anchor = tk.CENTER,                 # ボタン内部表示の位置
            command = command)                  # コマンド
    def pack(self, side : tk = tk.LEFT):
        """左詰めで縦に伸ばす"""
        self.button.pack(side = side ,fill = tk.Y)
    def gird(
            self,
            matrix : tuple[int, int] = None,
            row : int = None, column :int = None,
            columnspan : int = None):
        """grid設定"""
        if matrix != None:                      # 行列が設定してあるなら
            row, column = matrix                # 行と列を設定
        self.button.grid(
            row = row, column = column,
            sticky = tk.N+tk.S,
            columnspan = columnspan
        )
#==============================================================================
class Checkbutton:
    """チェックボタンの設定"""
    def __init__(self, frame : tk.Frame, text : Word = None) -> None:
        """"""
        self.check_button = tk.Checkbutton(
            master = frame, text = text
        )
    def pack(self, side : tk = tk.LEFT):
        """チェックボタンの設置"""
        self.check_button.pack(side = side, fill = tk.Y)
#==============================================================================
class ScrollBar:
    def __init__(
            self, canvas : tk.Canvas,
            width : int,
            height : int) -> None:
        """
        スクロールバーの設定
        ※Frameクラスは不可
        canvas = キャンバス
        width : 横軸の長さ
        height : 縦軸の長さ
        """
        # 横軸のスクロールバーの設定
        # 横は下に表示
        bar_width = tk.Scrollbar(
            canvas, orient = tk.HORIZONTAL,
            width = 16) 
        bar_width.pack(side = tk.BOTTOM, fill = tk.X)  
        bar_width.config(command = canvas.xview) 
        # 縦軸のスクロールバーの設定
        # 縦は右に表示
        bar_height = tk.Scrollbar(
            canvas, orient = tk.VERTICAL,
            width = 16)
        bar_height.pack(side = tk.RIGHT, fill = tk.Y)   
        bar_height.config(command = canvas.yview)
        #コンフィグ
        canvas.config(
            yscrollcommand = bar_height.set,
            xscrollcommand = bar_width.set)
        canvas.config(
            scrollregion = (0, 0, width, height))

#==============================================================================
class Canvas:
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    def __init__(
            self, master_frame : tk.Frame = None,
            canvas_width : int = None,
            canvas_height : int = None,
            canvas_postion_x : int = 0,
            canvas_postion_y : int = None,
            map_width :int = None,
            map_height :int = None,
            ):
        canvas_frame = Frame(
            width = canvas_width,
            height = canvas_height,
            bg = "green",
            master_frame = master_frame)
        canvas_frame.place(
            x = canvas_postion_x,
            y = canvas_postion_y)
        self.frame = canvas_frame.set_sub_frame()
        canvas = tk.Canvas(
            master = self.frame,
            bg = "green", highlightthickness = 0)
        canvas.place(
            x =0, y= 0, 
            anchor = tk.NW,
            width = canvas_width,
            height = canvas_height,      
            )
        canvas.create_line(0,0,1000,1000)
        ScrollBar(
            canvas = canvas,
            width = map_width,
            height = map_height)
    
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

#==============================================================================   
