from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from django.contrib import messages
from .models import User

def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            #fm.save() --> 1st way to save the data in database.
            '''reg=User(name=fm.cleaned_data['name'], email=fm.cleaned_data['email'], password=fm.cleaned_data['password'])
            reg.save()''' #--> 2nd way to save the data in database.
            User.objects.create(name=fm.cleaned_data['name'], email=fm.cleaned_data['email'], password=fm.cleaned_data['password'])
            fm=StudentRegistration()
            messages.add_message(request, messages.SUCCESS, 'Your data successfully submited !!!') 
    else: 
        fm=StudentRegistration()
    stu = User.objects.all()        
    return render(request, 'enroll/addandupdate.html', {'Form':fm, 'studetails': stu})

def delete_stu(request, pk):
    if request.method == "POST":
        stu= User.objects.get(id=pk)
        stu.delete()
        return HttpResponseRedirect('/')
    
def update_stu(request, pk):
    if request.method == "POST":
        stu=User.objects.get(id=pk)
        fm=StudentRegistration(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
        messages.info(request, 'Data successfully updated !!!')    
    else:
        stu=User.objects.get(id=pk)
        fm=StudentRegistration(instance=stu)        
    return render(request, 'enroll/update.html', {'form': fm})