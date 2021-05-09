from django.db import models
from PIL import Image
from django.urls import reverse
import random
import math

class stickers(models.Model):
    cat = models.CharField(verbose_name='Категория', max_length=255, default='Прочее')
    img = models.ImageField(verbose_name='Картинка стикера', default='sticker_img/sticker1.jpg', upload_to='sticker_img')
    title = models.CharField(verbose_name='Название стикерпака', max_length=100, default='placeholder')
    desc = models.TextField(verbose_name='Описание стикерпака', default='placeholder')
    price = models.IntegerField(verbose_name='Цена', default=0)
    slug = models.SlugField(verbose_name='Короткое название для ссылки', blank=True,unique=True)
    keywords = models.CharField(verbose_name='Ключевые слова', max_length=255, default='sticker')

    def __str__(self):
        return f'Стикерпак {self.title}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = "%s-%s-%s" % (self.title[:3], self.price, round(random.random(), 4))
        self.keywords = self.keywords.lower()
        super().save()

        image = Image.open(self.img.path)

        if image.height > 450 or image.width > 450:
            resize = (450, 450)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Стикер'
        verbose_name_plural = 'Стикеры'