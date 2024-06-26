from django import forms
from crm.models import Empolyees
from django.contrib.auth.models import User

class EmpolyeeForm(forms.Form):
    name=forms.CharField()
    department=forms.CharField()
    salary=forms.IntegerField()
    email=forms.EmailField()
    contact=forms.CharField()
    age=forms.IntegerField()


    #  or 


class EmpolyeeModelForm(forms.ModelForm):
    class Meta:
        model=Empolyees
        fields="__all__"

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "department":forms.TextInput(attrs={"class":"form-control"}),
            "salary":forms.NumberInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "age":forms.NumberInput(attrs={"class":"form-control"}),
            "contact":forms.Textarea(attrs={"class":"form-control","rows":9}),
            "dob":forms.DateInput(attrs={"class":"form-control","type":"date"})
        }

class RegistrationForm(forms.ModelForm):

    class Meta:
        model=User
        fields=["username","email","password"]

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    








   

