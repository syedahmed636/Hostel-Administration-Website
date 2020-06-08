from django.shortcuts import render ,redirect
from .models import Datadd, Datadds
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages

# Create your views here.
#Student
def add(request):
    if request.method=='POST':
        Name = request.POST['Name']
        ID = request.POST['Id']
        Year = request.POST['Year']
        Dept = request.POST['Dept']
        Mbno = request.POST['Mbno']
        Gender = request.POST['Gender']
        Gmail = request.POST['Gmail']
        Roomalloted = request.POST['Roomalloted']
        Fees = request.POST['Fees']
        Academicyear = request.POST['Academicyear']
        Parent_Mbno= request.POST['Mb2']
        Caution_Deposit = request.POST['Cd']
        if (Mbno==Parent_Mbno):
            messages.info(request, 'Mobile Number should be unique..')
            return redirect('add')

        elif Datadd.objects.filter(ID = ID).exists():
            messages.info(request, 'Data With this I.D already exists..')
            return redirect('add')
        else:
            data = Datadd(Name = Name,ID = ID,Year = Year,Dept = Dept,
                          Mbno = Mbno,Gender = Gender,Gmail = Gmail,Roomalloted = Roomalloted,
                          AmountPaid = Fees,Academicyear = Academicyear,ParentMbno = Parent_Mbno,CautionDeposit = Caution_Deposit )
            data.save()
            messages.info(request, 'Data Inserted Successfully..:)')
            return redirect('add')
    else:
        return render(request,'add.html')

def fetch(request):
    dta = Datadd.objects.all()
    if dta:
        if request.method=='POST':
            data=request.POST['search']

            if data:
                dt = Datadd.objects.filter(Q(ID__iexact=data))
                if dt:
                    return render(request,'fetch.html',{'data':dt})
                else:
                    messages.info(request, "No Record With this I.D exists..:)" )
                    return redirect('fetch')
        else:
            return render(request,'fetch.html')
    else:
        messages.info(request, "Data has not yet inserted..:)")
        return redirect('student')

def update(request,id):
        student = Datadd.objects.get(ID = id)

        if request.method == "POST":
            student.Name = request.POST['Name']
            student.ID = request.POST['Id']
            student.Year = request.POST['Year']
            student.Dept = request.POST['Dept']
            student.Mbno = request.POST['Mbno']
            student.Gender = request.POST['Gender']
            student.Gmail = request.POST['Gmail']
            student.Roomalloted = request.POST['Roomalloted']
            student.AmountPaid = request.POST['AmountPaid']
            student.Academicyear = request.POST['Academicyear']
            student.ParentMbno = request.POST['ParentMbno']
            student.CautionDeposit = request.POST['CautionDeposit']
            if (student.Mbno == student.ParentMbno):
                messages.info(request, 'Mobile Number should not to be the same..')
                return render(request, 'update.html', {'student': student})
            else:
                student.save()
                messages.info(request, 'Successfully Updated..')
                return redirect('fetch')
        return render(request, 'update.html', {'student': student})

def delete(request,id):
    student = Datadd.objects.get(ID=id)
    student.delete()
    messages.info(request, 'Deleted the Record of the given I.D')
    return redirect('fetch')

def completedata(request):
        data=Datadd.objects.all()
        if data:
            data= Datadd.objects.all()
            return render(request, 'comdt.html' ,{'data':data})
        else:
            messages.info(request, "Data has not yet inserted..:)")
            return redirect('student')

def toupdate(request, id):
        student = Datadd.objects.get(ID=id)

        if request.method == "POST":
            student.Name = request.POST['Name']
            student.ID = request.POST['Id']
            student.Year = request.POST['Year']
            student.Dept = request.POST['Dept']
            student.Mbno = request.POST['Mbno']
            student.Gender = request.POST['Gender']
            student.Gmail = request.POST['Gmail']
            student.Roomalloted = request.POST['Roomalloted']
            student.AmountPaid = request.POST['AmountPaid']
            student.Academicyear = request.POST['Academicyear']
            student.ParentMbno = request.POST['ParentMbno']
            student.CautionDeposit = request.POST['CautionDeposit']
            if (student.Mbno == student.ParentMbno):
                messages.info(request, 'Mobile Number should not to be the same..')
                return render(request, 'update.html', {'student': student})
            else:
                student.save()
                messages.info(request, 'Successfully Updated..')
                return redirect('completedata')
        return render(request, 'update.html', {'student': student})

def todelete(request,id):
    student = Datadd.objects.get(ID=id)
    student.delete()
    messages.info(request, 'Deleted the Record of the given I.D')
    return redirect('completedata')

#Staff

def toadd(request):
    if request.method=='POST':
        Name = request.POST['Name']
        ID = request.POST['ID']
        Age = request.POST['Age']
        Gender = request.POST['Gender']
        Mbno = request.POST['Mbno']
        Gmail = request.POST['Gmail']
        Address = request.POST['Address']
        AlternateContact = request.POST['Alternate_ContactNum']
        Designation = request.POST['Designation']
        Salary = request.POST['Salary']
        if (Mbno == AlternateContact):
            messages.info(request, 'Mobile Number should be unique..')
            return redirect('toadd')
        elif Datadd.objects.filter(ID = ID).exists():
            messages.info(request, 'Data With this I.D already exists..')
            return redirect('toadd')
        else:
            data = Datadds(Name=Name, ID=ID, Age=Age, Mbno=Mbno, Gender=Gender, Gmail=Gmail, Address=Address, Alternate_ContactNum=AlternateContact,
                       Designation = Designation, Salary = Salary)
            data.save()
            messages.info(request, 'Data Inserted Successfully..:)')
            return redirect('toadd')
    else:
        return render(request,'toadd.html')

def tofetch(request):
    dta = Datadds.objects.all()
    if dta:
        if request.method == 'POST':
            data = request.POST['search']

            if data:
                dt = Datadds.objects.filter(Q(ID__iexact=data))
                if dt:
                    return render(request, 'tofetch.html', {'data': dt})
                else:
                    messages.info(request, "No Record With this I.D exists..:)")
                    return redirect('tofetch')
        else:
            return render(request, 'tofetch.html')
    else:
        messages.info(request, "Data has not yet inserted..:)")
        return redirect('staff')

def updatestaff(request,id):
    staff = Datadds.objects.get(ID=id)

    if request.method == "POST":
            staff.Name = request.POST['Name']
            staff.ID = request.POST['ID']
            staff.Age = request.POST['Age']
            staff.Gender = request.POST['Gender']
            staff.Mbno = request.POST['Mbno']
            staff.Gmail = request.POST['Gmail']
            staff.Address = request.POST['Address']
            staff.Alternate_ContactNum = request.POST['Alternate_ContactNum']
            staff.Designation = request.POST['Designation']
            staff.Salary = request.POST['Salary']
            if (staff.Mbno == staff.Alternate_ContactNum):
                messages.info(request, 'Mobile Number should not to be the same..')
                return render(request, 'updatestaff.html', {'staff': staff})
            else:
                staff.save()
                messages.info(request, 'Successfully Updated..')
                return redirect('tofetch')
    return render(request, 'updatestaff.html', {'staff': staff})

def deletestaff(request,id):
    staff = Datadds.objects.get(ID=id)
    staff.delete()
    messages.info(request, 'Deleted the Record of the given I.D')
    return redirect('tofetch')

def tocompletedata(request):
        data = Datadds.objects.all()
        if data:
            data = Datadds.objects.all()
            return render(request, 'comdtt.html', {'data': data})
        else:
            messages.info(request, "Data has not yet inserted..:)")
            return redirect('staff')

def toupdatestaff(request, id):
        staff = Datadds.objects.get(ID=id)

        if request.method == "POST":
            staff.Name = request.POST['Name']
            staff.ID = request.POST['ID']
            staff.Age = request.POST['Age']
            staff.Gender = request.POST['Gender']
            staff.Mbno = request.POST['Mbno']
            staff.Gmail = request.POST['Gmail']
            staff.Address = request.POST['Address']
            staff.Alternate_ContactNum = request.POST['Alternate_ContactNum']
            staff.Designation = request.POST['Designation']
            staff.Salary = request.POST['Salary']
            if (staff.Mbno == staff.Alternate_ContactNum):
                messages.info(request, 'Mobile Number should not to be the same..')
                return render(request, 'updatestaff.html', {'staff': staff})
            else:
                staff.save()
                messages.info(request, 'Successfully Updated..')
                return redirect('tocompletedata')
        return render(request, 'updatestaff.html', {'staff': staff})

def todeletestaff(request,id):
    staff = Datadds.objects.get(ID=id)
    staff.delete()
    messages.info(request, 'Deleted the Record of the given I.D')
    return redirect('tocompletedata')








