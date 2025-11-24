from django.urls import path, include
from .views import login_view, refresh_token_view, logout_view, protected_view

from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

from .views import GetCurrentUserView

from accounts.views import GoogleLogin, UserView, LogoutView

from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')



urlpatterns = [
    path('login/', login_view),
    path('refresh/', refresh_token_view),
    path('protected/', protected_view),
    path('logout/', logout_view),  
    path('autenticate/', GetCurrentUserView.as_view()),
    # Adiciona todas as rotas REST do router
    path('', include(router.urls)), 
    #rotas do login do google
    path("google/", GoogleLogin.as_view(), name="google_login"),
    #path("user/", UserView.as_view(), name="user"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # endpoints do allauth (útil em debug)
    
    
    #novas urls Google Login usando Gemini
    path('user/', views.get_current_user, name='get_current_user'),
    path('logout/', views.custom_logout, name='custom_logout'),
    # URLs do allauth (ex: /accounts/google/login/)
    
]
