import pymysql

# Koneksi ke database
conn = pymysql.connect(
    host='sql12.freesqldatabase.com',
    database='sql12678341',
    user='sql12678341',
    password='gvErt5PTka',
    cursorclass=pymysql.cursors.DictCursor,
)

# Inisialisasi kursor
cursor = conn.cursor()

# Definisikan skema tabel untuk data anime
sql_query = """CREATE TABLE Statistik_Anime (
    id_anime INT AUTO_INCREMENT PRIMARY KEY,
    thumbnail TEXT NOT NULL,
    judul TEXT NOT NULL,
    genre TEXT NOT NULL,
    jumlah_episode INT NOT NULL,
    rating DECIMAL(3, 2) NOT NULL
)
"""

# Eksekusi perintah SQL untuk membuat tabel
cursor.execute(sql_query)

# Tutup koneksi
conn.close()