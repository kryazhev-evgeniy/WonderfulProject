from django import http
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.views.generic import ListView,CreateView,DetailView,UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Service,Order, Category
# Create your views here.

class HomeView(ListView):
    model = Service
    template_name = 'home.html'
    context_object_name = 'services'

class ServiceView(ListView):
    model = Service
    template_name = 'serviceView.html'
    context_object_name = 'services'

class ServiceDetail(DetailView):
    model = Service
    template_name = 'serviceDetail.html'
    context_object_name = 'service'

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileView(DetailView):
    model = User
    template_name = 'userView.html'

class ProfileUpdate(UpdateView):
    model = User
    template_name = 'userUpdate.html'
    fields = ['first_name','last_name', 'email']

    def get_success_url(self):
        return reverse_lazy('profile',kwargs={'pk': self.object.id})
    
class CreateOrder(CreateView):
    model = Order
    fields = ['user_order','service_order','date','time','commentary']
    success_url = reverse_lazy('services')
    template_name = 'orders/create.html'
    
    def get_context_data(self, **kwargs):
        context = super(CreateOrder,self).get_context_data(**kwargs)
        context['user_pk'] = self.kwargs['user_pk']
        context['service_pk'] = self.kwargs['service_pk']
        return context

class ListUserOrder(ListView):
    model = Order
    template_name = 'orders/listUserOrder.html'
    context_object_name = 'orders'
        
    