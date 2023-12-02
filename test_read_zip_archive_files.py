import shutil
from zipfile import ZipFile
import os

my_files = ["hello_pdf.pdf", "hello_xlsx.xlsx", "hello_xlsx.csv"]
my_text = "Yipikaye motherfucker"
my_dir_name = "resources"
my_zip_name = "/zip_file.zip"
CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)


def create_files_with_text(files, text):
    for f in files:
        with open(f, "w") as file:
            file.write(text)


def create_dir(dir_name):
    if not os.path.exists(dir_name):
        path = os.path.join(CURRENT_DIR, dir_name)
        os.mkdir(path)


def create_zip_and_write_in_files(dir_name, zip_name, files):
    with ZipFile(dir_name + zip_name, "a") as zip_file:
        for f in files:
            zip_file.write(f)


def delete_dir_and_files(dir_name, files):
    shutil.rmtree(os.path.join(CURRENT_DIR, dir_name))
    for file in files:
        os.remove(os.path.join(CURRENT_DIR, file))


def test_read_zip_archive_files():
    create_files_with_text(files=my_files, text=my_text)
    create_dir(dir_name=my_dir_name)
    create_zip_and_write_in_files(dir_name=my_dir_name, zip_name=my_zip_name, files=my_files)
    with ZipFile("resources/zip_file.zip", "r") as zip_file:
        for file in my_files:
            assert file in zip_file.namelist()
            assert my_text in str(zip_file.read(file))
    delete_dir_and_files(dir_name=my_dir_name, files=my_files)






