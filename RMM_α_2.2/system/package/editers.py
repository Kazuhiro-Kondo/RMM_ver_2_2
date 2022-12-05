#==============================================================================
# osのインポート
import os
# shutilのインポート
import shutil
# globのインポート
import glob
# PILのインポート
from PIL import Image
#==============================================================================
class Path:
    images_chips : str = "../images/chips/"
    user_chips : str  = "../../user/chips/"
#==============================================================================
class OperateDirectory:
    """ディレクトリ操作に関する処理をまとめたクラス"""
    
    def __init__(self):
        pass
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    def make_folder(
            self, path : str = None,
            folder_name : str = None) -> None:
        """
        フォルダの作成メソッド
        指定したフォルダ内に同一ファイルが
        既に存在している場合は処理しない。
        """
        if folder_name != None:
            name = f"{path + folder_name}"
        else:
            name = path
        try:
            os.mkdir(name)
        except FileExistsError:
            print(
                "既に存在するフォルダ:"
                + f"{folder_name}を作成することはできません")

    def delete_folder(self, path : str = None) -> None:
        """フォルダの削除"""
        shutil.rmtree(path)
    
    def clear_image_chips(self):
        """フォルダーのリフレッシュ"""
        files = self.return_dir(Path.images_chips)
        for i in range(len(files)):
            path = f"{Path.images_chips}/{files[i]}" 
            self.delete_folder(path = path)
        else:
            self.make_folder(
                path = Path.images_chips, folder_name = None
            )
        
    def return_dir(self, path : str = None) -> list:
        """フォルダー内のフォルダーを返す"""
        return os.listdir(path)
    def search_dir(
            self, path : str = None,
            extension : str = "png") -> list:
        """指定したパスにあるファイル名のリストを返す"""
        f = glob.glob(
            f"{path}*.{extension}")
        return f
    def base_name(self, path) -> str:
        """---.png の---の部分を取得して返す"""
        n = os.path.splitext(os.path.basename(path))[0]
        return n
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    def make_master_chips_folder(self):
        """
        master_chipごとにフォルダを作成する
        ../images/chips/内に作成
        """
        files = self.search_dir(Path.user_chips)
        for i in range(len(files)):
            # それぞれのファイル名を取得(---.png の---の部分)
            file_name = os.path.splitext(
                os.path.basename(files[i]))[0]
            # ../images/chips/の中に先ほど取得した---の部分が
            # ファイル名になるフォルダを作成する。
            self.make_folder(
                path = Path.images_chips, folder_name = file_name
            )
        
#==============================================================================
class DivideImage:
    """
    画像を分割する項目をまとめたクラス
    処理は一枚ごとに行う
    """
    #―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    def __init__(self, image_size : int = 32):
        """
        file_pathに大きさを変えたい画像のファイルパス、
        image_sizeに変えたい大きさのサイズ(初期値は32ピクセル)
        コンストラクタ上で処理を行う

        """
        # 分割するサイズの決定
        self.size = image_size
        # ファイル操作
        operate_dir = OperateDirectory()
        # ../../user/chips/内にある画像ファイルのリスト化
        file_list = operate_dir.search_dir(Path.user_chips)
        # ./images/chips/内にそれぞれのmaster_chipに対応する
        # 名前のフォルダを作成
        operate_dir.make_master_chips_folder()
        # ファイルリスト分繰り返して処理
        for i in range(len(file_list)):
            # 分割するファイル
            file = file_list[i]
            # ファイルパスの--.png の---の部分を取得する
            name = operate_dir.base_name(file)
            # 画像を開く
            self.image = Image.open(file)
            self.width = self.image.width
            self.height = self.image.height
            # 画像のサイズを変更
            self.resize_image()
            # 画像の分割
            self.save_divide(name = name)
        # なんとなく書いてある。
        # もしかしたら今後必要になるかもしれない処理
        else:
            self.image = None
            self.width = None
            self.height = None
    #――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 
    def resize_image(self):
        """
        元の画像のサイズが分割したサイズで,
        割り切れない場合の処理。
        例えば, 100なら, 32*3 + 4なので,
        100から4引いた値にリサイズされる。
        """
        # 縦横の幅が同じじゃない場合にサイズをリサイズする
        if self.width % self.size != 0 or self.height % self.size != 0:
            #元の画像の長さ + (分割サイズ - (元の画像 % 分割サイズ))
            self.width \
                = self.width \
                + (self.size - (self.width % self.size))
            self.height \
                = self.height \
                +(self.size - (self.height % self.size))
            # 画像の縦横の大きさを分割サイズに合わせて、変更する
            self.image = self.image.resize((self.width, self.height))

    def save_divide(self, name : str) -> None:
        """
        フォルダーを作って, 分割した画像を格納する。
        既にフォルダーがある場合はエラーを返す。
        """
        # 分割する幅
        width = self.width // self.size
        height = self.height // self.size
        # ここから下が分割処理となる
        # =============
        # xとyがごちゃまぜになる正直よくわからない
        # =============
        images = []
        for y in range(height):
            images_y = []
            for x in range(width):
                images_y.append(
                    self.image.crop((
                        x * 32, y * 32,
                        x * 32 + 32, y * 32 + 32)))
            images.append(images_y)
        self.images = images        
        for y in range(height):
            for x in range(width):
                self.div_func(x, y).save(
                    f"{Path.images_chips}/{name}/{name}_{y}_{x}.png")
                
    def div_func(self, x : int, y : int) -> list:
        """動的な関数作成用"""
        return self.images[y][x]



    
if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    DivideImage()
    op = OperateDirectory()
    a = input()
    op.clear_image_chips()