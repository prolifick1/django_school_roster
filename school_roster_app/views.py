from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import School

my_school = School('Django School')

def index(request):
    my_data = {
            "school_name" : my_school.name
        }
    return render(request, "pages/index.html", my_data)

def list_staff(request):
    staff_data = {
            "all_students" : my_school.staff
        }
    return render(request, "pages/list_staff.html", staff_data)

def staff_detail(request, employee_id):
    staff_data = {
            'staff': School.find_staff_by_id(my_school, employee_id)
            }
    return render(request, 'pages/staff_detail.html', staff_data)


def list_students(request):
    pass # implement


def student_detail(request, student_id):
    pass # implement
