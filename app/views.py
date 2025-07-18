from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from datetime import datetime
 # Ensure your Student model is imported
import app
import random
import string
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from app.models import *
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
# Create your views here.
from datetime import datetime
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from datetime import datetime
# Administartor work:
from django.shortcuts import render, redirect
from .models import Adminstartor  # Ensure correct import

def home(request):
    message = ""

    if request.method == 'POST':
        email = str(request.POST.get("email", "")).strip()
        password = str(request.POST.get("password", "")).strip()

        try:
            adminstartor = Adminstartor.objects.get(email=email)

            if adminstartor.password == password:
                request.session['alogin'] = True
                request.session['id'] = adminstartor.id
                return redirect('admin_panel')  # Use quotes or reverse() here
            else:
                message = "Invalid password"
        except Adminstartor.DoesNotExist:
            message = 'Invalid email or password'
        except Exception as ex:
            message = f'Error: {str(ex)}'

    # For both GET or failed POST
    request.session['alogin'] = False
    return render(request, 'home/login.html', {'message': message})


def userlogout(request):
    request.session['alogin'] = False
    logout(request)  # Call the built-in logout function
    request.session.flush()  # Clear the session
    return redirect('home')  # Redirect to the login page


def admin_panel(request):
        if 'alogin' in request.session and request.session['alogin']:
            id = request.session.get('id')
            adminstartor = get_object_or_404(Adminstartor, id=id)
            return render(request, 'adminstartor/admin_dash.html',{'Adminstartor':adminstartor})

def admin_profile(request):
    if 'alogin' in request.session and request.session['alogin']:
        id = request.session.get('id')
        adminstartor = get_object_or_404(Adminstartor, id=id)
        return render(request, 'adminstartor/admin_profile.html',{'Adminstartor':adminstartor})


def update_admin_profile(request):
    try:
        message = ""
        adminstartor = get_object_or_404(Adminstartor, id=request.session.get('id'))  
        if 'alogin' in request.session and request.session['alogin']:
            if request.method == 'POST':
              try:

                adminstartor.name = request.POST.get('name', adminstartor.name)
                adminstartor.mobile = request.POST.get('mobile', adminstartor.mobile)
                adminstartor.email = request.POST.get("email", adminstartor.email)
                adminstartor.password = request.POST.get('password', adminstartor.password)
                adminstartor.role = request.POST.get('role', adminstartor.role)
                adminstartor.image = request.FILES.get('image', adminstartor.image)

                adminstartor.save()  # Save the updated instance
                message = 'Admin details updated successfully...'

              except Exception as ex:
                 message = 'An error occurred while updating the teacher details.'

           
            return render(request,'adminstartor/admin_update.html', {'Adminstartor': adminstartor, 'message': message})

       
        message = 'You need to be logged in to update your profile.'
        return render(request, 'adminstartor/admin_update.html', {'message': message, 'Adminstartor': adminstartor})

    except Exception as ex:
        print(ex) 

# Administartor work:


def add_college(request):
    try:
        if request.method == 'POST':
            college = College()  # Use consistent variable name

            # Auto-generate fields
            college.id = datetime.now().strftime('%d%m%y%I%M%S')
            college.password = generate_password()
            
            # Get data from form
            college.name = request.POST.get('name')
            college.code = request.POST.get('code')
            college.address = request.POST.get('address')
            college.state = request.POST.get('state')
            college.city = request.POST.get('city')
            college.pincode = request.POST.get('pincode')
            college.email = request.POST.get("email")
            college.mobile = request.POST.get('phone')
            college.affiliation = request.POST.get('affiliation')  
            college.principal = request.POST.get('principal')
            college.website = request.POST.get('website')
            #college.image = request.FILES.get('image', None)
            college.role = request.POST.get('role')  
            print("inside add_clg")
            try:
                college.save()
                print("clg save")
                branches = request.POST.getlist("branches[]")
                for branch_name in branches:
                    branch, created = Branch.objects.get_or_create(branch=branch_name)
                    print(branch)
                    college.branches.add(branch)

                return JsonResponse({'success': True})
            except Exception as e:
                print("Save failed:", e)
                
                return JsonResponse({'success': False, 'error': str(e)})
                return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)
            message = 'New colleage details added successfully...'
            #send_mail_user(college.email,college.password)
            return render(request, 'college/add_college.html', {'message': message})
        else:
            return render(request, 'college/add_college.html', {'message': " "})
    except Exception as ex:
        return render(request, 'college/add_college.html', {'message': ex})



def college_master(request):
    try:
        if 'alogin' in request.session and request.session['alogin']:
            if request.method == 'POST':
                id_ = str(request.POST.get('id')).strip()
                if 'delete' in request.POST:
                    college = College.objects.get(id=id_)
                    college.delete()
                elif 'change_status' in request.POST:
                    college = College.objects.get(id=id_)
                    if college.status=='1':
                        college.status ='0'
                    else:
                          college.status ='1'
                    college.save()
            college = College.objects.all()
        return render(request, 'college/college_master.html', {'colleges': college})

    except Exception as ex:
        print(ex)
        return render(request, 'college/college_master.html', {'message': ex})




def send_mail_user(mail, password):
    try:
        context = {}

        address = mail
        subject = 'Your LMS Credentials Are Here – Student ID & Password '
        message = f"""
    Dear Student,
    Welcome to LMS!

    Your Learning Management System (LMS) credentials have been created. Please find your login details below:

    - Student ID: {mail}
    - Password: {password}
    - LMS Portal Link:https://lms-4nfs.onrender.com/

    To ensure the security of your account, please log in as soon as possible and change your password.

    If you have any issues accessing your account, please contact support at lmssystem1011@gmail.com

    Best regards.
    """

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'

        else:
            context['result'] = 'All fields are required'

    except  Exception as ex:
        print(e)


# def reset(request):
#     try:
#         message = ""

#         if request.method == 'POST':
#             email = request.POST.get("email", "").strip().lower()
#             role = request.POST.get("role", "").strip().lower()

#             if not email or not role:
#                 return render(request, 'home/reset.html', {'message': "Email and Role are required."})

#             user = None
#             if role == 'admin':
#                  user = Admin.objects.filter(email__iexact=email).first()
#             elif role == 'teacher':
#                 user = Teacher.objects.filter(email__iexact=email).first()
#             elif role == 'student':
#                 user = Student.objects.filter(email__iexact=email).first()

#             if user:
#                 send_mail_user(user.email, user.password)
#                 message = "A password  has been sent to your email."
#             else:
#                 message = "Invalid username or role."

#         return render(request, 'home/reset.html', {'message': message})

#     except Exception as ex:
#         return render(request, 'home/reset.html', {'message': f"Error: {str(ex)}"})


def generate_password(length=8):
    letters_digits = string.ascii_letters + string.digits
    special_chars = '#$@'

    password = random.choices(letters_digits, k=length - 1) + [random.choice(special_chars)]
    random.shuffle(password)

    return ''.join(password)


def add_subject(request):
    message=""
    try:
        if 'alogin' in request.session and request.session['alogin']:
            if request.method == 'POST':
                try:
                    university = request.POST.get('university')
                    branch_names = request.POST.getlist('branch_name[]')

                    year = request.POST.get('year')
                    semester = request.POST.get('semester')
                    
                    subject_names = request.POST.getlist('subject_name[]')
                    subject_codes = request.POST.getlist('subject_code[]')

                    for b_name in branch_names:
                        branch = Branch()
                        branch.id = datetime.now().strftime('%d%m%y%I%M%S%f')  # Unique ID
                        branch.university = university
                        branch.branch = b_name
                        existing_branch = Branch.objects.filter(branch=b_name, university=university).first()

                        if not existing_branch:
                            branch = Branch()
                            branch.id = datetime.now().strftime('%d%m%y%I%M%S%f')  # unique ID
                            branch.university = university
                            branch.branch = b_name
                            branch.save()

                    for name, code in zip(subject_names, subject_codes):
                            existing_subject = Subject.objects.filter( name=name, code=code,year=year, semester=semester ).first()
                    # Only save if not already present
                            if not existing_subject:
                                subject = Subject()
                                subject.id = datetime.now().strftime('%d%m%y%I%M%S%f')  # use microseconds for unique ID
                                subject.year = year
                                subject.semester = semester
                                subject.name = name
                                subject.code = code
                                subject.save()
                                
                                for branch_name in branch_names:
                                        try:
                                            branches = Branch.objects.filter(branch=branch_name, university=university)
                                            print(branch)
                                            for branch in branches:
                                                subject.branches.add(branch)

                                        except Branch.DoesNotExist:
                                            print(f"Branch with name '{branch_name}' not found for university '{university}'.")
                            else:
                                print(existing_subject)
                                for branch_name in branch_names:
                                        try:
                                            branches = Branch.objects.filter(branch=branch_name, university=university)
                                            print(branch)
                                            for branch in branches:
                                                existing_subject.branches.add(branch)

                                        except Branch.DoesNotExist:
                                            print(f"Branch with name '{branch_name}' not found for university '{university}'.")

                    message = 'Subjects added successfully.'
                except Exception as ex:
                    print(ex)
                    message = 'An error occurred while saving subjects.'       
            return render(request, 'subject/add_subject.html', {'message': message})
        
        message = 'You need to be logged in to update your profile.'
        return render(request, 'subject/add_subject.html', {'message': message})

    except Exception as ex:
        print(ex)
        return render(request, 'subject/add_subject.html', {'message': 'Unexpected error occurred.'})

def subject_master(request):
    try:
        if 'alogin' in request.session and request.session['alogin']:
            if request.method == 'POST':
                if 'action' in request.POST:
                    action = request.POST['action']
                    if action == 'Delete':
                        id_ = str(request.POST.get('id')).strip()
                        subject = Subject.objects.get(id=id_)
                        subject.delete()
                        return redirect('subject_master')  # Redirect after deletion
                    elif action == 'Update':
                        id_ = str(request.POST.get('id')).strip()
                        return redirect('update_subject', id=id_)  # Redirect to the update view
            subjects = Subject.objects.all()
            return render(request, 'subject/subject_master.html', {'subjects': subjects})

        message = 'You need to be logged in to update your profile.'
        return render(request, 'subject/subject_master.html', {'message': message})

    except Exception as ex:
        print(ex)
        return render(request, 'subject/subject_master.html', {'message': str(ex)})


def get_universities(request):
    try:
        print("Fetching universities...")

        # Get distinct universities from Subject table
        universities = Branch.objects.values_list('university', flat=True).distinct()

        university_list = list(universities)
        print("University List:", university_list)

        return JsonResponse(university_list, safe=False)
    except Exception as ex:
        print(f"Error in get_universities: {ex}")
        return JsonResponse({'error': str(ex)}, status=500)


def get_branches(request):
    try:
        print("branches")
        university = request.GET.get('university')
        if not university:
            return JsonResponse({'error': 'University not specified'}, status=400)

        print("branches")
        branches = Branch.objects.filter(university=university).values_list('branch', flat=True).distinct()

        return JsonResponse(list(branches), safe=False)
    except Exception as ex:
        return JsonResponse({'error': str(ex)}, status=500)