from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .models import Product
# def products_list(request):
#     ...


# class ProductsListView(View):
#     def get(self, request):
#         products = Product.objects.all()
#         #SELECT * FROM products;
#         # products = Product.objects.filter(...)
#         #SELECT * FROM products WHERE ...
#         template_name = 'products/list.html'
#         return render(request, template_name, {'products': products})


class ProductsListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'
    context_object_name = 'products'
    # paginate_by = 2
    # page_kwarg = 'p'

    def get_queryset(self):
        queryset = super().get_queryset()
        price_from = self.request.GET.get('price_from', 0)
        price_to = self.request.GET.get('price_to', 0)
        if price_from:
            queryset = queryset.filter(price__gte=price_from)
        if price_to:
            queryset = queryset.filter(price__lte=price_to)
        q = self.request.GET.get('search')
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset


class ProductsListByCategory(View):
    def get(self, request, category_id):
        products = Product.objects.filter(category_id=category_id)
        template_name = 'products/list.html'
        return render(request, template_name, {'products': products})
