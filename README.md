# Wine-Site

Этот проект представляет коллекцию вин с красивой визуальной презентацией. Он позволяет пользователям просматривать вина по категориям, узнавать об их особенностях и цене, а также получать информацию о каждом вине.

## Описание

Проект "Wine-Site" - это веб-приложение, которое отображает каталог вин с детальной информацией о каждом из них. Приложение автоматически получает данные из файла Excel и визуализирует их с помощью Jinja2 для представления в виде удобного и красивого веб-интерфейса. Оно позволяет пользователям изучать ассортимент вин, категории и ценовые предложения, а также получать дополнительную информацию о каждом продукте.

## Установка

```bash
# Клонируйте репозиторий
$ git clone https://github.com/MaksimObozniy/Wine-Site.git

# Перейдите в директорию проекта
$ cd Wine-Site

#Создайте виртуальное окружение
$ python -m venv .venv

#Активируйте виртуальное окружение
$ .venv\Scripts\activate

# Установите зависимости
$ pip install -r requirements.txt
```

## Использование

Для запуска проекта необходимо убедиться, что все зависимости установлены, а также файл c информацией о винах находится в корневой папке проекта. Так же при запуске нужно указать путь к файлу и название листа в котором хранится информация (По умолчанию : Лист1).
После этого можно запустить сервер, чтобы приложение было доступно по локальному адресу.

```bash

#Запустите сайт
python main.py
```
После запуска файла, убедитесь что у вас появился файл index.html. После, откройте браузер и перейдите по адресу (http://127.0.0.1:8000/index.html), чтобы просмотреть коллекцию вин.

## Особенности

- Автоматическая генерация каталога вин из Excel файла.
- Красивый и удобный интерфейс для просмотра коллекции.
- Возможность добавлять и группировать вина по категориям.
- Совместимость с Jinja2 для гибкой настройки шаблонов.
