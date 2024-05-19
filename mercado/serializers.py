from rest_framework import serializers
from mercado.models import Produto, Pedido,usuario, ItemPedido
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

class ProdutoNomeRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nome

    def to_internal_value(self, data):
        try:
            produto = Produto.objects.get(nome=data)
        except Produto.DoesNotExist:
            raise serializers.ValidationError('Produto não encontrado')
        return produto

class ItemPedidoSerializer(serializers.ModelSerializer):
 produto_nome = serializers.CharField(source='produto.nome', read_only=True)

 class Meta:
    model = ItemPedido
    fields = ['produto', 'produto_nome', 'quantidade']

 def create(self, validated_data):
    produto = validated_data.pop('produto')
    quantidade = validated_data.pop('quantidade')
    pedido = self.context['pedido']
    item_pedido = ItemPedido.objects.create(pedido=pedido, produto=produto, quantidade=quantidade)
    return item_pedido

class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True, source='itens_pedido', read_only=True)

    class Meta:
        model = Pedido
        fields = ['id','itens']

    def create(self, validated_data):
        pedido = Pedido.objects.create(usuario=self.context['request'].user)
        itens_data = self.context.get('view').request.data.get('itens', [])

        for item_data in itens_data:
            produto = Produto.objects.get(nome=item_data['produto'])
            quantidade = item_data['quantidade']
            ItemPedido.objects.create(pedido=pedido, produto=produto, quantidade=quantidade)

        return pedido



