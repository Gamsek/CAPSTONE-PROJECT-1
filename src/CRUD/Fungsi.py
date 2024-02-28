from . import OperasiYP
from tabulate import tabulate
from . import validasi

def delete_console():
    """
    Fungsi ini digunakan untuk menghapus data usaha dari konsol dengan prosedur sebagai berikut:

    Catatan:
    - Fungsi ini memanfaatkan fungsi-fungsi dari OperasiYP seperti read_data, delete, dan sebagainya.
    - Penggunaan loop while untuk memastikan validitas input dan konfirmasi.
    """
    while True :
        print("Menu Delete Data:")
        print("1. Delete Data Usaha")
        print("2. Menu Utama")
        try:
            user_pilihan = int(input("Masukkan Pilihan (1/2): "))
            if user_pilihan == 1:
                print("Menampilkan Data")
                # Menampilkan data usaha sebelum penghapusan
                read_console()

                while True:
                    print("Silahkan Pilih Nomor Usaha yang akan Dihapus")
                    no_usaha = int(input("Nomor Usaha: "))
                    
                    # Membaca data usaha berdasarkan nomor urut yang dimasukkan
                    data_usaha = OperasiYP.read_data(index=no_usaha)

                    if data_usaha:
                        # Membagi data usaha menjadi elemen-elemen terpisah
                        data_break = data_usaha.split(",")
                        pk = data_break[0]
                        nama_usaha = data_break[1]
                        kategori_usaha = data_break[2]
                        alamat = data_break[3]
                        telepon = data_break[4]
                        email = data_break[5][:-1]

                        # Menampilkan data usaha yang akan dihapus
                        print("\n" + "=" * 100)
                        print("Data yang akan Anda Hapus")
                        print(f"1. Nama Usaha\t: {nama_usaha:.40}")
                        print(f"2. Kategori Usaha\t: {kategori_usaha:.40}")
                        print(f"3. Alamat\t: {alamat:.40}")
                        print(f"4. Telepon\t: {telepon:.40}")
                        print(f"5. Email\t: {email:.40}")

                        # Meminta konfirmasi untuk penghapusan
                        is_done = input("Apakah Yakin Anda Hapus Data Tersebut (y/t)? ")
                        
                        if is_done == "y" or is_done == "Y":
                            # Memanggil fungsi delete untuk menghapus data usaha
                            OperasiYP.delete(no_usaha)
                            break
                    else:
                        print("Nomor tidak valid, silahkan masukkan lagi")

                print("Data Sukses Dihapus")
                print("=========================================")
            elif user_pilihan == 2:
                break # Kembali Ke Menu Utama 
            else:
                print("=================================================")
                print("Inputan Invalid. Silahkan Masukkan Angka 1 atau 2")    
                print("=================================================")
        except:
            print("=========================================")
            print("Input Invalid. Masukkan Input Dalam Angka")
            print("=========================================")

    
def update_console():
    """
    Fungsi ini digunakan untuk memperbarui data usaha dari konsol dengan prosedur sebagai berikut:

    Catatan:
    - Fungsi ini memanfaatkan fungsi-fungsi dari OperasiYP seperti read_data, update, dll.
    - Penggunaan loop while untuk memastikan validitas input dan konfirmasi.
    """
    #Menampilkan Sub menu untuk create data 
    while True:
        print("Menu Update Data:")
        print("1. Update Data Usaha")
        print("2. Menu Utama")
        try: 
            user_pilihan = int(input("Masukkan Pilihan (1/2): "))
            print("=========================================")
            if user_pilihan == 1:
                print("Menampilkan Data")
                # Menampilkan data usaha sebelum pembaruan
                read_console()

                while True:
                    print("Silahkan Pilih Nomor Usaha yang akan Diupdate")
                    no_usaha = int(input("Nomor Usaha: "))
                    
                    # Membaca data usaha berdasarkan nomor urut yang dimasukkan
                    data_usaha = OperasiYP.read_data(index=no_usaha)

                    if data_usaha:
                        break
                    else:
                        print("Nomor tidak valid, silahkan masukkan lagi")

                # Membagi data usaha menjadi elemen-elemen terpisah
                data_break = data_usaha.split(",")
                pk = data_break[0]
                nama_usaha = data_break[1]
                kategori_usaha = data_break[2]
                alamat = data_break[3]
                telepon = data_break[4]
                email = data_break[5][:-1]

                while True:
                    # Menampilkan data usaha yang akan diupdate
                    print("\n" + "=" * 100)
                    print("Silahkan pilih data yang akan diubah")
                    print(f"1. Nama Usaha\t: {nama_usaha:.40}")
                    print(f"2. Kategori Usaha\t: {kategori_usaha:.40}")
                    print(f"3. Alamat\t: {alamat:.40}")
                    print(f"4. Telepon\t: {telepon:.40}")
                    print(f"5. Email\t: {email:.40}")

                    # Memilih mode yang akan diupdate
                    user_pilihan = input("Pilih Data [1-5]: ")
                    print("\n" + "=" * 100)

                    match user_pilihan:
                        case "1": nama_usaha = input("Nama Usaha\t: ")
                        case "2": kategori_usaha = input("Kategori Usaha\t: ")
                        case "3": 
                            while (True):
                                try: 
                                    alamat = input("Alamat\t\t: ")
                                    if alamat.startswith('Jl.'):
                                        alamat = str(alamat)
                                        break
                                    else:
                                        print("Alamat Harus Dimulai Dengan Kata 'Jl.'")
                                except:
                                    print("Invalid Input. Pastikan Alamat Berupa Kata.")
                        case "4": 
                            while True:
                                try:
                                    telepon = input("Telepon\t\t: ")
                                    # Memastikan bahwa input merupakan angka dan dimulai dengan '08'
                                    if telepon.isdigit() and telepon.startswith('08'):
                                        telepon = str(telepon)
                                        break
                                    else:
                                        print("Nomor Telepon Harus Berupa Angka dan Dimulai dari '08'")
                                except ValueError:
                                    print("Invalid Input. Pastikan Nomor Telepon Berupa Angka.")
                        case "5": 
                            while True:
                                email = input("Email\t\t: ")
                                try:
                                    if validasi.is_valid_email(email):
                                        break
                                    else:
                                        print("Format email tidak valid. Mohon masukkan email yang benar")
                                except ValueError:
                                    print("Format email salah. Masukkan email yang benar")

                        case _: print("Index tidak sesuai")
                    
                    # Menampilkan data usaha yang baru setelah pembaruan
                    print("\n" + "=" * 100)
                    print("Data Baru Yang Sudah Diubah")
                    print(f"1. Nama Usaha\t: {nama_usaha:.40}")
                    print(f"2. Kategori Usaha\t: {kategori_usaha:.40}")
                    print(f"3. Alamat\t: {alamat:.40}")
                    print(f"4. Telepon\t: {telepon:.40}")
                    print(f"5. Email\t: {email:.40}")

                    # Meminta konfirmasi pengguna apakah data yang baru sudah sesuai
                    is_done = input("Apakah data sudah sesuai (y/t)? ")
                    if is_done == "y" or is_done == "Y":
                        break

            elif user_pilihan == 2:
                break
                #kembali ke menu utama 
            else:
                print("================================================")
                print("Inputan Invalid. Silahkan Masukkan Opsi 1 atau 2")    
                print("================================================")
        except:
            print("=========================================")
            print("Input Invalid. Masukkan Input Dalam Angka")
            print("=========================================")


def create_console():
    """
    Fungsi ini digunakan untuk menambahkan data usaha baru ke konsol dengan prosedur sebagai berikut:

    Catatan:
    - Fungsi ini memanfaatkan fungsi-fungsi dari OperasiYP seperti create dan read_console.
    - Menggunakan loop while untuk memastikan validitas input nomor telepon.
    """
    #Menampilkan Sub menu untuk create data 
    while True:
        print("Menu Create Data:")
        print("1. Buat Data Usaha Baru")
        print("2. Menu Utama")
        try:
            user_pilihan = int(input("Masukkan Pilihan (1/2)"))
            if user_pilihan == 1:
                print("Silahkan Tambahkan Data Usaha Anda")

                # Meminta input dari pengguna untuk data usaha baru
                nama_usaha = input("Nama Usaha\t: ")
                kategori_usaha = input("Kategori Usaha\t: ")
                while True:
                    try: 
                        alamat = input("Alamat\t: ")
                        if alamat.startswith('Jl.'):
                                        alamat = str(alamat)
                                        break
                        else:
                            print("Alamat Harus Dimulai Dengan Kata 'Jl.'")
                    except:
                            print("Invalid Input. Pastikan Alamat Berupa Kata.")

                while True:
                    try:
                        # Memastikan bahwa input telepon merupakan angka dan dimulai dengan '08'
                        telepon = input("Telepon\t: ")
                        if telepon.isdigit() and telepon.startswith('08'):
                            telepon = str(telepon)
                            break
                        else:
                            print("Nomor Telepon Harus Berupa Angka dan Dimulai dari '08'")
                    except ValueError:
                        print("Invalid Input. Pastikan Nomor Telepon Berupa Angka.")
                while True:
                    email = input("Email\t: ")
                    try:
                        if validasi.is_valid_email(email):
                            break
                        else:
                            print("Format email tidak valid. Mohon masukkan email yang benar")
                    except ValueError:
                        print("Format email salah. Masukkan email yang benar")
                

                # Memanggil fungsi create dari OperasiYP untuk menambahkan data baru
                OperasiYP.create(nama_usaha, kategori_usaha, alamat, telepon, email)
                while True:
                    # Menampilkan data usaha yang baru 
                    print("\n" + "=" * 100)
                    print("Data Baru Yang Sudah Diubah")
                    print(f"1. Nama Usaha\t: {nama_usaha:.40}")
                    print(f"2. Kategori Usaha\t: {kategori_usaha:.40}")
                    print(f"3. Alamat\t: {alamat:.40}")
                    print(f"4. Telepon\t: {telepon:.40}")
                    print(f"5. Email\t: {email:.40}")

                    # Meminta konfirmasi pengguna apakah data yang baru sudah sesuai
                    is_done = input("Apakah data sudah sesuai (y/t)? ")
                    if is_done == "y" or is_done == "Y":
                        break

                # Menampilkan data baru yang telah ditambahkan
                print("\nBerikut Data Baru Anda")
                read_console()
                print("=========================================")
            elif user_pilihan == 2:
                # Kembali ke menu utama 
                break 
            else: 
                print("=================================================")
                print("Inputan Invalid. Silahkan Masukkan Angka 1 atau 2")
                print("=================================================")
        except:
            print("=========================================")
            print("Input Invalid. Masukkan Input Dalam Angka")
            print("=========================================")

def read_console():
    # Membaca data dari file menggunakan fungsi read_data() dari OperasiYP
    data_file = OperasiYP.read_data()

    # Menentukan header untuk tabel
    headers = ["No", "ID Usaha", "Nama Usaha", "Kategori Usaha", "Alamat", "Telepon", "Email"]

    # Mengonversi data string menjadi list of lists (data_table) untuk kemudian ditampilkan dalam tabel
    data_table = []
    for index, data_break in enumerate(data_file):
        try:
            pk, nama_usaha, kategori_usaha, alamat, telepon, email = map(str.strip, data_break.split(","))
            # Menambahkan setiap baris data ke data_table sebagai list
            data_table.append([index+1, pk, nama_usaha, kategori_usaha, alamat, telepon, email])
        except ValueError:
            print(f"Error: Format tidak sesuai pada Database ({index+1}).")
            # Tambahan penanganan kesalahan atau langkah lainnya sesuai kebutuhan

    # Menampilkan data dalam tabel menggunakan tabulate dengan tipe pretty
    print(tabulate(data_table, headers=headers, tablefmt='pretty'))

    # Menampilkan footer tabel
    print("=" * 100 + "\n")


def readmenu_console():
    """
    Fungsi ini digunakan untuk menampilkan menu konsol dengan beberapa opsi untuk membaca data usaha:

    Opsi Menu:
    1. Tampilkan Semua: Menampilkan seluruh data usaha dalam bentuk tabel.
    2. Pilih Berdasarkan ID Usaha: Meminta input ID Usaha dari pengguna dan menampilkan data sesuai ID.
    3. Pilih Berdasarkan Kategori Usaha: Meminta input Kategori Usaha dari pengguna dan menampilkan data sesuai kategori.
    4. Menu Utama: Keluar dari menu dan kembali ke menu utama.

    Catatan:
    - Fungsi ini menggunakan tabulate untuk menampilkan data dalam bentuk tabel.
    - Memanfaatkan fungsi read_data() dari OperasiYP untuk mendapatkan data usaha.
    """
    while True:
        # Menampilkan menu
        print("Menu Read Data:")
        print("1. Tampilkan Semua")
        print("2. Pilih Berdasarkan ID Usaha")
        print("3. Pilih Berdasarkan Kategori Usaha")
        print("4. Menu Utama")
    
        # Menerima input pilihan dari pengguna (dalam bentuk angka)
        user_choice = int(input("Masukkan pilihan (1-4): "))
        print("=========================================")
        data_file = OperasiYP.read_data()
        headers = ["ID Usaha", "Nama Usaha", "Kategori Usaha", "Alamat", "Telepon", "Email"]
        if user_choice == 1:
            # Menampilkan seluruh data usaha dalam bentuk tabel
            data_table = []

            for index, data_break in enumerate(data_file):
                try:
                    pk, nama_usaha, kategori_usaha, alamat, telepon, email = map(str.strip, data_break.split(","))
                    data_table.append([index+1, pk, nama_usaha, kategori_usaha, alamat, telepon, email])
                except ValueError:
                    print(f"Error: Format tidak sesuai pada Database ({index+1}).")

            print(tabulate(data_table, headers=headers, tablefmt='pretty'))
            print("=" * 100 + "\n")

        elif user_choice == 2:
            read_console()
            # Meminta input ID Usaha dan menampilkan data sesuai ID
            id_usaha_input = input("Masukkan ID Usaha yang ingin ditampilkan: ")
            filtered_data = []
            id_found = False
            for pk in (data_file):
                item = pk.split(',')
                if id_usaha_input == item[0]:
                    filtered_data.append(item)
                    id_found = True
                    print(tabulate(filtered_data, headers=headers, tablefmt='pretty'))
                    break
            if not id_found:
                print('Tidak ada id di dalam tabel')
            #filtered_data = [pk for pk in data_file if id_usaha_input in pk]

        elif user_choice == 3:
            # Meminta input Kategori Usaha dan menampilkan data sesuai kategori
            read_console()
            kategori_input = str(input("Masukkan Kategori Usaha yang ingin ditampilkan: "))
            filtered_data = []
            kategori_found = False
            for pk in data_file:
                item = pk.split(',')
                if kategori_input.lower() in item[2].lower():
                    filtered_data.append(item)
                    kategori_found = True 
                    print(tabulate(filtered_data, headers=headers, tablefmt='pretty'))
            if not kategori_found:
                print('Tidak ada kategori di dalam tabel')

        elif user_choice == 4:
            # Keluar dari menu dan kembali ke menu utama
            break

        else:
            # Menampilkan pesan kesalahan jika pilihan tidak valid
            print("====================================")
            print("Pilihan invalid. Masukkan angka 1-4.")
            print("====================================")
        