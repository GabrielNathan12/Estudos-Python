import pprint

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30}
]

#dionario_comprehension

novos_produtos = [{**produto, 'preco': produto['preco'] * 1.05} 
                  if produto['preco'] > 20 else {**produto}
                  for produto in produtos
                  if (produto['preco'] * 1.05) > 10
                    
                  ]

pprint.pprint(novos_produtos)


lista = [n for n in range(10) if n < 5]

pprint.pprint(lista)