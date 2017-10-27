from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProductListView.as_view(), name='products_list_view'),
    url(r'^(?P<pk>\d+)/(?P<slug>[-_\w]+)/$',
        views.ProductDetailView.as_view(),
        name='products_detail_view'),
]