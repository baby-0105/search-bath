# お風呂検索アプリ

* Vue 立ち上げ

```
$ docker-compose exec vue bash yarn serve
```

* tailwind.css の　buildプロセス開始

```
vueコンテナ内で実行
$ npx tailwindcss -i ./src/tailwind-input.css -o ./public/tailwind.css --watch
```
