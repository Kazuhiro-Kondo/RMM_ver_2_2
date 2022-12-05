#==============================================================================
class Number:
    """変数, 定数に数を割り振るクラス"""
    n = 0
    b = 0
    def number() -> int:
        """番号を振る関数"""
        Number.b += 1
        return Number.b
#==============================================================================
class Mode(Number):
    """モード"""
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    def number() -> int:
        """番号を振る関数"""
        Number.n += 1
        return Number.n
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # 保持の状態
    
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # メニューモードの選択
    FILE_OPERATE : int = number()       # ファイルメニューを開く
    IMAGE_EDIT : int = number()         # 画像編集モード
    ID_EDIT : int = number()            # ID編集モード
    DISPLAY :str = number()
    SETTING : int = number()            # 設定変更
    TIP : int = number()                # ヒントを開く
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # Mode.FILE_OPRATEの中身
    FILE_NEW : int = number()           # 新規
    FILE_OPEN : int = number()          # 開く
    FILE_UPDATE :int = number()         # 上書き保存
    FIFE_SAVE : int = number()          # 名前を付けて保存
    FIFE_MENE_CLOSE : int = number()    # 閉じる
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # Mode.IMAGE_EDITの中身
    # レイヤー
    SELECT_LAYER : int = number() 
    LAYER_0 : str = f"{SELECT_LAYER}_0"
    LAYER_1 : str = f"{SELECT_LAYER}_1"
    LAYER_2 : str = f"{SELECT_LAYER}_2"
    LAYER_3 : str = f"{SELECT_LAYER}_3"
    LAYER_4 : str = f"{SELECT_LAYER}_4"
    LAYER_5 : str = f"{SELECT_LAYER}_5"

    # 描画
    SELECT_DRAW : int = number() 
    DRAW_POINT : str = f"{SELECT_DRAW}_1"
    DRAW_LINE : str = f"{SELECT_DRAW}_2"
    DRAW_RECTANGLE : str = f"{SELECT_DRAW}_3"
    DRAW_CIRCLE : str = f"{SELECT_DRAW}_4"
    DRAW_FILL : str = f"{SELECT_DRAW}_5"
    # 消去
    SELECT_CLEAR : int = number()
    CLEAR_POINT : str = f"{SELECT_CLEAR}_1"
    CLEAR_LINE : str = f"{SELECT_CLEAR}_2"
    CLEAR_RECTANGLE : str = f"{SELECT_CLEAR}_3"
    CLEAR_CIRCLE : str = f"{SELECT_CLEAR}_4"
    CLEAR_FILL : str = f"{SELECT_LAYER}_5"
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # Mode.ID_EDITの中身
    # 描画
    SELECT_WRITE : int = number()
    WRITE_POINT : str = f"{SELECT_WRITE}_1"
    WRITE_LINE : str = f"{SELECT_WRITE}_2"
    WRITE_RECTANGLE : str = f"{SELECT_WRITE}_3"
    WRITE_CIRCLE : str = f"{SELECT_WRITE}_4"
    WRITE_FILL : str = f"{SELECT_WRITE}_5"
    # 消去
    SELECT_ERASE : int = number()
    ERASE_POINT : str = f"{SELECT_ERASE}_1"
    ERASE_LINE : str = f"{SELECT_ERASE}_2"
    ERASE_RECTANGLE : str = f"{SELECT_ERASE}_3"
    ERASE_CIRCLE : str = f"{SELECT_ERASE}_4"
    ERASE_FILL : str = f"{SELECT_ERASE}_5"
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # Mode.DISPLAYの中身
    # ZOOM_UP : int = number()            # 拡大
    # ZOOM_DOWN : int = number()          # 縮小
    SHOW_GRID_LINE : int = number()     # グリッド線の表示
    SHOW_COORDINATE : int = number()    # 座標の表示
    SHOW_STATUS_BAR : int = number()    # ステータスバーの表示
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # Mode.SETTINGの中身
    CHANGE_MAPSIZE : int = number()     # マップサイズの変更
    CHANGE_LANGUAGE : int = number()    # 言語の変更
    # SETTING_SHORT_CUT : int = number()
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # Mode.TIPの中身
    TIP : int = number()
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # ウインドウのモード設定
    
    OPEN_HOLDER = number()
    OPEN_WRITER = number()
    CLOSE_WINDOW = number()



#==============================================================================
class Word:
    """画面に表示される文字"""
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # タイトル
    title = "RMM"
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # ヘッダー
    menu = "メニュー"
    image_edit = "画像編集"
    id_edit = "ID編集"
    display = "表示"
    setting = "設定"
    tip = "？"
    update = "更新"
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # メニュー
    new = "新規作成"
    open_file = "開く"
    save = "名前を付けて保存"
    close = "閉じる"
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # 画像編集とID編集
    layer = "レイヤー"
    edit = "描画"
    eraser = "消しゴム"
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    # 表示
    coordinate = "座標"
    grid = "グリッド線"
    states_bar = "ステータスバー"
#==============================================================================
