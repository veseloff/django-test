### Собираем образ
```
docker build -t djangodemo .
```

### Ну и запускаем
docker run --env-file someenvfile --restart always --name djangodemo -p 80:80 -p 8000:8000 -tid djangodemo:latest