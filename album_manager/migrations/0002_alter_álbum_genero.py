# Generated by Django 4.2 on 2025-02-08 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='álbum',
            name='genero',
            field=models.CharField(choices=[('PUN', 'Punk'), ('MET', 'Metal'), ('Blu', 'Blues'), ('DIS', 'Disco'), ('R&R', 'Rock & Roll'), ('LAT', 'Latina'), ('MER', 'Merengue'), ('JAZ', 'Jazz'), ('FOL', 'Folk'), ('CUM', 'Cumbia'), ('FUNK', 'Funk'), ('HIP', 'Hip-Hop'), ('BAl', 'Baladas'), ('CLA', 'Clásica'), ('REG', 'Reggae'), ('RAP', 'Rap'), ('POP', 'Pop'), ('ELE', 'Electrónica'), ('CRY', 'Country'), ('SAL', 'Salsa')], max_length=150),
        ),
    ]
