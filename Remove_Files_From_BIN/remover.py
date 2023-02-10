import os

file_path = r'C:\Users\bilsk\Downloads'

print(file_path)

check = os.path.isdir(file_path)
print(check)

if os.path.isdir(file_path):
    for files in os.listdir(file_path):
        try:
            os.remove(os.path.join(file_path, files))
            print('File named ' + files + ' was removed!')
        except PermissionError:
            print('You do not have permission to delete the file named ' + files)      
else:
    print('No files in the downloads folder were detected. There is nothing to be deleted here.')