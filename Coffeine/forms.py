from django.forms import ModelForm
from Coffeine.models import categoryModel,messageModel,orderModel,userModel,productModel,AddtoCartModel,Manager,Wishlist


class userform(ModelForm):
    class Meta:
        model = userModel
        fields ="__all__"

class ManagerForm(ModelForm):
    class Meta:
        model = Manager
        fields ="__all__"

class WishlistForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = "__all__"

class categoryform(ModelForm):
    class Meta:
        model = categoryModel
        fields = "__all__"

class productform(ModelForm):
    class Meta:
        model =productModel
        fields = ['category','name','description','price','image']

class Cartform(ModelForm):
    ModelForm = AddtoCartModel
    fields = "__all__"

class messageform(ModelForm):
    class Meta:
        model = messageModel
        fields = ['username','email','message']


class orderform(ModelForm):
    class Meta:
        model = orderModel
        fields = ['user_email','phone_no','address','category','product','quantity','city','pincode','total','payment']