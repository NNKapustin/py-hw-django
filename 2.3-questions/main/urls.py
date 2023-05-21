from django.urls import path

from main.views import ProductsListView, ProductsListByCategory

urlpatterns = [
    path('products/', ProductsListView.as_view(), name='list'),
    path('products/<slug:category_id>/', ProductsListByCategory.as_view(), name='list-by-category')
]
