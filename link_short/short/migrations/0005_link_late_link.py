# Generated by Django 4.1.6 on 2023-02-16 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0004_remove_link_late_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='late_link',
            field=models.CharField(default='https://clck.ru/9zuXm', max_length=30, verbose_name='Сокращенная ссылка'),
        ),
    ]
