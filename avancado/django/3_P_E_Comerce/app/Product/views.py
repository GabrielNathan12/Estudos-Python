from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View
from . import models
from django.db.models import Q
from django.contrib import messages
from Profile.models import Profile

class ListProduct(ListView):
    model = models.Product
    template_name = 'Product/_list.html'
    context_object_name = 'products'
    paginate_by = 10
    ordering = ['-id']

class GetProduct(ListView):
    def get_queryset(self, *args, **kwargs):
        term = self.request.GET.get('termo') or self.request.session['termo']
        qs = super().get_queryset(*args, **kwargs)

        if not term:
            return qs
        
        self.request.session['termo'] = term
        qs = qs.filter(
            Q(name__icontains=term) |
            Q(description_short__icontains=term) |
            Q(description_long__icontains=term))
        
        self.request.session.save()
        return qs
        
class DetailProduct(DetailView):
    model = models.Product
    template_name = 'Product/_details.html'
    context_object_name = 'Product'
    slug_url_kwarg = 'slug'
    
class AddToCar(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get('HTTP_REFERER', reverse('Product:list'))

        variation_id = self.request.GET.get('vid')

        if not variation_id:
            messages.error(self.request, 'Produto não existe')
            return redirect(http_referer)
        
        variation = get_object_or_404(models.Variation, id=variation_id)
        variation_stock = variation.stock
        product = variation.product

        product_id = product.id
        product_name = product.name
        variation_name = variation.name or ''
        price_unt = variation.price
        price_unt_promo = variation.price_promotion
        amount = 1
        slug = product.slug
        image = product.image

        if image:
            image = image.name
        else:
            image = ''

        if variation.stock < 1:
            messages.error(self.request, 'Estoque insuficiente')
            return redirect(http_referer)
        
        if not self.request.session.get('car'):
            self.request.session['car'] = {}
            self.request.session.save()

        car = self.request.session['car']

        if variation_id in car:
            amount_car = car[variation_id]['amount']
            amount_car += 1

            if variation_stock < amount_car:
                messages.warning(self.request,f'Estoque insuficiente para {amount_car}x no '
                    f'produto "{product_name}". Adicionamos {variation_stock}x '
                    f'no seu carrinho.')
                amount_car = variation_stock

            car[variation_id]['amount'] = amount_car
            car[variation_id]['price_amount'] = price_unt * amount_car
            car[variation_id]['price_mount_promo'] = price_unt_promo * amount_car

        else:
            car[variation_id] = {
                'product_id': product_id,
                'product_name': product_name,
                'variation_name' : variation_name,
                'variation_id': variation_id,
                'price_unt': price_unt,
                'price_unt_promo': price_unt_promo,
                'price_amount': price_unt,
                'price_amount_promo': price_unt_promo,
                'amount': 1,
                'slug': slug,
                'image':image
            }
        self.request.session.save()
        messages.success(self.request, f'Produto {product_name} {variation_name} adicionado ao seu '
            f'carrinho {car[variation_id]["quantidade"]}x.')
        
        return redirect(http_referer)

class RemoveToCar(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get('HTTP_REFERER', reverse('Product:list'))

        variation_id = self.request.GET.get('vid')

        if not variation_id:
            return redirect(http_referer)
        
        if not self.request.session.get('car'):
            return redirect(http_referer)
        
        if variation_id not in self.request.session['car']:
            return redirect(http_referer)
        
        car = self.request.session['car'][variation_id]

        messages.success(self.request, f'Produto {car["product_name"]} {car["variation_name"]} '
            f'removido do seu carrinho.')
        
        del self.request.session['car'][variation_id]
        self.request.session.save()
        return redirect(http_referer)
    
class Car(View):
    def get(self, *args, **kwargs):
        context = {
            'car': self.request.session.get('car', {})
        }
        return render(self.request, 'Product/car.html', context)
    
    
class ResumeToShoop(View):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('Profile:create')
        
        profile = Profile.objects.filter(user=self.request.user).exists()
        
        if not profile:
            messages.error(self.request,'Usuário sem perfil')
            return redirect('Profile:create')
        
        if not self.request.session.get('car'):
            messages.error(self.request, 'Carrinho vazio')
            return redirect('Product:list')
        
        context = {
            'user': self.request.user, 
            'car': self.request.session['car']
        }

        return render(self.request, 'Product/_resumeshoop.html', context)