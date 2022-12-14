import os

path = r'D:\TEST'
total_size = 0
path, dirs, files = next(os.walk(path))
for f in files:
    fp = os.path.join(path, f)
    total_size += os.path.getsize(fp)

print('Размер каталога (в Кб): ', total_size / 1024)
print('Количество подкаталогов: ', len(dirs))
print('Количество файлов: ', len(files))