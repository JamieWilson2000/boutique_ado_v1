from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JhXj4K0DlF3DBaToBGf1GM4rBJegnlT272i56AzXBgF2bkkW9OtzXOtO1h9zgAuMCseLjScX7lBQe847hS2xi3b00AXjlAzfK',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)