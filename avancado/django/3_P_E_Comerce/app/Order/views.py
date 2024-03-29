from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Order, ItemOrder
from Product.models import Variation
from django.contrib import messages
from utils import utils


class DispatchLoginRequiredMixin(View):
    def dispatch(self, *args: Any, **kwargs: Any) -> HttpResponse:
        if not self.request.user.is_authenticated:
            return redirect('Profile:create')
        
        return super().dispatch(*args, **kwargs)
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(user=self.request.user)
        return qs
    

class Pay(DispatchLoginRequiredMixin, DetailView):
    template_name = 'Order/_pay.html'
    model = Order
    pk_url_kwarg = 'pk'
    context_object_name = 'order'


class SaveOrder(View):
    template_name = 'Order/_pay.html'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(self.request, 'Login necessário')
            return redirect('Profile:create')
        
        if not self.request.session.get('car'):
            messages.error(self.request, 'Carrinho vazio')
            return redirect('Product:list')
        
        car = self.request.session.get('car')
        print(car)
        car_variation_ids = [v for v in car]
        bd_variation = list(Variation.objects.select_related('Product').filter(id__in=car_variation_ids))

        for variation in bd_variation:
            vid = str(variation.id)
            stock = variation.stock
            qtd_car = car[vid]['amount']            
            price_unt = car[vid]['price']
            price_unt_promo = car[vid]['price_promotional']
    
            error_msg_stock = ''

            if stock < qtd_car:
                car[vid]['amount'] = stock
                car[vid]['price'] = stock * price_unt
                car[vid]['price_promotional'] = stock * price_unt_promo

                error_msg_stock = 'Estoque insuficiente para alguns '\
                    'produtos do seu carrinho. '\
                    'Reduzimos a quantidade desses produtos. Por favor, '\
                    'verifique quais produtos foram afetados a seguir.'
                
            if error_msg_stock:
                messages.error(self.request, error_msg_stock)
            
                self.request.session.save()
                return redirect('Product:car')
            
            qtd_total_car = utils.cart_total_qtd(car)
            total_car = utils.cart_totals(car)

        order = Order(user=self.request.user, total=total_car, qtd_total = qtd_total_car, status='C')
        order.save()

        ItemOrder.objects.bulk_create(
            [
                Order(
                    order=order,
                    product=v['product_name'],
                    product_id=v['product_id'],
                    variation=v['variation_name'],
                    variation_id=v['variation_id'],
                    price=v['rederizar'],
                    price_promo=v['price_promotional'],
                    amount=v['amount'],
                    image=v['image'],
                ) for v in car.values()
            ]
        )

        del self.request.session['car']

        return redirect('Order:pay', kwargs={'pk':order.pk})

class Detail(DispatchLoginRequiredMixin,DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'Order/_details.html'
    pk_url_kwarg = 'pk'

class List(DispatchLoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'Order/_list.html'
    paginate_by = 10
    ordering = ['-id']


