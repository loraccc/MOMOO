from django.shortcuts import render,redirect
from .models import ContactMessage
# Create your views here.


# def home(request):
#     return render(request,'index.html')



def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        message = ContactMessage(name=name, email=email, comment=comment)
        message.save()

        return redirect("index/")  # Redirect to a success page
    else:
        return render(request,'index.html')
