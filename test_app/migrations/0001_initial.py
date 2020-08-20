# Generated by Django 2.2.2 on 2020-08-19 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название книги')),
                ('author_name', models.CharField(max_length=50, verbose_name='автор книги')),
                ('description', models.TextField(verbose_name='Описание книги')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['-id'],
            },
        ),
    ]