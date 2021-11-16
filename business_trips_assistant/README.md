1. Применить команду **pip install -r requirements.txt** для установления зависимостей


2. Установить субд **postgres**


3. В субд создать базу данных


4. Создать файл .env прописать в нём переменные окружения
   
   
    - CHROMEDRIVER - путь до chromedriver.exe 
    - PASSWORD_DATA_BASE - пароль от базы данных
    - NAME_DATA_BASE - название базы данных
    - USER_DATA_BASE - имя пользователя базы данных
    - HOST_DATA_BASE - host базы данных
    - PORT_DATA_BASE - порт базы данных 


5. Применить фиксутры c помощью команд:
    - python manage.py loaddata city.json
    - python manage.py loaddata station.json