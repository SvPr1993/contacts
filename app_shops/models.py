from django.db import models

class Shops(models.Model):
    # Названия организаций
    brand = models.CharField('Название магазина', max_length=21)
    name = models.CharField('Имя сотрудника', max_length=21)
    surname = models.CharField('Фамилия сотрудника', max_length=21)

    def __str__(self):
        return f'{self.brand} - {self.name} {self.surname}'

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организация'
