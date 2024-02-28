import random
import string

def random_string(panjang:int)->str:
    """
    Fungsi ini menghasilkan string acak dengan panjang tertentu.

    Parameters:
    - panjang: Panjang string yang ingin dihasilkan.

    Returns:
    - String acak dengan panjang sesuai parameter.

    Langkah-langkah:
    1. Menggunakan modul random dan string untuk memilih karakter acak dari
       kombinasi huruf besar, huruf kecil, dan angka sebanyak panjang yang ditentukan.
    2. Menggabungkan karakter-karakter acak tersebut menjadi satu string.
    3. Mengembalikan string acak hasil dari proses di atas.

    Catatan:
    - Fungsi ini dapat digunakan untuk menghasilkan ID unik atau string acak dalam aplikasi.
    """
    hasil_string = ''.join(random.choice(string.ascii_letters)for i in range(5))
    return hasil_string

