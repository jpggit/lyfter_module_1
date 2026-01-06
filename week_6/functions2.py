#2. Experimente con el concepto de scope:
#    1. Intente accesar a una variable definida dentro de una función desde afuera.
#    2.  Intente accesar a una variable global desde una función y cambiar su valor.

places_i_played_tennis = [
    'Costa Rica',
    'USA',
]
def places_visited():
    list_of_places = [
        'Costa Rica',
        'USA',
        'France',
        'Germany',
        'Spain',
        'Switzerland',
    ]
    return list_of_places

#print (list_of_places)
print(places_i_played_tennis)