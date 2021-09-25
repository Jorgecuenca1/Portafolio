from django.db import models

# Create your models here.
class Category(models.Model):
    image = models.ImageField(verbose_name='Imagen de la categoria', upload_to='images/category/')
    name = models.CharField(max_length=180, verbose_name='Categoría', blank=True, null=True, default="name")


    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)

class Place(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    latitude = models.FloatField(verbose_name='Latitud')
    longitude = models.FloatField(verbose_name='Longitud')

    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'

    def save(self, *args, **kwargs):
        super(Place, self).save(*args, **kwargs)

    def __str__(self):
        return '({},{})'.format(self.latitude, self.longitude)

class Plant(models.Model):
    image = models.ImageField(verbose_name='Imagen de la planta', upload_to='images/plants/')
    name = models.CharField(max_length=180, verbose_name='Nombre comun', blank=True, null=True, default="name")
    scientific_name = models.CharField(max_length=180, verbose_name='Nombre cientifico', blank=True, null=True, default="name scientific")
    description = models.TextField( verbose_name='Descripción', blank=True, null=True, default="description")
    category = models.ForeignKey(Category, verbose_name='Categoria', blank=True, null=True, default="Category", on_delete = models.CASCADE)
    place = models.ManyToManyField(Place, verbose_name='Lugar')


    class Meta:
        verbose_name = 'Planta'
        verbose_name_plural = 'PLanta'

    def save(self, *args, **kwargs):
        super(Plant, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)