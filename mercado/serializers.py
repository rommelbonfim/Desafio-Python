from rest_framework import serializers
from mercado.models import Produto, Pedido,usuario, ItemPedido
from django.contrib.auth.models import Group, Permission


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = usuario
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']

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
        fields = ['id', 'nome', 'preco']

class ItemPedidoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)

    class Meta:
        model = ItemPedido
        fields = ['produto', 'quantidade']

class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True, source='itens_pedido', read_only=True)

    class Meta:
        model = Pedido
        fields = ['id','itens']

    def create(self, validated_data):
        user = self.context['request'].user
        pedido = Pedido.objects.create(usuario=user)
        itens_data = self.context.get('view').request.data.get('itens', [])

        for item_data in itens_data:
            produto = Produto.objects.get(nome=item_data['produto'])
            quantidade = item_data['quantidade']
            ItemPedido.objects.create(pedido=pedido, produto=produto, quantidade=quantidade)

        return pedido



