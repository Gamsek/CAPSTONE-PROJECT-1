import os 
import CRUD as CRUD


sistem_operasi = os.name 
match sistem_operasi :
            case "nt" : os.system("cls")
            case "posix" : os.system("clear")
print("SELAMAT DATANG DI PROGRAM")
print("DATABASE YELLOW PAGES UMKM")
print("==========================")

#check database itu ada atau gak 
CRUD.init_console()

# Program Utama 
def MainYP():
    match sistem_operasi :
        case "nt" : os.system("cls")
        case "posix" : os.system("clear")
    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE YELLOW PAGES UMKM")
    print("==========================")
    while(True):
        print("MENU UTAMA YELLOW PAGES UMKM")
        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data")
        print(f"5. Exit Program")

        user_opsi = input("Masukkan opsi antara 1-5: ")
        print("=========================================")
        if user_opsi == '1':
            CRUD.readmenu_console()
        elif user_opsi == '2':
            CRUD.create_console()
        elif user_opsi == '3':
            CRUD.update_console()
        elif user_opsi == '4':
            CRUD.delete_console()
        elif user_opsi == '5':
            while(True):
                if user_opsi == '5':
                      print('Apakah Yakin Akan Keluar dari Program?')
                      user_opsi = input('Masukkan (y/t): ')
                      if str.isalpha(user_opsi.lower()) == 't':
                        break
                      elif str(user_opsi.lower()) == 'y':
                        print("""===============TERIMAKASIH===============
===========SELAMAT BERAKTIFITAS==========
==========SUKSES UNTUK USAHANYA!=========""") 
                        return
                break
        else:
            print('Masukkan angka sesuai dengan pilihan menu (1-5)')
            continue
             
MainYP()


