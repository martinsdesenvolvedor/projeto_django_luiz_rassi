from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def validacao_max_digits(value):
    max_digits = 3
    if value <0 or value >= 10**max_digits:
        raise ValidationError('Idade Inválida, tente novamente com um número positivo e com no maximo 3 digitos!')
    
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField(help_text='Informe a idade com no máximo 3 digitos.', validators=[validacao_max_digits])
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=13)
    data_cadastro = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Usuario'

    def __str__(self):
        return self.nome    
    
    def get_data_cadastro(self):
        return self.data_cadastro.strftime('%d/%m/%Y as %H:%M hs')