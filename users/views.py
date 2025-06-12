from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from users.models import User
from users.forms import UserRegisterForm


def index_view(request):
    return render(request, 'users/index.html')


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:index')
    template_name = 'users/register.html'
    extra_context = {
        'title': 'Создать аккаунт'
    }
