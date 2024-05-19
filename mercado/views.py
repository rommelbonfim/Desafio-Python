from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView

from .models import Produto, Pedido, usuario
from .serializers import UsuarioSerializer, ProdutoSerializer, PedidoSerializer
from rest_framework.authtoken.models import Token

# Gerenciamento de usuários
class UsuarioCreateView(generics.CreateAPIView):
    serializer_class = UsuarioSerializer

class UsuarioLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

class UsuarioProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        return self.request.user

class UsuarioDetailView(generics.RetrieveAPIView):
    queryset = usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
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
        User = get_user_model()
        user = self.request.user
        if user.is_authenticated:
            return Pedido.objects.filter(usuario__in=User.objects.filter(id=user.id))
        return Pedido.objects.none()



class PedidoDetailView(generics.RetrieveAPIView):
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

