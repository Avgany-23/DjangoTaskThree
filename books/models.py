from django.db import models


class Book(models.Model):
    name = models.CharField('Название', max_length=64, null=False)
    author = models.CharField('Автор', max_length=64, null=False)
    pub_date = models.DateField('Дата публикации')

    def __str__(self):
        return self.name + " " + self.author

    class Meta:
        unique_together = [['name', 'author'], ]
