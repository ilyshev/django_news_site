from django.db import models


class News(models.Model):
    title = models.CharField(max_length=128, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Содержимое')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-create_at']


class Category(models.Model):
    title = models.CharField(max_length=128, db_index=True, verbose_name='Наименование')

    def __str__(self): # за счет этого видим отображение названий категорий на странице, а не category_1, etc..
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']