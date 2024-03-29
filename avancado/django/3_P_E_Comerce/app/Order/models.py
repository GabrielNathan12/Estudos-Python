from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    qtd_total = models.PositiveIntegerField()
    status = models.CharField(
                            default="C",
                            max_length=1,
                            choices=(
                                ('A', 'Aprovado'),
                                ('C', 'Criado'),
                                ('R', 'Reprovado'),
                                ('P', 'Pendente'),
                                ('E', 'Enviado'),
                                ('F', 'Finalizado'),
                            )
    )

    def __str__(self) -> str:
        return f'Pedido número: {self.pk}'
    

class ItemOrder(models.Model):
    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    product_id = models.PositiveIntegerField()
    variation = models.CharField(max_length=255)
    variation_id = models.PositiveIntegerField()
    price = models.FloatField()
    price_promotional = models.FloatField(default=0)
    amount = models.PositiveIntegerField()
    image = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return f'Item do {self.order}'
    

    