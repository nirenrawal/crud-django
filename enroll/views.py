from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt


def home(request):
    form = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/home.html', {'form': form, 'stud':stud})

# Create your views here.
# @csrf_exempt
def save_data(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            sid = request.POST['stuid']
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if(sid == ""):
                user = User(name = name, email = email, password = password)
            else:
                user = User(id = sid, name = name, email = email, password = password)
            user.save()
            stud = User.objects.values()
            # print(stud)
            student_data = list(stud)
           
            return JsonResponse({'status':'Save', 'student_data':student_data})
        else:
            return JsonResponse({'status': 0})
        
        
def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        # print(id)
        pi = User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})
    
    

def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        student = User.objects.get(pk=id)
        studetn_data = {"id":student.id, "name":student.name, "email":student.email, "password":student.password}
        return JsonResponse(studetn_data)