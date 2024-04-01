def formact_price(val):
    return f'R$ {val:.2f}'.replace('.', ',')


def cart_total_qtd(car):
    return sum([item['amount'] for item in car.values()])


def cart_totals(car):
    return sum(
        [
            item.get('price')
            if item.get('price_promotional')
            else item.get('amount')
            for item
            in car.values()
        ]
    )