from django.shortcuts import render,redirect,get_object_or_404
from .models import Dish,Orders
from .forms import DishForm,OrderForm

# Create your views here.
def listAllDishes(request):
    alldishes= Dish.objects.all()
    context= {'alldishes':alldishes}
    return render(request,"dish_list.html",context)

def addDish(request):
    if request.method=='POST':
        form= DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menuapp:dishesList')
    else:
        form= DishForm()
        return render(request,'create_dish.html',{'form':form})  


def updateDish(request,dish_id):
    dish= get_object_or_404(Dish,pk=dish_id)
    form=None
    if request.method=='POST':
        form= DishForm(request.POST,instance=dish)
        if form.is_valid():
            form.save()
            return redirect('menuapp:dishesList')
        
    else:
        form= DishForm(instance=dish)
    return render(request,'update_dish.html',{'form':form,'dish':dish})



   
def deleteDish(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)

    if request.method == 'POST':
        dish.delete()
        return redirect('menuapp:dishesList')  

    return render(request, 'confirm_delete.html', {'dish': dish})

       
def placeOrder(request):
    form=None
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            customer_name=form.cleaned_data['customer_name']
            selected_dishes=form.cleaned_data['dishes']
            order= Orders.objects.create(customer_name=customer_name)
            order.dishes.set(selected_dishes)
            return redirect('menuapp:dishesList')  
    else:
        form= OrderForm()

    return  render(request,'placeOrder.html',{'form':form})


def showAllOrders(request):
    orders= Orders.objects.all()
    return render(request,'orderList.html',{'orders':orders})
       


