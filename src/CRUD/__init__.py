# Import modul init_console dari file Database dalam package yang sama
from .Database import init_console

# Import fungsi-fungsi readmenu_console, create_console, update_console, delete_console
# dari file Fungsi dalam package yang sama
from .Fungsi import readmenu_console, create_console, update_console, delete_console
"""
Catatan:
- Notasi titik (.) sebelum nama modul menunjukkan bahwa file tersebut berada dalam
  package (package yang sama dengan file yang berisi kode di atas).
- Penggunaan inisialisasi konsol (init_console) bertujuan untuk mempersiapkan atau
  membuka koneksi ke database sebelum menjalankan operasi CRUD (Create, Read, Update, Delete).
- Fungsi-fungsi seperti readmenu_console, create_console, update_console, dan delete_console
  diimpor untuk digunakan dalam pengembangan aplikasi konsol tersebut.
"""