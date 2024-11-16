"""
URL configuration for ECommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings

from django.conf.urls.static import static

from Coffeine import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.sign,name = "sign"),
    path("login/",views.login,name = "login"),
    path('logout/',views.logout,name='logout'),
    path("register/",views.register,name = "register"),
    

    path('home/',views.home,name="home"),
    path('profile/',views.profile,name = 'profile'),
    path('about/',views.aboutus,name="about"),
    path('menu/',views.menu,name="menu"),
    path('order/',views.order,name="order"),
    path('contact/',views.contact,name="contact"),
    path('product/',views.product,name="product"),
    path('cart/',views.cart,name="cart"),
    path('add_wishlist/<int:id>/',views.add_wishlist,name = "add_wishlist"),
    path('wishlist/',views.wishlist,name = "wishlist"),
    path('booking/',views.booking,name="book"),
    path('testimonial/',views.testimonial,name="testimonial"),
    path('manager/',views.manager,name="manager"),
    path('manform/',views.manform,name = "manform"),
    path('manprofile/',views.manprofile,name = "manprofile"),

    path('category_list/',views.category_list,name="category_list"),   
    path('user/',views.user,name="user"),   
    path('prodlist/',views.product_list,name="prodlist"),
    path('menuview/',views.menu_view,name="menuview"),
    path('addcart/<int:id>/',views.addCart, name='addcart'),
    path('order_list/',views.order_view,name='order_list'),
    path('comment/',views.comment,name = "comment"),
    path('ordersum/',views.ordersum,name = "ordersum"),


    
    path('delete/<int:id>/',views.deletedata,name="delete"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
