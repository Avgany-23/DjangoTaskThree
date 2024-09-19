import django

import phones.management.commands.django_settings
from django_project import settings
import csv
import requests
import re
import os
from phones.models import Phone


def create_media_photo(url: str) -> str:
    """Сохраняет фотографию и возвращает её имя"""

    name_re = re.search(r'\/\w*\.(png|jpg|webp|jpeg|gif)', url)
    name_photo = url[name_re.start() + 1: name_re.end()]

    response = requests.get(url)
    with open(settings.BASE_DIR / f'media/phones/{name_photo}', 'wb') as ph:
        ph.write(response.content)

    return name_photo


def start_migrate_csv(path: str = None):
    """Переносит данные с csv файла"""
    path = path if path is not None else 'phones.csv'
    if not os.path.exists(path):
        print(f'Файл {path} не нашёлся, миграция не произошла')
        return

    print('Миграция началась')
    with open(settings.BASE_DIR / path, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader:
            name_photo = create_media_photo(row[2])     # Сохранение фото в media/phones
            try:
                Phone(name=row[1],
                      price=row[3],
                      image=os.path.join('phones', name_photo),
                      release_data=row[4],
                      lte_exists=row[5]).save()
            except django.db.utils.IntegrityError:
                print('Запись с именем %s и ценой %s уже существует' % (row[1], row[3]))
            else:
                print('Запись %s добавлена' % (row[1]))
    print('Миграция закончилась')
