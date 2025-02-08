from django.db import models

# Create your models here.
class Artista(models.Model):
    nombre_del_artista = models.CharField(max_length=150)
    pais_de_origen = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.nombre_del_artista}'
    
class Álbum(models.Model):
    titulo_del_album = models.CharField(max_length=150)
    anio_de_lanzamiento = models.DateField()
    GENEROS = {
        ('R&R','Rock & Roll'),
        ('Blu', 'Blues'),
        ('BAl', 'Baladas'),
        ('CRY', 'Country'),
        ('ELE', 'Electrónica'),
        ('POP', 'Pop'),
        ('JAZ', 'Jazz'),
        ('REG', 'Reggae'),
        ('SAL', 'Salsa'),
        ('MER', 'Merengue'),
        ('HIP', 'Hip-Hop'),
        ('RAP', 'Rap'),
        ('FOL', 'Folk'),
        ('MET', 'Metal'),
        ('PUN', 'Punk'),
        ('FUNK', 'Funk'),
        ('DIS', 'Disco'),
        ('CLA', 'Clásica'),
        ('LAT', 'Latina'),
        ('CUM', 'Cumbia'),
    }
    genero = models.CharField(max_length=150, choices=GENEROS)
    portada = models.ImageField(upload_to="p_images", blank= True, null= True)
    artista_asociado = models.ForeignKey(Artista, on_delete=models.CASCADE, db_column='id_artista')
    
    def __str__(self):
        return f'{self.titulo_del_album} - {self.artista_asociado.nombre_del_artista}'
    
    