from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render, get_object_or_404
from .models import Order
from carts.models import Cart


@login_required
def checkout_cart(request):
    cart = Cart.objects.filter(customer=request.user, status='pending').first()

    if cart and cart.items.exists():
        if not Order.objects.filter(cart=cart).exists():
            Order.objects.create(
                customer=request.user,
                cart=cart,
                status='pending'
            )

    return redirect('order_list')


@login_required
def order_list(request):
    orders = Order.objects.filter(customer=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})


@user_passes_test(lambda u: u.is_staff)
def manage_orders(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'orders/manage_orders.html', {'orders': orders})


@user_passes_test(lambda u: u.is_staff)
def approve_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'approved'
    order.cart.status = 'approved'
    order.cart.save()
    order.save()
    return redirect('manage_orders')


@user_passes_test(lambda u: u.is_staff)
def deny_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'denied'
    order.cart.status = 'denied'
    order.cart.save()
    order.save()
    return redirect('manage_orders')