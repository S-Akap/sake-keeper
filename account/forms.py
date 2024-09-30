from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
        )
        labels = {
            "username": "ユーザー名",
            "email": "メールアドレス",
        }

class LoginFrom(AuthenticationForm):
    class Meta:
        model = get_user_model()