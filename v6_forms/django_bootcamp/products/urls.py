from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(
        template_name='products/product_list_view.html')),
    url(r'^(?P<pk>\d+)/(?P<slug>[-_\w]+)/$', TemplateView.as_view(
        template_name='products/product_detail_view.html'),
        name='products_detail_view'),
]