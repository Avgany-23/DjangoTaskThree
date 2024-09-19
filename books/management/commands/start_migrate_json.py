import phones.management.commands.django_settings
from django_project import settings
import django
import json
import os
from books.models import Book


def start_migrate_json(path: str = None):
    """Переносит данные с json файла"""
    path = path if path is not None else os.path.join('fixtures', 'books.json')
    if not os.path.exists(path):
        print(f'Файл {path} не нашёлся, миграция не произошла')
        return

    print('Миграция началась')
    with open(settings.BASE_DIR / path, encoding='utf-8') as f:
        reader = json.load(f)
        for row in reader:
            row = row['fields']
            try:
                Book(name=row['name'],
                     author=row['author'],
                     pub_date=row['pub_date']).save()
            except django.db.utils.IntegrityError:
                print('Запись с автором %s и его книгой  %s уже существует' % (row['author'], row['name']))
            else:
                print('Запись %s %s добавлена' % (row['author'], row['name']))
    print('Миграция закончилась')
