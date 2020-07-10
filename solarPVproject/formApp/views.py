from django.shortcuts import render
from formApp.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')


# Adding new records to DB
def insertRecord(request):
    if request.method == 'POST':
        if request.POST.get('username'):
            saverecord = User()
            saverecord.Username = request.POST.get('username', '')
            saverecord.First_Name = request.POST.get('firstName', '')
            saverecord.Middle_Initial = request.POST.get('middleInitial', '')
            saverecord.Last_Name = request.POST.get('lastName', '')
            saverecord.Email = request.POST.get('email', '')
            saverecord.Gender = request.POST.get('gender', '')
            saverecord.Street_Address = request.POST.get('streetAddress', '')
            saverecord.City = request.POST.get('city', '')
            saverecord.US_State = request.POST.get('uSState', '')
            saverecord.Zipcode = request.POST.get('zipcode', '')
            saverecord.Phone_Number = request.POST.get('phoneNumber', '')
            saverecord.Company = request.POST.get('company', '')
            saverecord.save()

            messages.success(request, 'Record Saved Successfully...')
            return render(request, 'signup.html')
        else:
            return render(request, 'signup.html')