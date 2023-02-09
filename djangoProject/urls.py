from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from app.views import AuthorModelViewSet, ArticleModelViewSet, BookModelViewSet, BiographyModelViewSet, MyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from graphene_django.views import GraphQLView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='DjangoProject',
        default_version='0.1',
        description='Doc  for project',
        contact=openapi.Contact(email='admin@admin.com'),
        license=openapi.License(name='MIT License')
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('article', ArticleModelViewSet)
router.register('biography', BiographyModelViewSet)
router.register('books', BookModelViewSet)
# router.register('my', MyAPIView, basename='my')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('api/', include(router.urls)),

    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Для работы документации API

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # re_path(r'^myapi/(?P<version>\d)/authors/$', MyAPIView.as_view({'get': 'list'})),
    # path('api/1/authors', include('app.urls', namespace='1')),
    path('api/authors', MyAPIView.as_view()),


]
