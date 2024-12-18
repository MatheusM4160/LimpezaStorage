from PIL import Image
from os.path import join,split


def create_thumbnail(filename:str,path_dest:str,size:tuple=(640,640)) -> None:
    """
    Create miniature  the files for tifs
     filename: str = Caminho completo do arquivo
     path_dest: str = Caminho da pasta de destino do novo arquivo
     size: tuple[int,int] = Largura e altura em pixels da thumbnail


    """
    try:
        __,n = split(filename)
        new = f"bolsinha__{n.replace('tif','bmp')}"
        new_name = join(path_dest,new)
        with Image.open(filename) as im:
            print(f"{new_name}")
            if im.mode != 'RGB':
                    im = im.convert('RGB')
            im.thumbnail(size)
            im.save(new_name)
            return new_name
    except:
         pass