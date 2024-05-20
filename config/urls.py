
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from mercado import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Mercado API",
        default_version='v1',
        description="Aplicação para gerenciamento de produtos, pedidos e usuários.",
        terms_of_service="#",
        contact=openapi.Contact(email="rommelbonfim.dev@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Gerenciamento de usuários
    path('usuarios/signup/', views.UsuarioCreateView.as_view(), name='usuario-signup'),
    path('usuarios/login/', views.UsuarioLoginView.as_view(), name='usuario-login'),
    path('usuarios/profile/', views.UsuarioProfileView.as_view(), name='usuario-profile'),

    # Gerenciamento de itens
    path('produtos/', views.ProdutoListView.as_view(), name='produto-list'),
    path('produtos/create/', views.ProdutoCreateView.as_view(), name='produto-create'),
    path('produtos/<int:pk>/update/', views.ProdutoUpdateView.as_view(), name='produto-update'),
    path('produtos/<int:pk>/delete/', views.ProdutoDeleteView.as_view(), name='produto-delete'),

    # Gestão de Pedidos
    path('pedidos/', views.PedidoListView.as_view(), name='pedido-list'),
    path('pedidos/create/', views.PedidoCreateView.as_view(), name='pedido-create'),
    path('pedidos/<int:pk>/', views.PedidoDetailView.as_view(), name='pedido-detail'),

    # Obter token de autenticação
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),


    # Documentação da API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
