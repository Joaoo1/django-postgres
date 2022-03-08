import uuid
from django.db import models
from stdimage.models import StdImageField


def format_file_name(_instance, filename):
    return f'{uuid.uuid4()}{filename}'


class Base(models.Model):
    createdAt = models.DateField('Data criação', auto_now_add=True)
    updatedAt = models.DateField('Data atualização', auto_now_add=True)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Service(Base):
    icon = models.CharField('Icone', max_length=30)
    service = models.CharField('Serviço', max_length=100)
    description = models.CharField('Descrição', max_length=200)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.service


class Role(Base):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.name


class Employee(Base):
    name = models.CharField(max_length=255)
    role = models.ForeignKey(
        'core.Role', max_length=200, on_delete=models.CASCADE)
    biography = models.TextField(max_length=400)
    facebook = models.CharField(max_length=255, default='#')
    twitter = models.CharField(max_length=255, default='#')
    instagram = models.CharField(max_length=255, default='#')
    image = StdImageField('Imagem', upload_to=format_file_name, variations={
                          'thumb': {'width': 480, 'height': 480, 'crop': True}})

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.name


class Feature(Base):
    name = models.CharField(max_length=100)
    icon = models.CharField('Icone', max_length=30)
    description = models.CharField('Descrição', max_length=200)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.name
