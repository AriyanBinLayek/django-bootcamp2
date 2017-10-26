from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^shipping-address/$',
        views.ShippingAddressView.as_view(),
        name='users_shipping_address_view'),
]