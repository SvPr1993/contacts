from django.db import models


class Employees(models.Model):
    # Имена сотрудников организации
    name = models.CharField('Имя сотрудника', max_length=21)
    surname = models.CharField('Фамилия сотрудника', max_length=21)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудники'
