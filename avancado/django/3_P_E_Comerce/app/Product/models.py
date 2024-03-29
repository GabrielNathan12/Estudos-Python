from django.conf import settings
from django.db import models
import os
from PIL import Image
from django.db import models
from django.utils.text import slugify
from utils import utils

class Product(models.Model):
    name = models.CharField(max_length=255)
    description_short = models.TextField(max_length=255)
    description_long = models.TimeField()
    image = models.ImageField(upload_to='product_images/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    price_marketing = models.FloatField(verbose_name='Price')
    price_marketing_promotion = models.FloatField(default=0, verbose_name='Price Promo. ')
    _type = models.CharField(default='V', max_length=1, choices=(('V', 'Variável'),('S', 'Simples'),))


    def get_price_formact(self):
        return utils.formact_price(self.price_marketing)
    
    def get_price_formact_promo(self):
        return utils.formact_price(self.price_marketing_promotional)
    

    @staticmethod
    def resize_image(img, new_width):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(img_full_path,optimize=True,quality=80)


    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.name)}'
            self.slug = slug

        super().save(*args, **kwargs)
        max_image_size = 800

        if self.image:
            self.resize_image(self.image, max_image_size)

    def __str__(self) -> str:
        return self.name
    

class Variation(models.Model):
    class Meta:
        verbose_name = 'Variation'
        verbose_name_plural = 'Variations'

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField()
    price_promotion = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.name or self.product.name
    
    