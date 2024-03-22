from django.shortcuts import render,redirect

# Create your views here.

from crm.forms import EmpolyeeForm,EmpolyeeModelForm,RegistrationForm,LoginForm
from django.views.generic import View
from crm.models import Empolyees
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator




def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper 




@method_decorator(signin_required,name="dispatch")
class EmpolyeeCreateView(View):
    def get(self,request,*args,**kwargs):
        form=EmpolyeeModelForm()
        return render(request,"emp_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=EmpolyeeModelForm(request.POST,files=request.FILES)
        if form.is_valid():
           form.save()
           messages.success(request,"new empolyee has been added")
         # Empolyees.objects.create(**form.cleaned_data)
           print("create")
           return render(request,"emp_add.html",{"form":form})
        else:
           messages.error(request,"failed to add new empolyee")
           return render(request,"emp_add.html",{"form":form})
        

        


@method_decorator(signin_required,name="dispatch")       
class EmpolyeeListView(View):
    def get(self,request,*args,**kwargs):
          qs=Empolyees.objects.all()
          departments=Empolyees.objects.all().values_list("department",flat=True).distinct()
          print(departments)
          if "department" in request.GET:
              dept=request.GET.get("department")
              qs=qs.filter(department__iexact=dept)
          return render(request,"emp_list.html",{"data":qs,"deptmnt":departments})
    
    def post(self,request,*args,**kwargs):
        name=request.POST.get("box")
        qs=Empolyees.objects.filter(name__icontains=name)
        return render(request,"emp_list.html",{"data":qs})
    
    

    
@method_decorator(signin_required,name="dispatch")
class EmpolyeeDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Empolyees.objects.get(id=id)
        return render(request,"emp_detail.html",{"data":qs})
    


    
@method_decorator(signin_required,name="dispatch")
class  EmpolyeeDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Empolyees.objects.get(id=id).delete()
        messages.success(request,"an empolyee has been deleted")
        return redirect("emp-all")
    



@method_decorator(signin_required,name="dispatch")
class EmpolyeeUpdateView(View):
    def get (self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Empolyees.objects.get(id=id)
        form=EmpolyeeModelForm(instance=obj)
        return render(request,"emp_update.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Empolyees.objects.get(id=id)
        form=EmpolyeeModelForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
           form.save()
           messages.success(request,"details of an empolyee updated")
           return redirect("emp-detail",pk=id)
        else:
           messages.error(request,"failed to update an empolyee")
           return render(request,"emp_update.html",{"form":form})
        

        
        
        
class SignupView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"created")
            return render(request,"register.html",{"form":form})
        else:
            messages.error(request,"failure")
            return render(request,"register.html",{"form":form})
        

        
class SigninView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            usr_name=form.cleaned_data.get("username")
            pswd=form.cleaned_data.get("password")
            # print(usr_name,pswd)
            usr_obj=authenticate(request,username=usr_name,password=pswd)
            if usr_obj:
                print("valid credential")
                login(request,usr_obj)
                print(request.user,"he is the user") 
                return redirect("emp-all")
            
        messages.error(request,"invalid credential")
        return render(request,"login.html",{"form":form})
    
    

@method_decorator(signin_required,name="dispatch")   
class SignoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")


    




    

        




    
        
    

            
        
        
        
    
