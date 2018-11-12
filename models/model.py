import psycopg2

conn = None


class table_drop_and_create(object):
    cur = conn.cursor()
    try:
        cur.execute("DROP TABLE movie;")
        print("tablo silindi!!!")
    except:
        print("tablo silinemedi!!")

    try:

        cur.execute(
            "CREATE TABLE movie"
            "("
                "uid               UUID PRIMARY KEY,"
                "category          VARCHAR,"
                "movie_name        VARCHAR(50),"
                "movie_path        TEXT,"
                "movie_description TEXT,"
                "movie_img         TEXT,"
                "movie_type        VARCHAR(50),"
                "movie_time        VARCHAR(50),"
                "vision_date       VARCHAR(50),"
                "quality           VARCHAR(50),"
                "imdb_score        FLOAT"
            ");"
        )

        print('tablo başarı ile oluşturuldu!')
    except:
        print("hata")

    conn.commit()
    conn.close()
    cur.close()