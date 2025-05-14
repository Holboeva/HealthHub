from datetime import timedelta
import random

from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView
from redis import Redis

from apps.forms import LoginForm, RegisterModelForm, EmailForm
from django.shortcuts import render

from root.settings import EMAIL_HOST_USER
from .models import BlogPost

redis = Redis()


class RegisterCreateView(CreateView):
    form_class = RegisterModelForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_invalid(self, form):
        for error in form.errors.values():
            messages.error(self.request, error)
        return super().form_invalid(form)

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        sms_code = form.cleaned_data.get('sms')
        redis = Redis()
        try:
            redis_code = redis.get(email)
            if not redis_code:
                messages.error(self.request, "Kod muddati tugagan.")
                return redirect('check_email')

            if int(redis_code) != int(sms_code):
                messages.error(self.request, "Kod noto'g'ri !!!")
                return redirect(reverse_lazy('send_email'))
            user = form.save()
            login(self.request, user)
            return redirect(self.success_url)
        finally:
            redis.close()


class SendMailFormView(FormView):
    form_class = EmailForm
    template_name = 'register.html'
    success_url = reverse_lazy('check_email')

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        verify_code = random.randrange(10 ** 5, 10 ** 6)
        send_mail(
            subject="Verification Code !!!",
            message=f"{verify_code}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False
        )
        redis.set(email, verify_code)
        redis.expire(email, time=timedelta(minutes=5))

        return render(self.request, 'base/chack_sms.html', {"email": email})

    def form_invalid(self, form):
        for error in form.errors.values():
            messages.error(self.request, error)
        return super().form_invalid(form)


class LoginFormView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.user
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {'posts': posts})


#
# class HomeListView(LoginRequiredMixin, ListView):
#     queryset = Product.objects.all()
#     template_name = 'home-page.html'
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
#
# class CategoriesView(ListView):
#     queryset = Category.objects.all()
#     context_object_name = 'categories'
#     template_name = 'auth/categories/products-list.html'
#     slug_url_kwarg = 'slug'
#
#     def get_context_data(self, **kwargs):
#         contex = super().get_context_data(**kwargs)
#         if self.kwargs.get('slug'):
#             contex['products'] = Product.objects.filter(category__slug=self.kwargs.get('slug'))
#
#         else:
#             contex['products'] = Product.objects.all().order_by('-created_at')
#
#         return contex
#
#
# class ProfileListView(UpdateView):
#     template_name = 'auth/profile.html'
#     queryset = User.objects.all()
#     success_url = reverse_lazy('profile')
#
#     def get_success_url(self):
#         return reverse('profile', kwargs={'pk':self.request.user.pk})
#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         data['regions'] = Region.objects.all()
#         return data
#
#
# # class AccountView(LoginRequiredMixin, TemplateView):
# #     template_name = 'account/my_account.html'
# #     login_url = reverse_lazy('send_email')
#
# class WebsiteInfoView(TemplateView):
#     template_name = 'about.html'
#
# # class OrderView(TemplateView):
# #     template_name = 'auth/categories/detail/ready_for_order.html'
#

def home_page_view(request):
    return render(request, 'home-page.html')


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
