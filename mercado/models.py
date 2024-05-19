from django.db import models
from django.contrib.auth.models import  AbstractUser


class usuario(AbstractUser):
    email = models.EmailField(unique=True)

class Produto(models.Model):
    nome = models.CharField(max_length=30)
    preco = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.nome


class Pedido(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)



    def __str__(self):
     return f"Pedido #{self.id} - Usuario: {self.usuario.username}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens_pedido')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)