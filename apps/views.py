from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, CreateView, FormView

from apps.forms import RegisterForm, LoginForm


def home_page_view(request):
    return render(request, 'home-page.html')


def login_view(request):
    return render(request, 'login.html')


def courses_view(request):
    return render(request, 'courses.html')


def recipies_view(request):
    return render(request, 'recipies.html')


def blog_view(request):
    return render(request, 'blog.html')


def about_view(request):
    return render(request, 'about.html')


def aloqa_view(request):
    return render(request, 'aloqa.html')

def nutrition_view(request):
    return render(request, 'nutrisologiya.html')

def fitness_view(request):
    return render(request, 'fitnes.html')

def psychology_view(request):
    return render(request, 'psixologiya.html')

def massaj_view(request):
    return render(request, 'massaj.html')

def seminar_view(request):
    return render(request, 'seminarlar.html')
#
# class HomeListView(LoginRequiredMixin, ListView):
#     queryset = Product.objects.all()
#     template_name = 'home.html'
#     context_object_name = 'products'
#     login_url = reverse_lazy('login')
#
#     def get_queryset(self):
#         query = super().get_queryset()
#         query = query.filter(user=self.request.user)
#         return query
#
#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         data['categories'] = Category.objects.all()
#         return data
#
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)
#
# class ProductDetailView(DetailView):
#     queryset = Product.objects.all()
#     template_name = 'product-detail.html'
#     context_object_name = 'product'
#     pk_url_kwarg = 'pk'
#
# class ProductDeleteView(DeleteView):
#     queryset = Product.objects.all()
#     template_name = 'product-list.html' #get
#     success_url = reverse_lazy('home') #post
#
# class RegisterCreateView(CreateView):
#     queryset = User.objects.all()
#     form_class = RegisterForm
#     template_name = 'register.html'
#     success_url = reverse_lazy('home')
#
# class LoginFormView(FormView):
#     form_class = LoginForm
#     template_name = 'login.html'
#     success_url = reverse_lazy('home')
#
#     def form_valid(self, form):
#         password = form.cleaned_data.get('password')
#         username = form.cleaned_data.get('username')
#         query = User.objects.filter(username=username)
#         if query.exists():
#             user = query.first()
#             if check_password(password, user.password):
#                 login(self.request, user)
#             else:
#                 messages.error(self.request, 'Invalid Password')
#                 return redirect('login')
#         else:
#             messages.error(self.request, 'Invalid Username')
#             return redirect('login')
#
#         return super().form_valid(form)
#
#
#     def form_invalid(self, form):
#         pass
#
#
# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return redirect('register')
