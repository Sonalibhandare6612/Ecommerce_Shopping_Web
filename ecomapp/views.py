from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Property, Tenant, Unit, Contact


def home(request):
    return render(request, "index.html")


# Login view
# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('property_list')
#         else:
#             messages.error(request, 'Invalid email or password.')
#     return render(request, 'login.html')

@login_required
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

@login_required
def property_detail(request, pk):
    property = Property.objects.get(pk=pk)
    return render(request, 'property_detail.html', {'property': property})

@login_required
def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenant_list.html', {'tenants': tenants})

@login_required
def tenant_detail(request, pk):
    tenant = Tenant.objects.get(pk=pk)
    return render(request, 'tenant_detail.html', {'tenant': tenant})




def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        pnumber=request.POST.get('pnumber')
        
        myquery=Contact(name=name, email=email,desc=desc, phonenumber=pnumber)
        myquery.save()
        messages.info(request, "We will get back to you soon")
        return render(request, "contact.html")
        
        
    return render(request, "contact.html")



def about(request):
    
    return render(request, "about.html")



# from django.shortcuts import redirect, render
# from ecomapp.models import Contact, Product, Orders, OrderUpdate
# from django.contrib import messages
# from math import ceil
# from ecomapp import keys
# from django.conf import settings
# MERCHANT_KEY=keys.MK
# import json
# from django.views.decorators.csrf import csrf_exempt
# #from PayTm import Checksum

# # Create your views here.
# def index(request):
#     allprods = []
#     catprods = Product.objects.values('category', 'id')
#     cats = {item['category'] for item in catprods}
#     for cat in cats:
#         prod = Product.objects.filter(category=cat)
#         n = len(prod)
#         nSlides = n // 4 + ceil((n / 4) - (n // 4))
#         allprods.append([prod, range(1, nSlides), nSlides])
        
#     params = {'allProds' : allprods}    
    
#     return render(request, "index.html", params)




# def checkout(request):
#     if not request.user.is_authenticated:
#         messages.warning(request, "Please login & tey again")
#         return redirect('/authapp/login')
    
    
#     if request.method == "POST":
#         item_json = request.POST.get('itemJson', '')
#         name = request.POST.get('name', '')
#         amount = request.POST.get('amt', '')
#         email = request.POST.get('email', '')
#         address1 = request.POST.get('address1', '')
#         address2 = request.POST.get('address2', '')
#         city = request.POST.get('city', '')
#         state = request.POST.get('state', '')
#         zip_code = request.POST.get('zip_code', '')
#         phone = request.POST.get('phone', '')
#         Order = Orders(items_json=item_json, name=name, amount=amount, email=email,address1=address1, address2=address2, city=city, state=state, zip_code=zip_code, phone=phone)
#         Order.save()
#         update = OrderUpdate(order_id = Order.order_id, update_desc = "Order has been placed")
#         update.save()
#         thank = True
        
        
        
# # Payment Integration         
        
#         id = Order.order_id
#         oid = str(id)+"shopycart"
#         param_dict = {
            
#             'MID' : keys.MID,
#             'ORDER_ID' : oid,
#             'TXN_AMOUNT' : str(amount),
#             'CUST_ID' : email,
#             'INDUSTRY_TYPE_ID' : 'Retail',
#             'WEBSITE' : 'WEBSTAGING',
#             'CHANNEL_ID' : 'WEB',
#             'CALLBACK_URL' : 'http://127.0.0.1:8000/handlerequest/',
               
#         }
#         # param_dict['CHECKSUMHASH'] = Checksum.generate_checksum
#         # (param_dict, MERCHANT_KEY)
#         # return render(request, 'pyttm.html', {'param_dict':
#         # param_dict})
        
#     return render(request, 'checkout.html')

# @csrf_exempt
# def handlerequest(request):
#     # paytm will send you post request here
#     form = request.POST
#     response_dict = {}
#     for i in form.keys():
#         response_dict[i] = form[i]
#         if i == 'CHECKSUMHASH':
#             Checksum = form[i]
            
#     verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, Checksum)
#     if verify:
#         if response_dict['RESPCODE'] == '01':
#             print('order successful')
#             a = response_dict['ORDERID']        
#             b = response_dict['TXNAMOUNT']
#             rid = a.replace("sshopycart", "")
            
#             print(rid)
#             filter2 = Orders.objects.filter(order_id = rid)
#             print(filter2)
#             print(a,b)
#             for post1 in filter2:
#                 post1.oid = a
#                 post1.amountpaid = b
#                 post1.paymentstatus = "PAID"
#                 post1.save()
#             print("run agede function")
            
#         else :
#             print("order was not successfull because" + response_dict['RESPCODE'])
#     return render(request, 'paymentstatus.html', {'response':response_dict})                        
        
        
         
        
