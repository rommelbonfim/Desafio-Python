from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import usuario, Produto, Pedido
from .serializers import UsuarioSerializer, ProdutoSerializer, PedidoSerializer

# Gerenciamento de usuários
class UsuarioCreateView(generics.CreateAPIView):
    serializer_class = UsuarioSerializer

class UsuarioLoginView(generics.GenericAPIView):
    serializer_class = UsuarioSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validate_user(request.data)
            if user:
                return Response({'token': user.auth_token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        return self.request.user

# Gerenciamento de produtos
class ProdutoCreateView(generics.CreateAPIView):
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class ProdutoUpdateView(generics.UpdateAPIView):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class ProdutoDeleteView(generics.DestroyAPIView):
    queryset = Produto.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class ProdutoListView(generics.ListAPIView):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

# Gestão de Pedidos
class PedidoCreateView(generics.CreateAPIView):
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class PedidoListView(generics.ListAPIView):
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Pedido.objects.filter(usuario=self.request.user)

class PedidoDetailView(generics.RetrieveAPIView):
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

