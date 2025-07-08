from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView

from shop.forms import BrandForms, ToolForms, ToolAdminForm, ToolAdminFormCreate
from shop.models import Brand, Tool
from shop.utils import slug_generator
from users.models import UserRolls


class AboutView(TemplateView):
    template_name = 'shop/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Электроинструмент - о нас'
        return context


# def about_view(request):
#     context = {
#         'title': 'Электроинструмент - о нас',
#     }
#
#     return render(request, 'shop/about.html', context=context)


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
    slug_url_kwarg = "brand_slug"
    extra_context = {
        'title': 'Все наши инструменты'
    }
    template_name = 'shop/tool_list.html'
    paginate_by = 3

    def get_queryset(self):
        category_slug = self.kwargs.get(self.slug_url_kwarg)
        on_sale = self.request.GET.get("on_sale")
        order_by = self.request.GET.get("order_by")
        tools = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            tools = Tool.objects.filter(Q(description__icontains=query))
        else:
            tools = super().get_queryset().order_by('id')
            if not tools.exists():
                raise Http404()

        if on_sale:
            tools = tools.filter(discount__gt=0)

        if order_by and order_by != "default":
            tools = tools.order_by(order_by)
        print(category_slug)
        return tools


class ToolCreateView(LoginRequiredMixin, CreateView):
    model = Tool
    form_class = ToolAdminFormCreate
    template_name = 'shop/tool_create.html'
    extra_context = {
        'title': 'Добавить Инструмент'
    }
    success_url = reverse_lazy('shop:tools')

    # def form_valid(self, form):
    #     if self.request.user.role != UserRolls.ADMIN:
    #         raise PermissionDenied()
    #     self.object = form.save()
    #     self.object.owner = self.request.user
    #     self.object.save()
    #     return super().form_valid(form)

    def form_valid(self, form):
        if self.request.user.role not in [UserRolls.USER, UserRolls.ADMIN]:
            return HttpResponseForbidden
        slug_object = form.save()
        if slug_object.slug == 'temp_slug':
            slug_object.slug = slug_generator(slug_object.name)
            slug_object.author = self.request.user
            slug_object.save()
        return super().form_valid(form)


class ToolDetailView(DetailView):
    model = Tool
    template_name = 'shop/tool_card.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        object_ = self.get_object()
        context_data['title'] = f'Подробная информация {object_}'
        # dog_object_increase = get_object_or_404(Tool, pk=object_.pk)
        return context_data


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


class ToolUpdateView(LoginRequiredMixin, UpdateView):
    model = Tool
    form_class = ToolForms
    template_name = 'shop/tool_update.html'
    success_url = reverse_lazy('shop:tools')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        object_ = self.get_object()
        print(object_)
        context_data['title'] = f'Изменить инструмент {object_}'
        return context_data

    # def get_success_url(self):
    #     return reverse('shop:tools', args=[self.kwargs.get('pk')])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        # if self.object.owner != self.request.user and not self.request.user.is_staff:
        #     raise Http404
        return self.object

    def get_form_class(self):
        dog_forms = {
            UserRolls.ADMIN: ToolAdminForm,
            UserRolls.MODERATOR: ToolForms,
            UserRolls.USER: ToolForms,
        }
        user_role = self.request.user.role
        dog_form_class = dog_forms[user_role]
        return dog_form_class


class BrandToolsListView(ListView):
    model = Tool
    template_name = 'shop/brand_tools.html'
    extra_context = {'title': 'Инструменты данного брэнда'}

    def get_queryset(self):
        # Получаем слаг бренда из URL
        brand_slug = self.kwargs.get('slug')

        # Получаем бренд по слагу
        brand = Brand.objects.get(slug=brand_slug)

        # Фильтруем инструменты по бренду
        queryset = super().get_queryset().filter(brand=brand)
        return queryset
