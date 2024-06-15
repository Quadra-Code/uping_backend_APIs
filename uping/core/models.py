from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
# Create your models here.

# class Imgs(models.Model):
#     img = models.ImageField(upload_to='images/', blank=True, null=True)

#     def __str__(self):
#         return self.img_path

class Country(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    img = models.ImageField(upload_to='images/countries/')

    def __str__(self):
        return self.name

class CategoriesTree(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    is_parent = models.BooleanField(default=False)
    level = models.IntegerField(default=0)
    parent_fk = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)
    img = models.ImageField(upload_to='images/categories/')

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    category_fk = models.ForeignKey(CategoriesTree, on_delete=models.PROTECT)
    country_fk = models.ForeignKey(Country, on_delete=models.PROTECT)
    sell_price = models.FloatField(blank=True, null=True)
    purchase_price = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    ingredients = models.CharField(max_length=255, blank=True, null=True)
    how_to_use = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField()
    offer = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)
    unit = models.CharField(max_length=45, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class ItemImg(models.Model):
    item_fk = models.ForeignKey(Item, related_name='item_img', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/item/')

    def __str__(self):
        return f'Image For Item {self.item_fk}'

class Client(models.Model):
    full_name = models.CharField(max_length=128, blank=True, null=True)
    main_phone = models.ForeignKey('ClientPhone', on_delete=models.CASCADE, null=True, blank=True)
    main_address = models.ForeignKey('ClientAddress', on_delete=models.CASCADE, null=True, blank=True)
    user_fk = models.ForeignKey(User, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.full_name

class ClientAddress(models.Model):
    client_fk = models.ForeignKey(Client, related_name='client_addresses', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return self.address

class ClientPhone(models.Model):
    client_fk = models.ForeignKey(Client, related_name='client_phones', on_delete=models.CASCADE)
    phone = models.CharField(max_length=45)
    
    def __str__(self):
        return self.phone

class OrderMaster(models.Model):
    STATE_CHOICES = [
        ('0', 'Pending'),
        ('1', 'Shipped'),
        ('2', 'Delivered')
    ]
    PAYMENT_CHOICES = [
        ('0', 'Cash On Delivery'),
        ('1', 'Visa'),
        ('2', 'Master Card'),
        ('3', 'Apple Pay'),
        ('4', 'Google Pay'),
        ('5', 'KNET Pay')
    ]
    client_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=45)
    paid = models.BooleanField(default=False)
    payment_type = models.CharField(choices=PAYMENT_CHOICES, default='0', max_length=1)
    datetime = models.DateTimeField(blank=True, null=True)
    state = models.CharField(choices=STATE_CHOICES, max_length=1, default='0')
    delivery_address = models.CharField(max_length=255)
    # order_total = models.FloatField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    @property
    def order_total(self):
        total = self.order_details.aggregate(total_price=Sum('detail_total'))['total_price']
        return total or 0

    def __str__(self):
        return f'Order Number {self.id}'

class OrderDetail(models.Model):
    order_master_fk = models.ForeignKey(OrderMaster, related_name='order_details', on_delete=models.PROTECT)
    item_fk = models.ForeignKey(Item, on_delete=models.PROTECT)
    quantity = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    @property
    def detail_total(self):
        return self.quantity * self.item_fk.sell_price

    def __str__(self):
        return f'Order Detail Number {self.id}'