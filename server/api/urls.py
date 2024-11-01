from django.urls import path, include
from .views.main.main_views import IncomeSourceView
from .views.Auth.auth_view import UserRegistrationView, UserLoginView, CustomTokenRefreshView, LogoutView, PasswordChangeView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'income', IncomeSourceView, basename='income')


urlpatterns = [
    # User Authentication
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),

    # Income API
    path('income/', include(router.urls)),
]
