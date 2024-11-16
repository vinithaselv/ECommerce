from django.db import models

# Create your models here.
from django.db import models


class userModel(models.Model):
    username = models.CharField(max_length=100,null=True)
    user_email = models.EmailField(max_length=254, unique=True, null=True)
    password = models.CharField(max_length=100,null=True)

    gender = models.CharField(max_length=50,null=True)
    post = models.PositiveIntegerField(null=True)
    user_img = models.ImageField(upload_to="folder",null=True)
    phoneno = models.PositiveIntegerField(null=True)
    address = models.TextField(null = True)

    def __str__(self):
        return self.username

    
class Manager(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(unique=True,null=True)
    password = models.CharField(max_length=100,null=True)

    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(max_length=100,null=True)
    Address = models.TextField(null=True)
    Role = models.CharField(max_length=100,null=True)
    mag_img = models.ImageField(upload_to="folder",null=True)



class categoryModel(models.Model):
    cat_name = models.CharField(max_length=100,null=True)
    pro_name = models.TextField()
    pro_img = models.ImageField(upload_to ="folder", null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.cat_name

class productModel(models.Model):
    CATEGORY_CHOICES = [
        ('coffee', 'Coffee'),
        ('dessert', 'Dessert'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to="folder")
    category = models.CharField(max_length=100,null=True)

    # category = models.ForeignKey(categoryModel,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

class AddtoCartModel(models.Model):
    user = models.ForeignKey(userModel,on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(null=True)
    product = models.ForeignKey(productModel,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

class messageModel(models.Model):
    username = models.TextField(null=True)
    email = models.EmailField(max_length=254,null=True)
    message = models.TextField(null=True)

class orderModel(models.Model):
    user = models.ForeignKey(userModel,on_delete=models.CASCADE,null=True)
    user_email = models.EmailField(max_length=254, null=True)
    phone_no = models.PositiveIntegerField()
    address = models.TextField()
    category = models.TextField()
    product = models.CharField(max_length=100,null=True)
    quantity = models.PositiveIntegerField(null=True)
    
    city = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)  
    pincode = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    payment = models.TextField(max_length=50, choices=[('credit_card', 'Credit Card'), ('cash', 'Cash On Delivery')],null=True)

    def __str__(self) :
          return f"Order {self.id} by {self.user.username}"


class Wishlist(models.Model):
    user = models.ForeignKey(userModel,on_delete=models.CASCADE)
    product = models.ForeignKey(productModel,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


