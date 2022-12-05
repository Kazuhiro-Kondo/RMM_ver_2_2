#==============================================================================
import tkinter as tk
from widget import Frame, Button, Label, Checkbutton
from static_global import Word, Number, Mode
from dynamic_global import Set

#==============================================================================
class Menu(tk.Frame):
    """builderのメニュー"""
    def __init__(
            self, master_frame : tk.Frame,
            header_height : int = 24,
            mega_height : int = 32) -> None:
        """
        master_frame = フレーム
        header_height = ヘッダーの高さ幅
        mega_height = メガメニューの高さ幅
        """
        super().__init__(master_frame)
        self.master_frame = master_frame
        # ヘッダーの高さ
        self.header_height = header_height
        # メガメニューの高さ
        self.mega_height = mega_height
        # 各フレームの初期値
        self.id_frame = None
        self.id_frame = None
        self.display_frame = None
        self.setting_frame = None
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # ヘッダーの設定
    def set_header(self) -> None:
        """ヘッダー"""
        # メニューフレームの作成
        header_frame = Frame(
            master_frame = self.master_frame,
            height = self.header_height)
        header_frame.pack()
        self.header_frame = \
            header_frame.set_sub_frame()
        # メニューボタン
        menu_button = Button(              
            frame = self.header_frame,
            text = Word.menu)
        menu_button.pack()
        # 画像編集切り替えボタン
        image_button = Button(              
            frame = self.header_frame,
            command = lambda : self.go_image_edit(),
            text = Word.image_edit)
        image_button.pack()
        # ID編集切り替えボタン
        id_button = Button(                 
            frame = self.header_frame,
            command = lambda : self.go_id_edit(),
            text = Word.id_edit)
        id_button.pack()
        # 表示設定切り替えボタン
        display_button = Button(            
            frame = self.header_frame,
            command = lambda : self.go_display(),
            text = Word.display)
        display_button.pack()
        # 設定切り替えボタン
        setting_button = Button(
            frame = self.header_frame,
            command = lambda : self.go_setting(),
            text = Word.setting)
        setting_button.pack()
        # ヒントボタン
        tip_button = Button(              
            frame = self.header_frame,
            text = Word.tip)
        tip_button.pack(side = tk.RIGHT)
        
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # メガメニューの設定     
    def set_mega(self) -> None:
        """メガメニュー"""
        # ベースとなるフレームの作成と設置
        mega_frame = Frame(
            master_frame = self.master_frame, bg = "blue")
        mega_frame.pack()
        # メガメニューのフレームの設定
        self.mega_frame = mega_frame.set_sub_frame()        
        # 最初に表示させる初期画面(image_edit)
        self.set_image_frame()                  
        
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # 各フレームの作成メソッド
    
    def set_image_frame(self):
        """画像編集画面を作成する"""
        # ベースとなるフレームの作成と設置
        self.image_frame = Frame(master_frame = self.mega_frame)      
        self.image_frame.pack()
        # 作成したフレームに乗せるウェジェット
        SetImageMenu(frame = self.image_frame.set_sub_frame())
        # Holderを開く
        Set.open_window = Mode.OPEN_HOLDER

    def set_id_frame(self):
        """ID編集画面を作成する"""
        # ベースとなるフレームの作成と設置
        self.id_frame = Frame(master_frame = self.mega_frame)
        self.id_frame.pack()
        # 作成したフレームに乗せるウェジェット
        SetIdMenu(frame = self.id_frame.set_sub_frame())
        # Writerを開く
        Set.open_window = Mode.OPEN_WRITER
        
    def set_display_frame(self):
        """画面設定の画面を作成する"""
        # ベースとなるフレームの作成と設置
        self.display_frame = Frame(
            master_frame = self.mega_frame)
        self.display_frame.pack()
        # 作成したフレームに乗せるウェジェット
        SetDisplayMenu(frame = self.display_frame.set_sub_frame())
        # サブウインドウを閉じる
        Set.open_window = Mode.CLOSE_WINDOW

    def set_setting_frame(self):
        """設定画面を作成する"""
        # ベースとなるフレームの作成と設置
        self.setting_frame = Frame(
            master_frame = self.mega_frame)
        self.setting_frame.pack()
        # 作成したフレームに乗せるウェジェット 
        # サブウインドウを閉じる
        Set.open_window = Mode.CLOSE_WINDOW
        
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # フレーム変更コマンド
    def go_image_edit(self):
        """画像編集画面に変更をする"""
        # フレームの破棄
        self.destroy_frame(
            [self.image_frame, self.id_frame,
             self.display_frame, self.setting_frame])
        # 変更するフレームの作成
        self.set_image_frame()
    
    def go_id_edit(self):
        """ID編集画面に変更をする"""
        # フレームの破棄
        self.destroy_frame(
            [self.image_frame,self.id_frame,
             self.display_frame, self.setting_frame])
        # 変更するフレームの作成
        self.set_id_frame()
        
    def go_display(self):
        """表示設定画面に変更をする"""
        # フレームの破棄
        self.destroy_frame(
            [self.image_frame,self.id_frame,
             self.display_frame, self.setting_frame])
        # 変更するフレームの作成
        self.set_display_frame()
        
    def go_setting(self):
        """設定画面に変更をする"""
        # フレームの破棄
        self.destroy_frame(
            [self.image_frame,self.id_frame,
             self.display_frame, self.setting_frame])
        # 変更するフレームの作成
        self.set_setting_frame()
        
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # フレーム削除メソッド  
    def destroy_frame(self, frame_list : list) -> None:
        frame : Frame = None
        for frame in frame_list:
            if frame == None:
                pass
            else:
                frame.destroy()

#==============================================================================
class SetImageMenu:
    """イメージメニュークラス"""
    def __init__(self, frame : Frame):
        """frame = フレーム"""
        self.frame = frame
        self.set_label(text = Word.layer)           # レイヤー(ラベル)
        self.set_button(                            # レイヤー(ボタン)
            mode = Mode.SELECT_LAYER,
            quantity = 6)               
        self.set_label(text = Word.edit)            # 描画(ラベル)
        self.set_button(                            # 描画(ボタン)
            mode = Mode.SELECT_DRAW,
            quantity = 5)              
        self.set_label(text = Word.eraser)          # 消しゴム(ラベル)
        self.set_button(                            # 消しゴム(ボタン)
            mode = Mode.SELECT_CLEAR,
            quantity = 5)               
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # ラベル作成メソッド
    def set_label(self, text : Word = None) -> None:
        """text = 表示させるテキスト(Wordクラスを使う(str))"""
        label = Label(frame = self.frame, text = text)
        label.pack()
 
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # ボタン作成メソッド 
    def set_button(self, mode : Mode = None, quantity : int = None)-> None:
        """quantity = 個数"""
        self.button = []
        # 入力された個数分繰り返して処理する
        for number in range(quantity):

            self.button.append(
                Button(frame = self.frame,      # Buttonクラス
                       style = tk.RAISED,
                       command = self.command(mode, number),
                       width = 2)
            )
            # 入力された個数分設置する
            self.btn(number).pack()

    def command(self, mode, number):
        """モード切替のコマンド"""
        def inner():
            if mode == None:
                pass
            # レイヤーの変更
            elif mode == Mode.SELECT_LAYER:
                Set.layer = f"{mode}_{number}"
            # 画像編集の編集モードの変更
            elif mode == Mode.SELECT_DRAW \
                    or mode == Mode.SELECT_CLEAR:
                Set.image_edit = f"{mode}_{number}"
        return inner
                
    def btn(self, number : int) -> Frame:
        """ボタン作成用の関数"""
        return self.button[number]
#==============================================================================
class SetIdMenu(SetImageMenu):
    """SetImageMenuクラスを継承する"""
    def __init__(self, frame) -> None:
        """frame = フレーム"""
        self.frame = frame
        self.set_label(text = Word.edit)            # 描画(ラベル)
        self.set_button(                            # 描画(ボタン)
            mode = Mode.SELECT_WRITE,
            quantity = 5)               
        self.set_label(text = Word.eraser)          # 消しゴム(ラベル)
        self.set_button(                            # 消しゴム(ボタン)
            mode = Mode.SELECT_ERASE,
            quantity = 5)               
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # ラベル作成メソッド
    def set_label(self, text : Word = None) -> None:
        """text = 表示させるテキスト(Wordクラスを使う(str))"""
        super().set_label(text)
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # ボタン作成メソッド 
    def set_button(
            self, mode : Mode = None, quantity: int = None) -> None:
        """quantity = 個数"""
        super().set_button(mode, quantity)

    def command(self, mode, number):
        """モード切替のコマンド"""
        def inner():
            if mode == None:
                pass
            # ID編集の編集モードの変更
            elif mode == Mode.SELECT_WRITE \
                    or mode == Mode.SELECT_ERASE:
                Set.id_edit = f"{mode}_{number}"
        return inner
    def btn(self, num) -> Frame:
        """ボタン作成用の関数"""
        super().btn(num)
        return self.button[num]
#==============================================================================
class SetDisplayMenu:
    def __init__(self, frame):
        """frame = フレーム"""
        self.frame = frame
        self.set_check_button(Word.coordinate)
        self.set_check_button(Word.grid)
        self.set_check_button(Word.states_bar)
    
    
    def set_check_button(self, text : Word = None):
        check_button = Checkbutton(frame = self.frame, text = text)
        check_button.pack()

#==============================================================================

class SubMenu(tk.Frame):
    """builder以外のメニュー"""
    def __init__(
        self, master_frame : tk.Frame  = None,
        header_height : int = None):
        super().__init__()
        self.master_frame = master_frame
        # ヘッダーの高さ
        self.header_height = header_height
        # ヘッダーフレームの初期値
        self.header_frame = None
    
    def set_header(self):
        """ヘッダーの設定"""
        # ヘッダーフレームの設定
        header_frame = Frame(
            master_frame = self.master_frame,
            height = self.header_height)
        header_frame.pack()
        self.header_frame = header_frame.set_sub_frame()
        # メニューボタン
        menu_button = Button(              
            frame = self.header_frame,
            text = Word.menu)
        menu_button.pack()      
        update_button = Button(              
            frame = self.header_frame,
            text = Word.update)
        update_button.pack(side = tk.RIGHT)