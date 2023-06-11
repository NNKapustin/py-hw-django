from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    text = models.TextField()
    image = models.ImageField(null=True, blank=True,
                              upload_to='posts/images/')  # upload_to указывает на путь в корневой папке media
    # image = models.FileField(null=True, blank=True) # любой файл. В ImageField есть проверка на картинку
    # при работе с файлами в settings нужно указать MEDIA_URL = "/media/" и MEDIA_ROOT = BASE_DIR / "media"
    # после этого папка media создастся при первом запуске
    # STATIC_URL = "/static/" и STATIC_ROOT = BASE_DIR / "static" по умолчанию тоже лучше указывать так
    # это меняет путь на статический, что лучше обрабатывается
    # static - это часть сайта, media - это файлы образующиеся при работе сайта
    # для работы с изображениями так же нужно установить pip install pillow
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posts')
    favorite_by = models.ManyToManyField(User,
                                         related_name='favorite_posts')  # для возможности добавления в избранное
    created_at = models.DateTimeField(auto_now_add=True)
