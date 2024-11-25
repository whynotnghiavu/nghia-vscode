
try:
    if os.path.exists(link):
        os.remove(link)
        print(f"Đã xóa symlink: {link}")
    os.symlink(os.path.abspath(path), link)
    print(f"Tạo link: {link}")
except OSError as e:
    print(f"Lỗi: {e}")
