from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginFrom

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "account/signup.html"
    success_url = reverse_lazy('app:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return response

class LogInView(BaseLoginView):
    form_class = LoginFrom
    template_name = "account/login.html"

class LogOutView(BaseLogoutView):
    success_url = reverse_lazy("app:index")