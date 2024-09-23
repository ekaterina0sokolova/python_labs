import re
import os


def main():
    input_path = "folder_main"

    file_count = 0
    txt_count = 0

    for dirpath, dirnames, filenames in os.walk(input_path):
        for filename in filenames:
            file_count += 1
            if filename.endswith('.txt'):
                txt_count += 1  # Увеличиваем счетчик .txt файлов
                # Формируем новое имя файла
                new_filename = filename[:-4] + '_backup.txt'  # Добавляем _backup к имени
                # Полный путь к старому и новому файлам
                old_file_path = os.path.join(dirpath, filename)
                new_file_path = os.path.join(dirpath, new_filename)
                # Переименовываем файл
                os.rename(old_file_path, new_file_path)
                print(f"Файл {filename} переименован в {new_filename}")

    dif_file = file_count - txt_count

    # Выводим результаты
    print(f"Общее количество файлов: {file_count}")
    print(f"Количество .txt файлов: {txt_count}")
    print(f"Разность между общим количеством файлов и .txt файлами: {dif_file}")


if __name__ == '__main__':
    main()