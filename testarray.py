resp = {
    'data': {
        'info': {
            'product_1': {
                'prodinfo': 1
            },
            'product_2': {
                'prodinfo': 2
            },
            'product_3': {
                'prodinfo': 3
            }
        }
    }
}


products_key = [x for x in resp['data']['info'].keys()]
print(products_key)
products = []
for key in products_key:
    products.append(resp['data']['info'][key])
