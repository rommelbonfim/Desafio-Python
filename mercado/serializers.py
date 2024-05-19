from rest_framework import serializers
from mercado.models import Produto, Pedido,usuario
from django.contrib.auth.models import Group, Permission


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = usuario
        fields = ['id', 'username', 'password', 'email']

    def create(self, validated_data):
        user = usuario.objects.create_user(**validated_data)
        default_group, created = Group.objects.get_or_create(name='default_group')
        default_group.user_set.add(user)

        # Adicionar todas as permissões ao grupo "default_group"
        permissions = Permission.objects.all()
        default_group.permissions.set(permissions)

        return user



class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
