from django.views import generic

from . import models


class ProductListView(generic.ListView):
    template_name = 'products/product_list_view.html'
    queryset = models.Product.objects.all()


class ProductDetailView(generic.DetailView):
    template_name = 'products/product_detail_view.html'
    model = models.Product