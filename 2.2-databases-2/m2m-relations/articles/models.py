from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=10, verbose_name="Название тега")
    scopes = models.ManyToManyField('Article', through='Scope')
    def __str__(self):
        return self.name

class Scope(models.Model):
    article= models.ForeignKey(Article, on_delete=models.DO_NOTHING,related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,related_name='tag')
    is_main = models.BooleanField()
    class Meta:
        verbose_name = 'Облако тегов'
        verbose_name_plural = 'Облако тегов'
        ordering = ['tag']