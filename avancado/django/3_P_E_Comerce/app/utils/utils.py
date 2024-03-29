def formact_price(val):
    return f'R$ {val:.2f}'.replace('.', ',')


def cart_total_qtd(car):
    return sum([item['amount'] for item in car.values()])


def cart_totals(car):
    return sum(
        [
            item.get('promotional_quantitative_price')
            if item.get('promotional_quantitative_price')
            else item.get('quantitative_price')
            for item
            in car.values()
        ]
    )