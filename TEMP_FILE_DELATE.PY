import os
def delete_temp():
    folder_path = r'C:\Users\GLOBAL\AppData\Local\Temp'
    for root, dir, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
            except PermissionError:
                pass
            except Exception:
                pass

delete_temp()