from django.urls import path
from . import views
app_name = 'menuapp'
urlpatterns=[
    path("add/",views.addDish,name="addDish"),
    path("update/<int:dish_id>",views.updateDish,name="updateDish"),
    path("read/",views.listAllDishes,name="dishesList"),
    path("delete/<int:dish_id>",views.deleteDish,name="deleteDish"),
    path("placeOrder/",views.placeOrder,name="placeOrder"),
    path("showOrders/",views.showAllOrders,name="showOrders")
]