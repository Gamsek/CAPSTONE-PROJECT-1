from . import OperasiYP

DB_NAME = "C:\PURWADHIKA\CAPSTONE PROJECT MODULE 1\Data\data.csv"
TEMPLATE = {
    "pk":"XXXXX",
    "nama_usaha":" ",
    "kategori_usaha":" ", 
    "alamat":" ", 
    "telepon":" ", 
    "email":" ",
}

def init_console():
    try: 
        with open(DB_NAME,"r") as file:
            print("Database tersedia")
    except:
        print("Database tidak tersedia, silahkan membuat database baru ")
        OperasiYP.create_first_data()