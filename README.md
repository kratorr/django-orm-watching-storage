# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны — это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

# Как установить

Запросите доступ к БД у менеджера вашего банка. Для доступа вам понадобятся хост, порт,название базы данных ,имя пользователя, пароль.
Так же, сгенерируйте длинную  строку для поля SECRET_KEY

Поместите эти данные в файл .env в директории project
Пример:
```
DB_HOST="адрес_базы_данных"
DB_PORT=порт_базы_данных
DB_NAME="имя_базы_данных"
DB_USER="имя_пользователя"
DB_PASSWORD="пароль_пользователя"
SECRET_KEY="секретный_ключ"
```

Для работы необоходим Python 3. 
Установите зависимости с помощью pip:
```bash
pip install -r requirements.txt
```
Для лучшей изоляции  рекомендуется использовать виртуальное окружение.

# Quickstart


Запуск на встроенном сервере Django
```bash
$ python3 manage.py runserver
```

После откройте в браузере страницу с веб-приложением по адресу: 
[localhost:8000](http://localhost:8000)



# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DVMN.ORG](https://dvmn.org)
