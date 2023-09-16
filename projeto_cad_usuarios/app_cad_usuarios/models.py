from django.db import models


# Create your models here.   
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=3)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=13)
    data_cadastro = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Usuario'

    def __str__(self):
        return self.nome    
    
    def get_data_cadastro(self):
        return self.data_cadastro.strftime('%d/%m/%Y as %H:%M hs')