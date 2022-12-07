from fastfood.models import *

Azat = Client.objects.create(email='nikname21@gmail.com', password='defender42', name="Azat Sokolov", card_number='4147565798789009')
Altynai = Worker.objects.create(email='altywa1998@gmail.com', password='nono34', name="Altynai Alieva", position='waiter')
b_1 = Food.objects.create(food='waurma', start_price=50)
b_2 = Food.objects.create(food='humburger', start_price=25)
i_1 = Ingredient.objects.create(name='cheese', extra_price=10)
i_2 = Ingredient.objects.create(name='chicen', extra_price=70)
i_3 = Ingredient.objects.create(name='govadina', extra_price=80)
i_4 = Ingredient.objects.create(name='salat', extra_price=15)
i_5 = Ingredient.objects.create(name='fri', extra_price=15)

b_1.structure.set([i_1, i_3, i_4, i_5], through_defaults={"client":Azat, "worker":Altynai})
b_2.structure.set([i_2, i_4], through_defaults={"client":Azat, "worker":Altynai})


summa_1 = (b_1.start_price + i_1.extra_price + i_3.extra_price + i_4.extra_price + i_5.extra_price)
summa_2 = (b_2.start_price + i_2.extra_price + i_4.extra_price)

print(summa_1)
print(summa_2)

