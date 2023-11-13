from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Order,orderUpdate
from math import ceil
import json
# Create your views here.
def index(request):
    # param={}
    allprods=[]
    # product = Product.objects.all()
    # n=len(product)
    # print(product)
    # all productt are pass in the pages then its not a way to do
    prodcat= Product.objects.values('category', 'id')
    # print(prodcat)
    categ={item['category'] for item in prodcat}
    # print(categ)
    for identity in categ:
        prod_of_same_category=Product.objects.filter(category=identity)
        n=len(prod_of_same_category)
        nslides=n//4 +ceil(n/4-n//4)
        allprods.append([prod_of_same_category,range(1,nslides),nslides])
    params={'allprods':allprods}    
    # nslides=n//4 +ceil(n/4-n//4)
    # params={'products':product,'no_of_slides':nslides,'range':range(1,nslides)}
    return render(request,'shop/test.html',params)


def about(request):
    return render(request,'shop/about.html')    


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()  
    return render(request,'shop/contact.html')   


def tracker(request):
    if request.method=="POST":
        order_id=request.POST.get('orderId','')
        email=request.POST.get('email','')
        
        try:
            order=Order.objects.filter(order_id=order_id,email=email)
            if len(order)>0:
                update=orderUpdate.objects.filter(update_id=order_id)
                updates=[]
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request,'shop/tracker.html')   


def search(request):
    return render(request,'shop/search.html')   


def productView(request,myid):
    product=Product.objects.filter(id=myid)
    print(product[0])
    return render(request,'shop/productview.html',{'product':product[0]})   


def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name','')
        amount=request.POST.get('amount','')
        print(amount)
        email=request.POST.get('email','')
        address=request.POST.get('address1','')+""+request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        pincode=request.POST.get('pin','')
        phone=request.POST.get('phone','')
        order=Order(items_json= items_json,name=name,email=email,address=address,city=city,state=state,pincode=pincode,phone=phone,amount=amount)
        order.save()
        data=True
        id=order.order_id
        update=orderUpdate(update_id=order.order_id,update_desc="The order has been placed")
        update.save()
        return render(request,'shop/checkout.html',{'data':data,'id':id})  
    return render(request,'shop/checkout.html')     


def moreinfo(request):
    return render(request,'shop/moreinfo.html')    


def payment(request):
    return render(request,'shop/payment.html') 
     
     
        