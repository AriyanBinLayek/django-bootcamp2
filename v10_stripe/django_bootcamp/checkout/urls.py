from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.CheckoutView.as_view(), name='checkout_view'),
    url(r'^success/$',
        TemplateView.as_view(template_name='checkout/checkout_success_view.html'),
        name='checkout_success_view'),
]