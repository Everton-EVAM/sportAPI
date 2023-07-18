from django.db import models

class BettingShop(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=50, null=False, blank=False)
    region = models.CharField(verbose_name='Região', max_length=50, null=False, blank=False)
    url = models.CharField(verbose_name='URL', max_length=50, null=False, blank=False)