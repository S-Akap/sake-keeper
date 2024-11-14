from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .models import Restaurant, BottleManagement, Bottle
from .forms import RestaurantForm, BottleManagementForm, BottleForm, BottleEditForm
from django.db.models import Q, Count

from django.shortcuts import get_object_or_404, redirect
from django.views import View

# Create your views here.
class IndexView(TemplateView):
    template_name = "app/index.html"

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "app/home.html"



class RestaurantView(LoginRequiredMixin, TemplateView):
    template_name = "app/restaurant/index.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["user_restaurant_list"] = Restaurant.objects.get_index_list(user)
        return context

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    model = Restaurant
    template_name = "app/restaurant/create.html"
    form_class = RestaurantForm
    success_url = reverse_lazy("app:restaurant-list")

class RestaurantListView(LoginRequiredMixin, ListView):
    model = Restaurant
    template_name = "app/restaurant/list.html"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("query")
        if query:
            query_set = Restaurant.objects.get_search_list(query)
        else:
            query_set = Restaurant.objects.order_by("-pk")
        return query_set

class RestaurantDetailView(LoginRequiredMixin, DetailView):
    model = Restaurant
    template_name = "app/restaurant/detail.html"

class RestaurantEditView(LoginRequiredMixin, UpdateView):
    model = Restaurant
    template_name = "app/restaurant/edit.html"
    form_class = RestaurantForm

    def get_success_url(self):
        return reverse_lazy("app:restaurant-detail", kwargs={'pk': self.object.pk})



class BottleManagementView(LoginRequiredMixin, TemplateView):
    template_name = "app/bottle_management/index.html"

class BottleManagementCreateView(LoginRequiredMixin, CreateView):
    model = BottleManagement
    template_name = "app/bottle_management/create.html"
    form_class = BottleManagementForm
    success_url = reverse_lazy("app:bottle-management-list")

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

class BottleManagementListView(LoginRequiredMixin, ListView):
    model = BottleManagement
    template_name = "app/bottle_management/list.html"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("query")
        user = self.request.user
        query_set = BottleManagement.objects.filter(customer=user).annotate(bottle_count=Count('bottle'))
        if query:
            if query_set.exists():
                query_set = query_set.filter(Q(restaurant__name__icontains=query)|Q(management_name__icontains=query))
        else:
            query_set = query_set.order_by("-pk")
        return query_set

class BottleManagementDetailView(LoginRequiredMixin, DetailView):
    model = BottleManagement
    template_name = "app/bottle_management/detail.html"

class BottleManagementEditView(LoginRequiredMixin, UpdateView):
    model = BottleManagement
    template_name = "app/bottle_management/edit.html"
    form_class = BottleManagementForm

    def get_success_url(self):
        return reverse_lazy("app:bottle-management-detail", kwargs={'pk': self.object.pk})
    
class BottleManagementDeleteView(LoginRequiredMixin, DeleteView):
    model = BottleManagement
    template_name = "app/bottle_management/detail.html"
    success_url = reverse_lazy("app:bottle-management-index")



class BottleView(LoginRequiredMixin, TemplateView):
    template_name = "app/bottle/index.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["user_bottle_list"] = Bottle.objects.filter(management__customer=user, is_empty=False)
        return context

class BottleCreateView(LoginRequiredMixin, CreateView):
    model = Bottle
    template_name = "app/bottle/create.html"
    form_class = BottleForm
    success_url = reverse_lazy("app:bottle-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class BottleListView(LoginRequiredMixin, ListView):
    model = Bottle
    template_name = "app/bottle/list.html"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("query")
        user = self.request.user
        if query:
            query_set = Bottle.objects.get_search_list(user=user, query=query)
        else:
            query_set = Bottle.objects.filter(management__customer=user).order_by("-pk")
        return query_set

class BottleDetailView(LoginRequiredMixin, DetailView):
    model = Bottle
    template_name = "app/bottle/detail.html"

class BottleEditView(LoginRequiredMixin, UpdateView):
    model = Bottle
    template_name = "app/bottle/edit.html"
    form_class = BottleEditForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse_lazy("app:bottle-detail", kwargs={'pk': self.object.pk})


class BottleDeleteView(LoginRequiredMixin, DeleteView):
    model = Bottle
    template_name = "app/bottle/detail.html"
    success_url = reverse_lazy("app:bottle-list")

class BottleToggleIsEmptyView(View):
    def post(self, request, pk, *args, **kwargs):
        bottle = get_object_or_404(Bottle, pk=pk)
        bottle.is_empty = not bottle.is_empty
        bottle.save()

        return redirect(reverse("app:bottle-detail", args=[pk]))