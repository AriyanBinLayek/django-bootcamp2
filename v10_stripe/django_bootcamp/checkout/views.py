from django.conf import settings
from django.views import generic
from django.shortcuts import redirect

import stripe

from products.models import Product


class CheckoutView(generic.TemplateView):
    template_name = 'checkout/checkout_view.html'

    def dispatch(self, request, *args, **kwargs):
        product_id = request.session.get('product_id')
        if not product_id:
            return redirect('/products/')
        try:
            self.product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return redirect('/products/')
        return super(CheckoutView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(CheckoutView, self).get_context_data(**kwargs)
        ctx.update({
           'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
           'amount': int(self.product.price * 100),
           'title': self.product.title,
        })
        return ctx
        
    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        token = request.POST.get('stripeToken')
        amount = request.POST.get('amount')
        user = request.user
        stripe.Charge.create(
            amount=amount,
            currency='sgd',
            source=token,
            description="Credit Card Payment to Django Bootcamp",
            shipping={
                'address': {
                    'city': user.shipping_city,
                    'country': 'SG',
                    'line1': user.shipping_street,
                    'postal_code': user.shipping_zip,
                    'state': user.shipping_state,
                },
                'name': '{} {}'.format(
                    user.shipping_first_name, user.shipping_last_name),
                'phone': user.shipping_phone,
            }
        )
        return redirect('checkout_success_view') 
