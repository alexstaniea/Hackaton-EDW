from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    TemplateView, ListView,
    CreateView, UpdateView, DeleteView, DetailView
)

from app.forms import UserProfileForm
from app.models import User, UserProfile, Cart, Article


def index(request):
    article_list = Article.objects.all()
    return render(request, 'index.html', {'article_list': article_list})


def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, "article_detail.html", {"article": article})


class RegisterView(CreateView):
    template_name= 'register.html'
    form_class = UserCreationForm
    model = User

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(username=data['username'],
                                        password=data['password1'])
        Cart.objects.create(user_id=user, sum=0)
        UserProfile.objects.create(user=user)
        return redirect('index')


class LoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self):
        form = AuthenticationForm()
        return {'form': form}

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'],
                                password=data['password'])
            login(request, user)
            return redirect('index')
        else:
            return render(request, "login.html", {"form": form})


class LogoutView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')


class UserProfileView(LoginRequiredMixin, DetailView):
    template_name = 'user_profile.html'
    context_object_name = 'userprofile'

    def get_object(self):
        user = User.objects.get(id=self.kwargs['pk'])
        userprofile = user.profile.first()
        return userprofile


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'user_profile_update.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileUpdateView, self).get_context_data(**kwargs)
        user =  self.object.user
        context['form'].fields['first_name'].initial = user.first_name
        context['form'].fields['last_name'].initial = user.last_name
        context['form'].fields['e_mail'].initial = user.email
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        self.object.birthday = data['birthday']
        self.request.user.first_name = data['first_name']
        self.request.user.last_name = data['last_name']
        self.request.user.email = data['e_mail']
        self.object.address = data['address']
        self.object.credit = data['credit']
        self.object.save()
        self.request.user.save()
        return redirect(reverse_lazy("user_profile", kwargs={"pk": self.request.user.id}))


@login_required(login_url='login')
def add_to_cart(request, pk):
    article = Article.objects.get(id=pk)
    cart = request.user.cart
    cart.articles.add(article)
    cart.sum += article.price
    cart.save()
    return redirect('index')


@login_required(login_url='login')
def remove_from_cart(request, pk):
    article = Article.objects.get(id=pk)
    cart = request.user.cart
    cart.articles.remove(article)
    cart.sum -= article.price
    cart.save()
    return render(request, 'cart_detail.html', {'cart': cart})


@login_required(login_url='login')
def cart_checkout(request, pk):
    cart = request.user.cart
    user = request.user.profile.first()
    if user.credit >= cart.sum:
        user.credit -= cart.sum
        cart.articles.clear()
        cart.sum = 0
        cart.save()
        user.save()
        return redirect('index')
    else:
        return render(request, 'cart_detail.html', {'cart': cart})


class CartDetailView(LoginRequiredMixin, View):
    template_name = 'cart_detail.html'

    def get(self, request, *args, **kwargs):
        #pk = self.kwargs['user_pk']
        cart = request.user.cart
        return render(request, 'cart_detail.html', {'cart': cart})
