from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from shop.forms import BrandForms, ToolForms
from shop.models import Brand, Tool
from users.models import UserRolls


def about_view(request):
    context = {
        'title': 'Электроинструмент - о нас',
    }

    return render(request, 'shop/about.html', context=context)


class BrandListView(ListView):
    model = Brand
    extra_context = {
        'title': 'Все наши брэнды'
    }
    template_name = 'shop/brand_list.html'
    paginate_by = 3


class BrandCreateView(LoginRequiredMixin, CreateView):
    model = Brand
    form_class = BrandForms
    template_name = 'shop/brand_create.html'
    extra_context = {
        'title': 'Добавить брэнд'
    }
    success_url = reverse_lazy('shop:catalog')

    def form_valid(self, form):
        if self.request.user.role == UserRolls.USER:
            raise PermissionDenied()
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

class ToolListView(ListView):
    model = Tool
    extra_context = {
        'title': 'Все наши инструменты'
    }
    template_name = 'shop/tool_list.html'
    paginate_by = 3

class ToolCreateView(LoginRequiredMixin, CreateView):
    model = Tool
    form_class = ToolForms
    template_name = 'shop/tool_create.html'
    extra_context = {
        'title': 'Добавить Инструмент'
    }
    success_url = reverse_lazy('shop:tools')

    def form_valid(self, form):
        if self.request.user.role != UserRolls.ADMIN:
            raise PermissionDenied()
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ToolDeleteView(PermissionRequiredMixin, DeleteView):
    model = Tool
    template_name = 'shop/tool_delete.html'
    success_url = reverse_lazy('shop:tools')
    permission_required = 'shop.delete_tool'
    permission_denied_message = 'У вас нет нужных прав'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        object_ = self.get_object()
        context_data['title'] = f'Удалить инструмент {object_}'
        return context_data