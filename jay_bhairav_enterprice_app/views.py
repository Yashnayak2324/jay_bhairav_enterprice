import re
from django.shortcuts import render
from .models import *
from django.db.models import Q


# Create your views here.
data = {}
cat = Category.objects.all()
data['cat'] = cat

def index(request):
    prod_detail = Product_Details.objects.all().order_by("-id")
    data['prod_detail'] = prod_detail
    return render(request,'index.html',data)

def contact(request):

    if request.method == "POST":
        vName = request.POST['fname']
        vEmail = request.POST['femail']
        vPhone_No = request.POST['fphone_no']
        vMessage = request.POST['fmessage']
        if vName == " " or vEmail == " " or vPhone_No == " " or vMessage == " ":
            msg = "Plz Enter all the fields!"
            data['msg'] = msg
            print("1")
        else:
            print("2")
            Contact.objects.create(Name=vName,Email=vEmail,Phone_No=vPhone_No,Message=vMessage)
            msg="Your Requeste submited successfully!"
            data['msg'] = msg
        return render(request,'contact.html',data)
    else:
        return render(request,'contact.html',data)

def category(request):
    return render(request,"category.html",data)

def category1(request,pk):
    category = Category.objects.get(pk=pk)
    cat1 = category
    print(cat1)
    prod = Product_Details.objects.filter(Name=cat1)
    print(prod)
    data['prod'] = prod
    data['category'] = category
    return render(request,"category.html",data)

def Newsletter(request):
    if request.method == "POST":
        vemail = request.POST['femail']
        Subscribe.objects.create(Email=vemail)
        return render(request,'index.html',data)
    else:
        return render(request,'index.html',data)

def about(request):
    return render(request,'about.html',data)

def catlog(request):
    broucher = Catlog.objects.all()
    data['broucher'] = broucher
    return render(request,'catlog.html',data)

def search(request):
    if request.method == "POST":
        vsearch = request.POST['fsearch']
        data['search_name'] = vsearch
        search = Product_Details.objects.filter(Q(Title__contains=vsearch) | Q(Name__Category_Name__contains=vsearch))
        data['search'] = search
    return render(request,'search.html',data)