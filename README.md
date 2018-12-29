# falcon-movie-api
falcon ile postgresql kullanarak api dağıtma servisi hazırladım.


Projeyi klonladıktan sonra öncelikle 
requirements.txt dosyasını aşşağıdaki komut ile yüklemelisiniz

``` pip install -r requirements.txt ```

Sonrasında ise Model ve MovieList dosyasında bulunan veritabanı bağlantısını oluşturduğumuz yeri kendi 
veritabanı bilgileriniz ile oluşturmalısınız.

# Örnek :
``` conn = psycopg2.connect(host="localhost",database="suppliers", user="postgres", password="postgres")```

# Son olarak ise aşşağıdaki komut ile projeyi çalıştırabilirsiniz

``` gunicorn MovieList:api ```