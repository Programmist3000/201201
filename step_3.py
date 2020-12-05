...

housing = ['House', 'Apartment', 'Studio', 'Hostel']
#             0          1           2         3
#            -4         -3          -2        -1

print('House: 25.000$')
print('Apartment: 5.000$')
print('Studio: 7.500$')
print('Hostel: 1.000$')

print('Все жилье которое стоит дороже 10,000$:')
print('1.', housing[-4])

print('Все жилье которое стоит дешевле 7.000$:')
print('1.', housing[1])
print('2.', housing[-1])

print('По мнению продавца оптимальное жилье является:')
print(housing[-2])

print('По мнению продавца худшее жилье является:')
print(housing[3])
