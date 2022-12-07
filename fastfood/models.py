from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=20, verbose_name='Почта')
    password = models.CharField(max_length=100, verbose_name="Пароль")

    def __str__(self):
        return self.email

    class Meta:
        abstract = True


class Client(User):
    name = models.CharField(max_length=20, verbose_name='Имя')
    card_number = models.IntegerField(verbose_name='Номер карточки')

    class Meta(User.Meta):
        pass


class Worker(User):
    name = models.CharField(max_length=20, verbose_name='Имя')
    position = models.CharField(max_length=100, verbose_name='Должность')

    class Meta(User.Meta):
        pass


class Ingredient(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование ингридиента')
    extra_price = models.IntegerField(verbose_name='Надбавка')

    def __str__(self):
        return self.name


class Food(models.Model):
    food = models.CharField(max_length=200, verbose_name='Блюдо')
    start_price = models.IntegerField(verbose_name="Начальная стоимость")
    structure = models.ManyToManyField(Ingredient, related_name='foods', through='Order')

    def __str__(self):
        return self.food


class Order(models.Model):
    Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    order_date_time = models.DateTimeField(auto_now_add=True)

