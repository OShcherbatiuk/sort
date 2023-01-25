import os
import re
from pathlib import Path
import shutil

dir_suff_dict = {"Images": ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.ico', '.bmp', '.webp', '.svg'],
                 "Documents": [".md", ".pdf", ".epub", ".txt", ".docx", ".doc", ".ods", ".odt", ".dotx", ".docm",
                               ".dox",
                               ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".xml"],
                 "Archives": [".iso", ".tar", ".gz", ".7z", ".dmg", ".rar", ".zip"],
                 "Audio": [".aac", ".m4a", ".mp3", "ogg", ".raw", ".wav", ".wma"],
                 "Video": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mpg", ".mpeg", ".3gp"]}


def normalize(name: str) -> str:
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = (
        "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
        "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g"
    )

    TRANS = {}
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    t_name = name.translate(TRANS)
    t_name = re.sub(r'\W', '_', t_name)
    return t_name


def sort_file(path):
    cur_dir = Path(path)
    dir_path = []

    for root, dirs, files in os.walk(path):
        for item in dirs:
            dir_path.append(Path(root) / item)
        for file in files:
            file_path = Path(root) / file
            name_normalize = f"{normalize(file_path.name[0:-len(file_path.suffix)])}{file_path.suffix}"
            file_path.rename(Path(root) / name_normalize)
            file_path = Path(root) / name_normalize
            for suff in dir_suff_dict:
                if file_path.suffix.lower() in dir_suff_dict[suff]:
                    (cur_dir / "move_files").mkdir(exist_ok=True)
                    dir_move = cur_dir / "move_files" / suff
                    dir_move.mkdir(exist_ok=True)
                    try:
                        if file_path.suffix.lower() in [".tar", ".gztar", ".bztar", ".xztar", ".zip"]:
                            try:
                                shutil.unpack_archive(file_path, dir_move)
                                Path(file_path).unlink()
                            except ValueError:
                                print("Формат для распаковки не зарегистрирован")
                                continue
                        else:
                            shutil.move(file_path, dir_move)
                    except FileExistsError:
                        file_path = f'{file_path.parent / file_path.name.split(file_path.suffix)[0]}_c{file_path.suffix}'
                        shutil.move(file_path, dir_move / file_path)
                        print(f"Duplicate?: {file_path}")

    for dir_p in reversed(dir_path):
        os.rmdir(dir_p)


if __name__ == "__main__":
    path_d = input('[+] Choose path: ')
    if not Path(path_d).exists():
        print('[-] Not found')
    else:
        sort_file(path_d)
    print('[!] Finish')
