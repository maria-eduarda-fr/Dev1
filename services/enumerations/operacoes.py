from django.db import models

class Operacoes(models.TextChoices):
    ADDITIONS = '+', 'Adição'
    SUBTRACTION = '-', 'Subtração'
    MULTIPLICATION = '*', 'Multiplicação'
    DIVISION = '/', 'Divisão'