# Generated by Django 3.1.7 on 2021-04-15 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stickers',
            name='cat',
            field=models.CharField(default='Прочее', max_length=255, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='stickers',
            name='img',
            field=models.ImageField(default='sticker_img/sticker1.jpg', upload_to='sticker_img', verbose_name='Картинка стикера'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
