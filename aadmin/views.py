from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def adminpanel(request):
    return render(request,'aadmin.html')

def adduser(request):
    if request.method == "POST":
        id = request.POST['id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email = request.POST['email']
        superuser = request.POST['superuser']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('adduser')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('adduser')
            elif User.objects.filter(id=id).exists():
                messages.info(request, 'Record with this I.D already Exists..:')
                return redirect('adduser')
            else:
                user = User.objects.create_user(id=id,username=username, password=pass2, email=email, first_name=first_name,
                                                last_name=last_name,is_superuser = superuser)
                user.save()
                messages.info(request, 'User Created')
                return redirect('adduser')
        else:
            messages.info(request, 'Password not matching..')
            return redirect('adduser')
    else:
        return render(request, 'adduser.html')

def fetchuser(request):
        data = User.objects.all()
        return render(request, 'fetchuser.html', {'data': data})

def updateuser(request,id):
    data = User.objects.get(id = id)
    if request.method == "POST":
            data.is_superuser = request.POST['superuser']
            data.first_name = request.POST['first_name']
            data.last_name = request.POST['last_name']
            data.save()
            messages.info(request, 'Successfully Updated..')
            return redirect('fetchuser')
    return render(request, 'updateuser.html', {'data': data})

def deleteuser(request, id):
    data = User.objects.get(id=id)
    data.delete()
    if request.user.is_authenticated:
        messages.info(request, 'Deleted the Record Successfully..:)')
        return redirect('fetchuser')
    else:
        return redirect('/')

def profile(request):
    return render(request,'profile.html')

def updateprofile(request,id):
    if request.method == "POST":
        data = User.objects.get(id=id)
        data.email = request.POST['email']
        data.first_name = request.POST['first_name']
        data.last_name = request.POST['last_name']
        data.save()
        messages.info(request, 'Successfully Updated..')
        return redirect('profile')
    return render(request,'updateprofile.html')

def deleteprofile(request,id):
    data = User.objects.get(id=id)
    data.delete()
    return redirect('/')