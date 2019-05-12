from django.db import models
from django.utils.timezone import now

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    content = models.CharField(max_length=100, verbose_name="text")
    created_date = models.DateTimeField(default=now, editable=False, verbose_name="Дата")   
    #image = models.ImageField(verbose_name="Изображение", upload_to="news")

    def __str__(self):
        return self.title + self.content

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"