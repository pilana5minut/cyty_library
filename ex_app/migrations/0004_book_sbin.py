# Generated by Django 5.1.2 on 2024-10-30 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex_app', '0003_book_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='sbin',
            field=models.CharField(
                default='000000000000', max_length=12, verbose_name='(SBIN) уникальный номер'),
            preserve_default=True,
        ),
    ]