from django.shortcuts import render,redirect

# Create your views here.
data={
    "name":"Ankit",
    "age":24,
    "city":"Delhi"

}

def create(request):
        if request.method=="POST":
                key= request.POST.get("key")
                value=request.POST.get("value")
                data[key]=value
                return redirect("read")
        return render(request,"crud_op/create.html")


def read(request):
        return render(request,"crud_op/read.html",{"data":data})

def update(request):
        if request.method=="POST":
                key= request.POST.get("key")
                value=request.POST.get("value")
                if key in data:
                        data[key]=value
                return redirect("read")
        return render(request,"crud_op/update.html")


def delete(request):
        if request.method=="POST":
                key= request.POST.get("key")
                if key in data:
                        del data[key]
                return redirect("read")
        return render(request,"crud_op/delete.html")