from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth import logout as django_logout

from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.exceptions import TokenError

from rest_framework import status

from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.views import APIView
from .serializers import UserSerializerAuth

from django.views.decorators.csrf import ensure_csrf_cookie

from allauth.socialaccount.models import SocialAccount

# api para configuração do token

# Login
# LOGIN
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        # 1. Gera os tokens (como você já estava fazendo)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        
        # 2. Prepara a resposta JSON com os dados do usuário
        # Inclua o username e outros dados que o frontend PRECISA
        # response = Response({'message': 'Login realizado com sucesso!'})
        
        response_data = {
            'username': user.username,  # <-- O nome de usuário para o frontend
            'user_id': user.id,        # <-- O ID do usuário (útil)
            # 'email': user.email,     # Você pode adicionar mais campos aqui
        }
        # 3. Cria o objeto de resposta
        response = Response(response_data)
        
        # 4. Define o cookie httpOnly (como você já estava fazendo)
        # 🔥 Cookie do ACCESS TOKEN
        response.set_cookie(
            key="access",
            value=access_token,
            httponly=True,
            samesite="Lax",
            secure=False,  # True se HTTPS
            max_age=300,  # 5 minutos
        )
        # 🔥 Cookie do REFRESH TOKEN
        response.set_cookie(
            key="refresh",
            value=str(refresh),
            httponly=True,
            samesite="Lax",
            secure=False,
            max_age=86400,  # 1 dia
        )

        return response
    else:
        return Response(
            {'message': 'Credenciais inválidas'},
            status=status.HTTP_401_UNAUTHORIZED
        )


# Refresh token
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token_view(request):
    refresh_token = request.COOKIES.get('refresh')  # 🔥 mesmo nome que no login

    if not refresh_token:
        return Response(
            {'detail': 'Refresh token não encontrado.'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    try:
        refresh = RefreshToken(refresh_token)
        access_token = str(refresh.access_token)
        response = Response({'message': 'Token atualizado com sucesso!'})
        # Recria o cookie do access
        response.set_cookie(
            key="access",
            value=access_token,
            httponly=True,
            samesite="Lax",
            secure=False,
            max_age=300,
        )
        return response
    except Exception as e:
        print("Erro ao renovar token:", e)
        return Response(
            {'detail': 'Token inválido ou expirado.'},
            status=status.HTTP_401_UNAUTHORIZED
        )

# Protected route
# VIEW PROTEGIDA
@csrf_exempt
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def protected_view(request):
    user = request.user
    return Response({
        'username': user.username,
        'email': user.email,
        'message': f'Olá {user.username}, você está autenticado!'
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated]) # 1. Exige que o usuário esteja logado
def logout_view(request):
    
    django_logout(request) 
    
    return Response(
        {"detail": "Logout realizado com sucesso."}, 
        status=status.HTTP_200_OK
    )


# Configuração do post
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.AllowAny]  # qualquer um pode criar


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]  # qualquer um pode comentar

class GetCurrentUserView(APIView):
    # Garante que apenas usuários autenticados possam acessar esta view
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # O middleware de autenticação do Django (baseado no cookie)
        # já terá preenchido o 'request.user' com o usuário logado.
        serializer = UserSerializerAuth(request.user)
        return Response(serializer.data)
    

# Recebendo dados do Google Social
# sua_app/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import ensure_csrf_cookie

# Importar o modelo correto
from allauth.socialaccount.models import SocialAccount

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@ensure_csrf_cookie
def get_current_user(request):
    """
    Tenta buscar a URL do avatar da SocialAccount do usuário logado.
    """
    
    avatar_url = None
    
    # --- NOVO BLOCO DE BUSCA MAIS ROBUSTA ---
    try:
        # 1. Tenta encontrar a Social Account para o usuário logado E o provedor 'google'
        social_account = SocialAccount.objects.get(
            user=request.user, 
            provider='google'
        )
        # 2. Se encontrado, obtém a URL do avatar
        avatar_url = social_account.get_avatar_url() 

    except SocialAccount.DoesNotExist:
        # 3. Este erro ocorre se o usuário não logou via Google 
        # (mas apenas com usuário/senha, por exemplo).
        print(f"DEBUG: Social Account Google não encontrada para o usuário {request.user.email}")
        pass
    except Exception as e:
        # 4. Captura qualquer outro erro que possa estar impedindo a execução (ex: AttributeError)
        print(f"ERRO CRÍTICO AO BUSCAR AVATAR: {e}")
        pass
    # ----------------------------------------
    
    user_data = {
        'id': request.user.id,
        'username': request.user.username,
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'avatar_url': avatar_url  
    }
    
    # Linha de debug para o terminal
    print(f"--- DEBUG AVATAR URL FINAL: {avatar_url} ---")
    
    return Response(user_data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def custom_logout(request):
    """
    Faz o logout do usuário e limpa o cookie de sessão.
    """
    django_logout(request)
    return Response({"detail": "Logout realizado com sucesso."}, status=status.HTTP_200_OK)