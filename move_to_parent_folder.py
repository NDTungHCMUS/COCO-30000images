import os
import shutil

def move_files_from_subdirs(root_dir, subfolders=('1', '2', '3')):
    """
    Move all files from the specified subfolders (named '1','2','3' by default)
    up one level into root_dir.
    """
    for sub in subfolders:
        sub_path = os.path.join(root_dir, sub)
        if not os.path.isdir(sub_path):
            print(f"Subfolder not found, skipping: {sub_path}")
            continue

        for fname in os.listdir(sub_path):
            src_path = os.path.join(sub_path, fname)
            if not os.path.isfile(src_path):
                continue  # bỏ qua thư mục con hoặc các mục không phải file

            dst_path = os.path.join(root_dir, fname)
            # Nếu đã có file trùng tên, thêm suffix tránh ghi đè
            if os.path.exists(dst_path):
                base, ext = os.path.splitext(fname)
                i = 1
                new_name = f"{base}_{i}{ext}"
                dst_path = os.path.join(root_dir, new_name)
                while os.path.exists(dst_path):
                    i += 1
                    new_name = f"{base}_{i}{ext}"
                    dst_path = os.path.join(root_dir, new_name)

            shutil.move(src_path, dst_path)
            print(f"Moved: {src_path} → {dst_path}")

    print("Hoàn tất di chuyển tất cả file từ các thư mục con lên thư mục gốc.")

if __name__ == "__main__":
    # Lấy thư mục hiện tại (nơi script được chạy)
    folder_A = os.getcwd()
    print(f"Root directory set to: {folder_A}")
    move_files_from_subdirs(folder_A)
