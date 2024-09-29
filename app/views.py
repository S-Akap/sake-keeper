from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexView(TemplateView):
    template_name = "app/index.html"

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "app/home.html"