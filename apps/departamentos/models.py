from django.db import models


class Departemento (models.Model):
    nome = models.CharField (max_length=70)

    def __str__(self):
      return self.nome
