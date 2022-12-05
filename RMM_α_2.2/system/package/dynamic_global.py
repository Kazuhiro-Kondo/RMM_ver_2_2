from static_global import Mode

import tkinter as tk
#==============================================================================
class Img:
    """画像クラス"""
    class Filepath:
        """str, ファイルパスクラス"""
    class png:
        """拡張子png"""

class Id:
    """型定義はされていないクラス"""
class Layer_class:
    pass
class Layer(Layer_class):
    """四次次元配列クラス"""
    
    @ classmethod
    def change(cls, number : int) -> Layer_class:
        layers = [
            Map.layer_0, Map.layer_1, Map.layer_2,
            Map.layer_3, Map.layer_4, Map.layer_5]
        return layers[number]

class Domain:
    """master_chipから作られる,"""
    class tag:
        """tagクラス"""
#==============================================================================
class Array:
    @ classmethod
    def make(cls,row : int, colume : int) -> list:
        """
        引数に作りたい0を除く、
        行（row）と列（colume）のマスの数を入れ、
        array[ 列 ][ 行 ][ タグの名前, 列, 行]
        の形で表現される２次元配列を返す。
        無効な値が入れられた際には空のリストを返す
        
        """
        array = []
        try:
            colume = int(colume)
            row = int(row)
            if row == 0 or colume == 0:
                print("無効な値(0)が代入されました")
                return array
            else:
                for c in range(0, colume):
                    array_c = []
                    for r in range(0, row):
                        array_c.append(None)
                        array_c[r] = [None, None]
                    array.append(array_c)
                return array
        except ValueError:
            print("ValueError")
            return array        
#==============================================================================
class Map:
    """モジュール間で動く変数を格納しておくクラス"""
    #_________________________________________________________________
    storage_tag : Domain = None     # [Chip.tag, x, y]
    #_________________________________________________________________
    storage_id  : Layer = None      # [Chip.tag]
    #_________________________________________________________________
    size : tuple = None             # マップの大きさ
    @ classmethod
    def width(cls) -> int:          # マップの横幅
        """横幅"""
        w, _ = Map.size
        return w
    @ classmethod
    def height(cls) -> int:         # マップの縦幅
        """縦幅"""
        _, h = Map.size
        return h
    #_________________________________________________________________
    # layer [y軸上の座標][X軸上の座標][storage_tag, storage_id]
    layer_0: Layer = None
    layer_1: Layer = None       # レイヤー、数が多きほど上の階層になる
    layer_2: Layer = None
    layer_3: Layer = None
    layer_4: Layer = None
    layer_5: Layer = None       # top_layerは全てのレイヤーの一番上
    #_________________________________________________________________
    # 出来たマップ画像
    image: Img.png = None
#==============================================================================
class MasterChips:
    """"""
    
#==============================================================================
class Chip:
    """モジュール間で動く変数を格納しておくクラス"""
    #_________________________________________________________________
    storage_id: Id = None   # master_chipから作ったIDを保管しておく
    #_________________________________________________________________
    domain: Domain = None       # holder上でchipを選択する際に必要な領域   
    tag: Domain.tag = None      # 画像のファイルパスの拡張子を除いた部分
    #_________________________________________________________________
    pixel : int = 32            # チップの大きさ, 初期値で32ドット
#==============================================================================
class Set:
    update_timing = 60
    layer = Mode.LAYER_5
    image_edit = Mode.DRAW_POINT
    id_edit = Mode.WRITE_POINT
    open_window = Mode.OPEN_HOLDER
#==============================================================================
class Setting:
    icon_pixel : int = 24
    bg = "#f0f0f0"


    
#==============================================================================
class MouseEvent:
    pass

