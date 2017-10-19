from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^shipping-address/$', TemplateView.as_view(
        template_name='users/user_shipping_address_view.html')),
]