import re

def is_valid_email(email):
    # Definisikan pola ekspresi reguler untuk validasi email
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    
    # Lakukan pencocokan pola terhadap email yang diberikan
    match = email_pattern.match(email)
    
    # Kembalikan True jika email valid, False jika tidak
    return bool(match)
