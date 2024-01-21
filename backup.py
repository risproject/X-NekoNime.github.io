from flask import Flask, request, jsonify, render_template, redirect, url_for
import pymysql

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = pymysql.connect(
            host='sql12.freesqldatabase.com',
            database='sql12678341',
            user='sql12678341',
            password='gvErt5PTka',
            cursorclass=pymysql.cursors.DictCursor,
        )
    except pymysql.Error as e:
        print(e)
    return conn

@app.route("/Statistik_Anime", methods=["GET", "POST", "PUT", "DELETE"])
def Anime():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute("SELECT * FROM Statistik_Anime")
        Statistik_Anime = [
            dict(
                id_anime=row["id_anime"],
                judul=row["judul"],
                genre=row["genre"],
                jumlah_episode=row["jumlah_episode"],
                rating=row["rating"]
            )
            for row in cursor.fetchall()
        ]
        if Statistik_Anime:
            return jsonify(Statistik_Anime)

    elif request.method == "POST":
        add_judul = request.form["judul"]
        add_genre = request.form["genre"]
        add_jumlah_episode = request.form["jumlah_episode"]
        add_rating = request.form["rating"]
        
        query_insert = """INSERT INTO Statistik_Anime (
            judul, genre, jumlah_episode, rating
        ) VALUES (%s, %s, %s, %s)"""
        
        cursor.execute(query_insert, (add_judul, add_genre, add_jumlah_episode, add_rating))
        conn.commit()
        return "Data Berhasil Ditambahkan"

    elif request.method == "PUT":
        update_id_anime = request.form["id_anime"]
        update_judul = request.form["judul"]
        update_genre = request.form["genre"]
        update_jumlah_episode = request.form["jumlah_episode"]
        update_rating = request.form["rating"]

        query_update = """UPDATE Statistik_Anime SET
            judul=%s, genre=%s, jumlah_episode=%s, rating=%s
            WHERE id_anime=%s"""

        cursor.execute(query_update, (update_judul, update_genre, update_jumlah_episode, update_rating, update_id_anime))
        conn.commit()
        return "Data Berhasil Diperbarui"

    elif request.method == "DELETE":
        id_anime = request.form['id_anime']
        query_delete = """DELETE FROM Statistik_Anime WHERE id_anime=%s"""  
        cursor.execute(query_delete, (id_anime,))
        conn.commit()
        return "Data Berhasil Dihapus"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/admin')
def admin():
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Statistik_Anime")
    statistik_anime = [
        dict(
            id_anime=row["id_anime"],
            judul=row["judul"],
            genre=row["genre"],
            jumlah_episode=row["jumlah_episode"],
            rating=row["rating"]
        )
        for row in cursor.fetchall()
    ]

    return render_template('admin.html', statistik_anime=statistik_anime)


if __name__ == "__main__":
    app.run()