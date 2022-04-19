
from django.shortcuts import render,redirect
from . models import productdetails

def start(request):
    return render(request,'start.html')


def adding_emp(request):
    if request.method=='POST':
        ename=request.POST['employee_name']
        
        dobb=request.POST['dob']
        
        addrss=request.POST['address']
        mob=request.POST['mobile']
        email=request.POST['emaill']
        Gen=request.POST['Gend']
        Qual=request.POST['Quali']


        products=productdetails(employee_name=ename,
                                
                                dob=dobb,
                               
                                address=addrss,
                                mobile=mob,
                                emaill=email,
                                Gend=Gen,
                                Quali=Qual
                                )

        products.save()
        print("success")
        return redirect('show_emp')

def show_emp(request):
    prdcts=productdetails.objects.all()
    return render(request,'tab.html',{'products':prdcts}) 

def editpage(request,pk):
    prdcts=productdetails.objects.get(id=pk)
    return render(request, 'edit.html', {'products': prdcts})


def edit_pro_details(request,pk):
    if request.method=='POST':
        prdcts=productdetails.objects.get(id=pk)
        prdcts.employee_name=request.POST.get('employee_name')
        
        prdcts.dob=request.POST.get('dob')
        
        prdcts.address=request.POST.get('address')
        prdcts.mobile=request.POST.get('mobile')
        prdcts.emaill=request.POST.get('emaill')
        prdcts.Gend = request.POST.get('Gend')
        prdcts.Quali = request.POST.get('Quali')
        prdcts.save()
        return redirect('show_emp')
    return render(request,'edit.html')


def deletepage(request,pk):
    prdcts=productdetails.objects.get(id=pk)
    return render(request, 'delete.html', {'products': prdcts})

def delete_product(request,pk):
    prdcts=productdetails.objects.get(id=pk)
    prdcts.delete()
    return redirect('show_emp')




    