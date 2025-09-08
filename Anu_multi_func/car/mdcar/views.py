from django.shortcuts import render
from mdcar.models  import Parts, Contact
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'mdcar/home.html')

def parts(request):
    # fetching data from database
    parts = Parts.objects.all()
    
    param = {
        'parts' : parts
    }

    return render(request, 'mdcar/parts.html', context=param)

def team(request):
    return render(request, 'mdcar/team.html')
    
def contact(request):
     if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')
        topic = request.POST.get('topic', '')
        
        if Contact.objects.filter(email=email, contact=contact).exists():
                messages.error(request, 'You have already sent a message! Please try in a different way.')
                return render(request, 'mdcar/contact.html')
        else:
            # Save the form data to the database
            # print(name, email, contact, subject, requirement)
            contact = Contact(name=name, email=email, contact=contact, topic=topic)
            contact.save()
            messages.error(request, 'Message has been sent successfuly.')
            return render(request, 'mdcar/contact.html') 
     return render(request, 'mdcar/contact.html')

def bts(request):
    return render(request, 'mdcar/bts.html')


def partsView(request):
    return render(request, 'mdcar/partsView.html')
