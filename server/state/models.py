from django.db import models

# Create your models here.
class State(models.Model):
    """
    Модель для сохранения данных игры
    """

    tg_name = models.SlugField()
    data = models.JSONField(default=None, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    updated = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    class Meta:
        indexes = [models.Index(fields=['-tg_name', 'created'])]
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

    def __str__(self):
        return self.tg_name