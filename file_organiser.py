import os

# Vybereme cestu ke složce a zkontrolujeme, jestli existuje
def choose_path():
    directory = input("Enter path: ")

    if os.path.exists(directory):
        files = os.listdir(directory)
        return files, directory
    else:
        print("The entered path does not exist. Please enter a valid path.")
        return choose_path()
    
def folder(name, new_directory):
    new_folder = os.path.join(new_directory, name)
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)


def file_type(files, directory):
    for file in files:
        file_name, file_extension = os.path.splitext(file)
        file_extension = file_extension[1:]
        print("Name:", file_name, "Extension:", file_extension)
        folder(file_extension, directory)

file_type(*choose_path())
