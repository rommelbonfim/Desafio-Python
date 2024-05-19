from rest_framework import serializers
from mercado.models import Produto, Pedido,usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = usuario
        fields = ['id', 'username', 'password', 'email']

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'



class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
