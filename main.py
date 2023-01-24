from pathlib import Path

dir_suff_dict = {"Images": ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.ico', '.bmp', '.webp', '.svg'],
                 "Documents": [".pdf", ".txt", ".docx", ".doc", ".ods", ".odt", ".dotx", ".docm", ".dox",
                               ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".xml"],
                 "Archives": [".iso", ".tar", ".gz", ".7z", ".dmg", ".rar", ".zip"],
                 "Audio": [".aac", ".m4a", ".mp3", "ogg", ".raw", ".wav", ".wma"],
                 "Video": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mpg", ".mpeg", ".3gp"],
                 }



def sort_func(path_dir):
    cur_dir = Path(path_dir)
    for file in cur_dir.iterdir():
        if file.is_dir():
            if file.stat().st_size == 0:
                file.rmdir()
        for suff in dir_suff_dict:
            if file.suffix.lower() in dir_suff_dict[suff]:
                dir_img = cur_dir / suff
                dir_img.mkdir(exist_ok=True)
                file.rename(dir_img.joinpath(file.name))


if __name__ == "__main__":
    path_d = input('[+] Введите путь к директории для сортировки: ')
    if not Path(path_d).exists():
        print('[-] Директории не существует')
    else:
        sort_func(path_d)
    print('[!] Сортировка завершена')