from django.shortcuts import render , HttpResponseRedirect
from .models import SudentModel
from django.contrib import messages
from .forms import Sudent_data

# Create your views here.

def Create_Data(request):
   if request.method=='POST':
      fm=Sudent_data(request.POST)   
      if fm.is_valid():
         nm=fm.cleaned_data['name']
         em=fm.cleaned_data['email']
         ps=fm.cleaned_data['password']
         user=SudentModel(name=nm , email=em,  password=ps)
         user.save()
         messages.info(request , 'Submit Data SuccessFully!!')
         return HttpResponseRedirect('/')
         # fm=Sudent_data()
   else:
      fm = Sudent_data()
   stu=SudentModel.objects.all()
   return render(request , 'enroll/add.html', {'stu':stu , 'form':fm})         



def Delete_data(request , id):
   if request.method=='POST':
      pi=SudentModel.objects.get(pk=id)
      pi.delete()
      messages.info(request , 'Delete Data SuccessFully!!')
      return HttpResponseRedirect('/')



def Update_data(request , id):
     if request.method=='POST':
         pi=SudentModel.objects.get(pk=id)
         fm=Sudent_data(request.POST , instance=pi)
         if fm.is_valid():
            fm.save()
            messages.info(request , 'Update Data SuccessFully!!')
            fm=Sudent_data()

     else:
         pi=SudentModel.objects.get(pk=id)
         fm=Sudent_data(instance=pi)       
     return render(request, 'enroll/update.html', {'form':fm})
     