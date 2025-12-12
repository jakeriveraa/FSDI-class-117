from django.shortcuts import render
from django.core.mail import send_mail
from .forms import contactForm
# Create your views here.

def about_view(request):
    return render(request, 'pages/about_me.html')

def experience_view(request):
    return render(request, 'pages/experience.html')


def contact_view(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            message_body = (
                f'You have a new email from your portfolio contact form\n'
                f'Name: {name}\n'
                f'Email: {email}\n'
                f'Message:\n{message}'
            )
            
            try:
                send_mail(
                    f'Portfolio Contact: {name}',
                    message_body,
                    email,
                    recipient_list=['jake.riveraa@gmail.com']
                    
                )
                form = contactForm()
                return render(request, 'pages/contact.html', {'form': form})
            except Exception as e:
                print(f'Error sending email: {e}')
                
                return render(request, 'pages/contact.html', {'form': form})
    else:
        form = contactForm()
    
        return render(request, 'pages/contact.html', {'form': form})

