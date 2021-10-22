[src1](https://qiita.com/ryomatube/items/1b36fe6d73b9a6c3468c)
[src2](https://qiita.com/ryomatube/items/1e7e7e96d5d23e5ce282)
cd nuxt/front
yarn
cd ../../django/config
python3 get_random_secretkey.py
cd ../../
docker-compose up -d --build
docker-compose run back python3 manage.py migrate
docker-compose run back python3 manage.py createsuperuser
docker-compose run back python3 manage.py collectstatic
touch nuxt/front/.env
write baseURL,browserBaseURL,topURL to .env 
