import falcon, psycopg2, json

try:
    conn = None
    conn.autocommit = True

except:
    print('invalid db connection')


class movie_show_and_add(object):
    curr = conn.cursor()

    def on_post(self, req, res):
        curr = conn.cursor()

        data = json.loads(req.stream.read())
        for d in data['movies']:
            category = d['category']
            movie_name = d['movie_name']
            movie_path = d['movie_path']
            movie_description = d['movie_description']
            image = d['image']
            movie_type = d['movie_type']
            movie_time = d['movie_time']
            vision_date = d['vision_date']
            quality = d['quality']
            imdb_score = d['imdb']

            try:
                curr.execute("""insert into movie values (uuid_generate_v4(), %s,%s,%s,%s, %s,%s,%s,%s,%s,%s)""",
                             (category, movie_name, movie_path, movie_description, image, movie_type, movie_time,
                              vision_date, quality, imdb_score))
                print("kayıt başarılı")

            except:
                print("hatalı kayıt!")

    curr.execute("SELECT m.*, c.category_uid FROM movie AS m INNER JOIN category AS c ON m.category = c.category_name;")
    data_list = []

    for data_query in curr:
        data_dict = {
            'movies': {
                'movie_id': data_query[0],
                'movie_categories': {
                    'category_id': data_query[11],
                    'movie_category': data_query[1]
                },
                'movie_name': data_query[2],
                'movie_path': data_query[3],
                'movie_description': data_query[4],
                'movie_img': data_query[5],
                'movie_type': data_query[6],
                'movie_time': data_query[7],
                'vision_date': data_query[8],
                'quality': data_query[9],
                'imdb_score': data_query[10],
            }
        }
        data_list.append(data_dict)

    def to_json(self, body_dict):
        return json.dumps(body_dict)

    def on_get(self, req, res):
        if req.path == '/data':
            res.status = falcon.HTTP_200
            res.body = self.to_json(self.data_list)
        else:
            raise print("hata")


class category_show(object):
    cur = conn.cursor()

    cur.execute("SELECT * FROM category;")
    data_list = []

    for data_query in cur:
        data_dict = {
            'categories': {
                'category_id': data_query[0],
                'category_name': data_query[1],
            }
        }
        data_list.append(data_dict)

    def to_json(self, body_dict):
        return json.dumps(body_dict)

    def on_get(self, req, res):
        if req.path == '/category':
            res.status = falcon.HTTP_200
            res.body = self.to_json(self.data_list)
        else:
            raise print("hata")


class movie_show(object):
    curr = conn.cursor()
    data_list = []

    def on_post(self, req, res):
        curr = conn.cursor()
        data = []
        data.append(json.loads(req.stream.read()))
        for d in data:
            uid = d['uid']
            try:
                # curr.execute("SELECT * FROM movie LIMIT 1;")
                curr.execute("SELECT * FROM movie WHERE uid = %(uid)s",
                               {"uid": uid})
                # curr.fetchall()
                for data_query in curr:
                    print(data_query)
                    data_dict = {
                        'movies': {
                            'movie_id': data_query[0],
                            'movie_category': data_query[1],
                            'movie_name': data_query[2],
                            'movie_path': data_query[3],
                            'movie_description': data_query[4],
                            'movie_img': data_query[5],
                            'movie_type': data_query[6],
                            'movie_time': data_query[7],
                            'vision_date': data_query[8],
                            'quality': data_query[9],
                            'imdb_score': data_query[10],
                        }
                    }
                    self.data_list.append(data_dict)
                    print(self.data_list)

            except:
                print("hata")

    def to_json(self, body_dict):
        return json.dumps(body_dict)

    def on_get(self, req, res):
        if req.path == '/movie':
            res.status = falcon.HTTP_200
            res.body = self.to_json(self.data_list)
        else:
            raise print("hata")


api = falcon.API()
api.add_route('/data', movie_show_and_add())
api.add_route('/category', category_show())
api.add_route('/movie', movie_show())
