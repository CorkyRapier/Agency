from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    sale = 'Продажа'
    rent = 'Аренда'
    title = models.CharField(max_length=80)
    date_create = models.DateTimeField(auto_now_add=True)
    type_category = models.CharField(choices=[('ПРОДАЖА', sale), ('АРЕНДА', rent)], max_length=10)
    subtype_category = models.IntegerField(choices=[
                                                (0, 'Жилая'), 
                                                (1, 'Загородная'), 
                                                (2, 'Коммерческая')], default=0)

    def __str__(self):
        return self.title    


class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    gender = models.IntegerField(choices=[(0, 'Ж'), (1, 'М')], default=0)
    series = models.CharField(max_length=4)
    number = models.CharField(max_length=6)
    phone = models.CharField(max_length=20)
    user = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.last_name} {self.first_name} - владелец'  


class Area(models.Model):
    area_name = models.CharField(max_length=250)
    area_abbr = models.CharField(max_length=20, null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.area_name


class RealEstate(models.Model):
    sale = 'Продажа'
    rent = 'Аренда'
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=False, blank=False)
    description = models.TextField()
    number_of_rooms = models.IntegerField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    price = models.IntegerField()
    total_area = models.CharField(max_length=10)
    floor = models.CharField(max_length=4)
    max_floor = models.CharField(max_length=4)
    type_real_estate = models.CharField(choices=[('ПРОДАЖА', sale), ('АРЕНДА', rent)], max_length=10)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.number_of_rooms}-х комнатная {self.owner}'

    def get_absolute_url(self):
        return reverse('main:detail', kwargs={"estate_id": self.pk})


class Image(models.Model):
    img = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    real_estate = models.ForeignKey(RealEstate, related_name='photos', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.real_estate.number_of_rooms}-х комнатная {self.real_estate.owner} image'


class Realtor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    gender = models.IntegerField(choices=[(0, 'Ж'), (1, 'М')], default=0)
    series = models.CharField(max_length=4)
    number = models.CharField(max_length=6)
    phone = models.CharField(max_length=20)
    experience = models.CharField(max_length=3)
    description = models.TextField()
    realtor_image = models.ImageField(blank=True, upload_to='realtor_photo/%Y/%m/%d/', verbose_name='Фото риелтора')

    def __str__(self):
        return f'{self.last_name} {self.first_name} - риелтор'


class Discount(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title 


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    gender = models.IntegerField(choices=[(0, 'Ж'), (1, 'М')], default=0, blank=True, null=True)
    series = models.CharField(max_length=4, blank=True, null=True)
    number = models.CharField(max_length=6, blank=True, null=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.last_name} {self.first_name} - покупатель'


class Request(models.Model):
    real_estate = models.ForeignKey(RealEstate, related_name='e_request', on_delete=models.CASCADE)
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE, blank=True, null=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, null=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, blank=True, null=True)
    date_request = models.DateTimeField(auto_now_add=True)
    request_status = models.CharField(max_length=50)

    def __str__(self):
        return f'Заявка - {self.pk}'
