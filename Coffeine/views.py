from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login


from django.contrib import messages
import random

# Create your views here.

from Coffeine.models import  categoryModel,messageModel,orderModel,userModel,productModel,AddtoCartModel,Manager,Wishlist
from Coffeine.forms import categoryform,messageform,orderform,userform,productform,Cartform,ManagerForm,WishlistForm

# Create your views here.


def sign(request):
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "signin":
            useremail = request.POST.get('user_email')
            userpassword = request.POST.get('password')

            try:
                user = userModel.objects.get(user_email=useremail)
                if user.password == userpassword:
                    # Store user ID in session
                    request.session['user_id'] = user.id
                    return redirect('home') 
                else:
                    print("Wrong password")
            except userModel.DoesNotExist:
                print("User does not exist")

        elif action == "signup":
            username = request.POST.get('username')
            useremail = request.POST.get('user_email')
            userpassword = request.POST.get('password')

            if userModel.objects.filter(user_email=useremail).exists():
                print("Email already exists")
            else:
                user = userModel(username=username, user_email=useremail, password=userpassword)
                user.save()
                print("Registration successful")
                context = {
                    'username' :username,
                    'user_email':useremail,
                    'password':userpassword,
                    'id':user.id
                }
                return render(request,"signinpage.html", context)

    return render(request, "signinpage.html")

def navibar(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('sign')
    try:
        user = userModel.objects.get(id=user_id)
    except userModel.DoesNotExist:
        return redirect('sign')
    context = {
        'user':user
    }
    return render(request,"navibar.html",context)

def login(request):
    if request.method == "POST":
        useremail = request.POST['email']
        userpassword = request.POST['password']
        if Manager.objects.filter(email = useremail).exists():
            manager = Manager.objects.get(email = useremail)
            
            print(manager)
            print(manager.password)
            if manager.password == userpassword:
                request.session['manager_id'] = manager.id
                return redirect("manager")
            else:
                print("Invalid Password")
    return render(request,"login.html")

def logout(request):
    request.session.flush()  # Clear all session data
    return redirect('sign')

def home(request):
    return render(request, "home.html")

def profile(request):
    user_id = request.session.get('user_id')
    user = userModel.objects.get(id=user_id)
    context = {
        'user':user
    }
    return render(request,"profile.html",context)

def register(request):
    user_id = request.session.get('user_id')
    user = userModel.objects.get(id=user_id)
    if request.method == "POST":
        form = userform(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = userform(instance=user)  
    return render(request, "register.html", {"form": form})

def aboutus(request):
    return render(request,"about.html")

def menu(request):
    products = productModel.objects.all()
    return render(request, 'menu.html',{"products":products})

def cart(request):
    user_id = request.session.get('user_id')   
    user = userModel.objects.get(id = user_id)

    cart_items = AddtoCartModel.objects.filter(user = user)
   
    context ={
        'cart_item' :cart_items,
        'user' :user
    }
    return render(request,"cart.html",context)

def addCart(request,id):
    user_id = request.session.get('user_id')   
    user = userModel.objects.get(id = user_id)
   
    if request.method == "POST":
        try:
            product = productModel.objects.get(id=id)
        except productModel.DoesNotExist:
            return render(request,"menu")
        
        qty = int(request.POST.get('quantity',1))

        cart_item, created = AddtoCartModel.objects.get_or_create(
            user=user,
            product=product,
            defaults={'quantity': qty}
        )

        try:
            cart_item =AddtoCartModel.objects.get(user = user,product = product)
            cart_item.quantity += qty
            cart_item.save()
        except AddtoCartModel.DoesNotExist:
            cart_item = AddtoCartModel(user = user, product = product, quantity = qty)
            cart_item.save()


        products = productModel.objects.all()

        context = {
            'products' :products,
        }
    return render(request,"menu.html",context)

def add_wishlist(request,id):
    user_id = request.session.get('user_id')
    user = userModel.objects.get(id = user_id)
   
    if request.method == "POST":
        try:
            product = productModel.objects.get(id=id)
        except productModel.DoesNotExist:
            return render(request,"menu")
        
        wishlist_item, created = Wishlist.objects.get_or_create(
            user=user,
            product=product
        )
        if created:
            print("Product added to wishlist")
        else:
            print("Product is already in wishlist")

        # Fetch all products for the menu view
        products = productModel.objects.all()

        context = {
            'products': products,
            'user': user,
        }
        return render(request, "menu.html", context)
    return redirect('menu')

def wishlist(request):
    user_id = request.session.get('user_id')   
    user = userModel.objects.get(id = user_id)
    wishlist = Wishlist.objects.filter(user = user)
    context ={
        'user' : user,
        'wishlist':wishlist
    }
    return render(request,"wishlist.html",context)

def order(request):
    if request.method == "POST":
        products = productModel.objects.all()
        print(products)
        print(request.POST)

        form = orderform(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            user_id = request.session.get('user_id')
            if user_id:
                try:
                    user = userModel.objects.get(id=user_id)
                    order.user = user
                    order.save()
                    return redirect('menu')
                except userModel.DoesNotExist:
                    return render(request,"orderpage.html", {"form": form, "products": products})
            else:
                messages.error(request, "User not authenticated")
        else:
            print("not valid form")
            print(form.errors) 
            return render(request,"orderpage.html",{"form":form})
    else:
        form = orderform()
        products = productModel.objects.all() 
    return render(request,"orderpage.html",{"form":form,"products": products})

def contact(request):
    if request.method == "POST":
        form = messageform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully!")
            return redirect(f'{request.path}?scroll_to_form=true')
    else:
        form = messageform()
    
    return render(request, "contact.html", {'form': form})

def product(request):
    return render(request,"product.html")

def booking(request):
    return render(request,"booking.html")

def testimonial(request):
    return render(request,"testimonial.html")

def order_view(request):
    user_id = request.session.get('user_id')
    user = userModel.objects.get(id = user_id)
    orders = orderModel.objects.filter(user = user)
    
    print("User ID:", user_id)
    print("Orders Found:", orders)
    context ={
        'user' : user,
        'orders' : orders
    }
    return  render(request,"orderview.html",context)

def manager(request):
    manager_id = request.session.get('manager_id')

    if not manager_id:
        return redirect('login')

    manager = Manager.objects.get(id = manager_id)
    user_count = userModel.objects.count()
    category_count = categoryModel.objects.count()
    comment_count = messageModel.objects.count()
    order_count = orderModel.objects.count()
    product_count = productModel.objects.count()

    context = {
        'manager': manager,
        'user_count': user_count,
        'category_count': category_count,
        'comment_count': comment_count,
        'order_count': order_count,
        'product_count': product_count,

    }
    return render(request,"manager.html",context)

def manprofile(request):
    manager_id = request.session.get('manager_id')

    if not manager_id:
        return redirect('login')
    try:
        manager = Manager.objects.get(id = manager_id)
    except Manager.DoesNotExist:
        return redirect('login')
    context = {
        "manager" :manager
    }
    return render(request,"manprofile.html",context)

def manform(request):
    manager_id = request.session.get('manager_id')
    if not manager_id:
        return redirect('login')
    try:
        manager = Manager.objects.get(id = manager_id)
    except Manager.DoesNotExist:
        return redirect('login')

    if request.method == "POST":
        form = ManagerForm(request.POST, request.FILES, instance = manager)
        if form.is_valid():
            form.save()
            return redirect('manprofile')
    else:
        form = ManagerForm(instance=manager)  
    return render(request,"manform.html",{"form":form,"manager":manager})

def product_list(request):
    if request.method == "POST":
        form = productform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("prodlist")
    else:
        form = productform()

    products = productModel.objects.all()
    manager_id = request.session.get('manager_id')
    manager = Manager.objects.get(id = manager_id)
    context ={
        "form":form,
        "products":products,
        "manager":manager
    }
    
    return render(request, "prodlist.html",context)

def menu_view(request):
    manager_id = request.session.get('manager_id')
    manager = Manager.objects.get(id = manager_id)

    products = productModel.objects.all()
    return render(request, 'menuview.html',{"products":products,"manager":manager})

def category_list(request):
    if request.method == "POST":
        form = categoryform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("category_list")
        else:
            print(form.errors)
    else:   
        form = categoryform()
    categories = categoryModel.objects.all()
    manager_id = request.session.get('manager_id')
    manager = Manager.objects.get(id = manager_id)
    context = {
        "form":form,
        "categories":categories,
        "manager":manager
    }

    return render(request, "categories.html",context)

def user(request):
    manager_id = request.session.get('manager_id')
    manager = Manager.objects.get(id = manager_id)

    datas = userModel.objects.all()
    for data in datas:
        datas.random_number = random.randint(1,100)
    return render(request,"user.html",{"datas":datas,"manager":manager})

def comment(request):
    manager_id = request.session.get('manager_id')
    manager = Manager.objects.get(id = manager_id)

    reviews = messageModel.objects.all()
    for review in reviews:
        reviews.random_number = random.randint(1,100)
    return render(request,"comment.html",{"reviews":reviews,"manager":manager})

def ordersum(request):
    manager_id = request.session.get('manager_id')
    manager = Manager.objects.get(id = manager_id)

    orders = orderModel.objects.all()
    for order in orders:
        orders.random_number = random.randint(1,100)
    return render(request,"ordersum.html",{"orders":orders,"manager":manager})

def deletedata(request, id):
    if categoryModel.objects.filter(id=id).exists():
        categoryModel.objects.get(id=id).delete()
        return redirect('category_list')
    elif messageModel.objects.filter(id=id).exists():
        messageModel.objects.get(id=id).delete()
        return redirect('comment')
    elif orderModel.objects.filter(id=id).exists():
        orderModel.objects.get(id=id).delete()
        return redirect('ordersum')
    elif productModel.objects.filter(id=id).exists():
        productModel.objects.get(id=id).delete()
        return redirect('prodlist')
    elif AddtoCartModel.objects.filter(id=id).exists():
        AddtoCartModel.objects.get(id=id).delete()
        return redirect('cart')
    elif Wishlist.objects.filter(id=id).exists():
        Wishlist.objects.get(id=id).delete()
        return redirect('wishlist')
    else:
        pass
    return HttpResponse("No matching data found.") 





