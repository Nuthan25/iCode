from django.shortcuts import render
from .models import contact
from .models import registration

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def course(request):
    return render(request,'courses.html')
def contact1(request):
    if request.method=="POST":
        cont=contact()
        cont.name=request.POST['name']
        cont.phoneno=request.POST['phone_no']
        cont.email=request.POST['email']
        cont.msg=request.POST['msg']
        cont.save()
    return render(request,'contact.html')
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phoneno = request.POST.get('phone_no')
        email = request.POST.get('email')
        c_programming = request.POST.get('c') == 'on'
        java = request.POST.get('java') == 'on'
        html_css = request.POST.get('html&css') == 'on'
        python = request.POST.get('python') == 'on'
        react_js = request.POST.get('react') == 'on'
        sql = request.POST.get('sql') == 'on'
        cpp = request.POST.get('cpp') == 'on'
        mongodb = request.POST.get('mongodb') == 'on'
        program_period = request.POST.get('period')
        card_number = request.POST.get('cno')
        cvv = request.POST.get('cvv')
        
        registration_obj = registration(
            name=name,
            phoneno=phoneno,
            email=email,
            c_programming=c_programming,
            java=java,
            html_css=html_css,
            python=python,
            react_js=react_js,
            sql=sql,
            cpp=cpp,
            mongodb=mongodb,
            program_period=program_period,
            card_number=card_number,
            cvv=cvv
        )
        
        registration_obj.save()
        
        # Perform any additional actions or redirect to a success page
        
    return render(request, 'registration.html')