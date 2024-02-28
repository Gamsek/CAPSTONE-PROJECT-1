from . import Database
from .utiliti import random_string
import os
from . import validasi

def delete(no_usaha):
    """
    Fungsi ini digunakan untuk menghapus data usaha berdasarkan nomor urut.

    Parameters:
    - no_usaha: Nomor urut data usaha yang akan dihapus.

    Catatan:
    - Jika file database tidak ditemukan, mencetak pesan kesalahan.
    - Jika terjadi kesalahan lain selama proses, mencetak pesan kesalahan.
    """
    try:
        # Membaca seluruh data dari file database
        with open(Database.DB_NAME, 'r') as file:
            lines = file.readlines()

        # Mengecek apakah nomor usaha valid
        if 0 <= no_usaha - 1 < len(lines):
            # Menghapus data dengan nomor usaha yang diberikan dari daftar
            del lines[no_usaha - 1]

            # Menyimpan sisa data ke file sementara
            with open("data_temp.csv", 'w', encoding="utf-8") as temp_file:
                temp_file.writelines(lines)

            # Mengganti nama file sementara menjadi nama file database utama
            os.replace("data_temp.csv", Database.DB_NAME)
            print(f"Data dengan nomor usaha {no_usaha} berhasil dihapus.")
        else:
            print("Nomor usaha tidak valid.")

    except FileNotFoundError:
        print(f"File {Database.DB_NAME} tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


def update(no_usaha,pk,nama_usaha,kategori_usaha,alamat,telepon,email):
    """
    Fungsi ini digunakan untuk memperbarui data usaha berdasarkan nomor urut dan parameter yang diberikan.

    Parameters:
    - no_usaha: Nomor urut data usaha yang akan diperbarui.
    - pk: ID unik data usaha.
    - nama_usaha: Nama usaha baru.
    - kategori_usaha: Kategori usaha baru.
    - alamat: Alamat usaha baru.
    - telepon: Nomor telepon usaha baru.
    - email: Alamat email usaha baru.

    Catatan:
    - Fungsi menggunakan modul Database untuk mengakses template dan nama file database.
    - Jika ada kesalahan dalam proses pembacaan atau penulisan file, fungsi mencetak pesan kesalahan.
    """
    data = Database.TEMPLATE.copy()

   # Mengisi data usaha baru menggunakan parameter
    data["pk"] = pk
    data["nama_usaha"] = nama_usaha
    data["kategori_usaha"] = kategori_usaha
    data["alamat"] = alamat 
    data["telepon"] = str(telepon)
    data["email"] = email

    # Membuat string data baru
    data_str = f'{data["pk"]},{data["nama_usaha"]},{data["kategori_usaha"]},{data["alamat"]},{data["telepon"]},{data["email"]}\n'

    # Menghitung panjang data untuk menentukan posisi penulisan pada file
    data_panjang = len(data_str)

    try:
        # Membuka file database dalam mode baca dan tulis ('r+')
        with open(Database.DB_NAME, 'r+', encoding="utf-8") as file:
            # Mengarahkan posisi penulisan ke lokasi yang sesuai dengan nomor urut data
            file.seek(data_panjang * (no_usaha - 1))
            # Menulis data baru ke dalam file
            file.write(data_str)
    except Exception as e:
        print(f"Database Error: {e}")



def create(nama_usaha, kategori_usaha,alamat,telepon,email):
    """
    Fungsi ini digunakan untuk membuat data usaha baru dengan parameter yang diberikan
    dan menyimpannya ke dalam file database.

    Parameters:
    - nama_usaha: Nama usaha.
    - kategori_usaha: Kategori usaha.
    - alamat: Alamat usaha.
    - telepon: Nomor telepon usaha.
    - email: Alamat email usaha.

    Catatan:
    - Fungsi menggunakan modul Database untuk mengakses template dan nama file database.
    - Jika ada kesalahan dalam proses penyimpanan, fungsi mencetak pesan kesalahan.
    """
    data = Database.TEMPLATE.copy()
    # Menghasilkan ID unik dengan panjang 5 karakter menggunakan fungsi random_string
    data["pk"] = random_string(5)
    # Mengisi data usaha baru menggunakan parameter dan data template
    data["nama_usaha"] = nama_usaha + Database.TEMPLATE["nama_usaha"][len(nama_usaha):]
    data["kategori_usaha"] = kategori_usaha + Database.TEMPLATE["kategori_usaha"][len(kategori_usaha):]
    data["alamat"] = alamat + Database.TEMPLATE["alamat"][len(alamat):]
    data["telepon"] = telepon + Database.TEMPLATE["telepon"][len(telepon):]
    data["email"] = email + Database.TEMPLATE["email"][len(email):]
    # Menyimpan data usaha ke dalam file database
    data_str = f'{data["pk"]},{data["nama_usaha"]},{data["kategori_usaha"]},{ data["alamat"]},{ data["telepon"]},{data["email"]}\n'
    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Database Invalid")



def create_first_data():
    """
    Fungsi ini digunakan untuk membuat data usaha pertama dan menyimpannya ke dalam file database.

    Catatan:
    - Fungsi menggunakan modul Database untuk mengakses template dan nama file database.
    - Jika ada kesalahan dalam proses penyimpanan, fungsi mencetak pesan kesalahan.
    """
    nama_usaha = input("Nama Usaha: ")
    kategori_usaha = input("Kategori Usaha: ")
    alamat = input("Alamat: ")
    while True:
        try:
            telepon = input("Telepon\t: ")
            # Memastikan bahwa input merupakan angka dan dimulai dengan '08'
            if telepon.isdigit() and telepon.startswith('08'):
                telepon = str(telepon)
                break
            else:
                print("Nomor Telepon Harus Berupa Angka dan Dimulai dari '08'")
        except ValueError:
            print("Invalid Input. Pastikan Nomor Telepon Berupa Angka.")
    while True:
        email = input("Email: ")
        try:
            if validasi.is_valid_email(email):
                break
            else:
                print("Format email tidak valid. Mohon masukkan email yang benar")
        except ValueError:
            print("Format email salah. Masukkan email yang benar")

    data = Database.TEMPLATE.copy()

    # Membuat data usaha menggunakan template dan input pengguna
    data["pk"] = random_string(5)
    data["nama_usaha"] = nama_usaha + Database.TEMPLATE["nama_usaha"][len(nama_usaha):]
    data["kategori_usaha"] = kategori_usaha + Database.TEMPLATE["kategori_usaha"][len(kategori_usaha):]
    data["alamat"] = alamat + Database.TEMPLATE["alamat"][len(alamat):]
    data["telepon"] = telepon + Database.TEMPLATE["telepon"][len(telepon):]
    data["email"] = email + Database.TEMPLATE["email"][len(email):]

    # Menyimpan data usaha ke dalam file database
    data_str = f'{data["pk"]},{data["nama_usaha"]},{data["kategori_usaha"]},{ data["alamat"]},{ data["telepon"]},{data["email"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Database Invalid")



def read_data(**kwargs):
    """
Fungsi ini digunakan untuk membaca data dari file database.

Parameters:
- kwargs: Argumen kata kunci yang dapat berisi "index" untuk membaca data berdasarkan indeks.

Returns:
- Jika argumen "index" ada, fungsi mengembalikan data pada indeks tertentu.
- Jika tidak ada argumen "index", fungsi mengembalikan seluruh data.

Catatan:
- Jika terjadi kesalahan saat membaca file atau indeks diluar rentang, fungsi mengembalikan False.
"""
    try:
        with open(Database.DB_NAME,'r')as file:
            content = file.readlines()
            jumlah_usaha = len(content)

            # Jika argumen "index" ada, baca data pada indeks tertentu
            if "index" in kwargs:
                index_usaha = kwargs["index"]-1
                if index_usaha < 0 or index_usaha > jumlah_usaha:
                # Jika indeks diluar rentang, kembalikan False
                    return False
                else:
                    return (content[index_usaha])
            else: 
                # Jika tidak ada argumen "index", kembalikan seluruh data
                return content
    except:
        print("Membaca Database Error")
        return False
    
