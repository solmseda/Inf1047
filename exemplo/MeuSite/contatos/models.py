from django.db import models

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, help_text='Entre com o nome')
    idade = models.IntegerField(help_text='Entre com a idade')
    salario = models.DecimalField(help_text='Entre com o salario', decimal_places=2, max_digits=8)
    email = models.EmailField(help_text='Entre com o email', max_length=24)
    telefone = models.CharField('Entre com o DDD e DDI', max_length=20)
    dtNasc = models.DateField(help_text="Nascimento com o formato DD/MM/AAAA", verbose_name='Data de Nascimento')

    def __str__(self):
        return self.nome