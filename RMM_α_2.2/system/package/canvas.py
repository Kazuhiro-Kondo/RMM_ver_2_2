import tkinter as tk
from dynamic_global import Img , Layer 
from dynamic_global import Map, Chip, Set
from static_global import Word
from widget import ScrollBar,Frame
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
            bg : str = "green"
            ):
        # キャンバスフレームの設定
        canvas_frame = Frame(
            width = canvas_width,
            height = canvas_height,
            bg = "red",
            master_frame = master_frame)
        # キャンバスフレームの場所の決定
        canvas_frame.place(
            x = canvas_postion_x,
            y = canvas_postion_y)
        # フレームの設定
        self.frame = canvas_frame.set_sub_frame()
        # キャンバスの設定
        canvas = tk.Canvas(
            master = self.frame,
            bg = bg, highlightthickness = 0)
        # キャンバスの配置
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
        self.master = master_frame
        self.canvas = canvas
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    def display_background_image(
            self, canvas :tk.Canvas,
            width : int, height :int) -> None:
        """
        背景用の画像を表示させる.
        map_sizeと同じだけ表示。
        """
        bg_file_path : str = "../images/icons/checkered.png"
        self.bg_image = tk.PhotoImage(
            file = bg_file_path, master = self.master)
        # 指定されたサイズ分, 背景画像を置く
        for y in range(0, width // Chip.pixel):
            for x in range(0, height // Chip.pixel):
                canvas.create_image(
                    y * Chip.pixel,
                    x * Chip.pixel,
                    image = self.bg_image,
                    tag = "BG", anchor = tk.NW)
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    def domain_draw(self, domain : list) -> None:
        """
        holderにマスターチップを表示するメソッド
        domainはグローバル領域から取得した2次元配列
        """
        # 下のself.domain_imagesは、
        # なぜかself.を付けないと画像が表示されない、
        # おそらくcreta_imageのスコープの関係か、
        # mainloopで画像を削除している可能性がある。
        self.domain_images : list = []
        # 空のリストの作成。
        # ここもないと上手く動かない
        for _ in range(0, len(domain)):
            self.domain_images.append(None)
        for i in range(0,len(domain)):     
            name : str = domain[i][0]    
            # 左上寄せで順に画像を表示するため
            # 始点のyの情報しか必要ない
            place_y : int = domain[i][2]  
            self.domain_images[i] = tk.PhotoImage(
                file = f"../images/chips/{name}/{name}.png",
                master = self.master)       # masterを設定しないと表示が
            self.canvas.create_image(       # 出来ない
                0, place_y ,
                image = self.domain_images[i],
                tag = "HOLDER",
                anchor = "nw")
            Map.tags.append(name) 
    def main_draw(self) -> None:   
        """メインの描画処理"""
        # 現在のレイヤーの参照
        # Set.layer : str = {Mode}_{number}なので
        # Set.layer[-1]はnumberを取得する
        layer_number =  int(Set.layer[-1])
        # 表示させるレイヤー(layer)の決定
        layer = Layer.change(layer_number)
        

        # self.image_list = None
        # for y in range(Map.height()):
        #     for x in range(Map.width()):
        #         if layer[y][x][0] != None:      # layerのセルが空でなければ
        #             self.image_list[y][x] = tk.PhotoImage(
        #                 file = Map.storage_tag,
        #                 master = self.master
        #             )
        #             self.canvas.create_image(
        #                 image = self.image_list[y][x],
        #                 tag = "BUILDER",
        #                 anchor = tk.NW
        #             )
            
        # 更新
        self.master.after(Set.update_timing, self.main_draw)

    #=========================================================================# 
   