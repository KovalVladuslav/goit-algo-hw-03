import os
import shutil
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Копіювання файлів з сортуванням за розширенням.')
    parser.add_argument('src_dir', help='Шлях до вихідної директорії')
    parser.add_argument('dst_dir', nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням "dist")')
    return parser.parse_args()

def copy_files(src_dir, dst_dir):
    try:
        # Перевіряємо чи існує вихідна директорія
        if not os.path.exists(src_dir):
            print(f"Директорія {src_dir} не існує.")
            return

        # Створюємо директорію призначення, якщо вона не існує
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        # Рекурсивно обходимо всі файли та піддиректорії у вихідній директорії
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            # Якщо це директорія, викликаємо функцію рекурсивно
            if os.path.isdir(item_path):
                copy_files(item_path, dst_dir)
            else:
                # Якщо це файл, отримуємо його розширення
                file_ext = os.path.splitext(item)[-1].lower().strip('.')
                # Створюємо піддиректорію для відповідного розширення
                ext_dir = os.path.join(dst_dir, file_ext if file_ext else 'others')

                # Перевіряємо, чи існує піддиректорія для цього типу файлів
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)

                # Копіюємо файл до відповідної піддиректорії
                try:
                    shutil.copy2(item_path, ext_dir)
                    print(f"Файл {item} скопійовано до {ext_dir}")
                except Exception as e:
                    print(f"Не вдалося скопіювати файл {item}: {e}")
    except Exception as e:
        print(f"Помилка при обробці директорії {src_dir}: {e}")

if __name__ == "__main__":
    args = parse_args()
    copy_files(args.src_dir, args.dst_dir)
