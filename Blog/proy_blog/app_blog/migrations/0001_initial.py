# Generated by Django 4.2.6 on 2023-11-22 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=64)),
                ('subtitulo', models.CharField(max_length=64)),
                ('cuerpo', models.CharField(max_length=64)),
                ('autor', models.CharField(max_length=64)),
                ('fecha', models.IntegerField()),
            ],
        ),
    ]
