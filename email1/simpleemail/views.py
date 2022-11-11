from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import ContactForm



def mail1(request):
    #https://www.youtube.com/watch?v=X7DWErkNVJs

    send_mail('my first mail app',
    'this app send message simply by opening  this view','abrhambelete.haile@gmail.com',['tomasbeyene21@gmail.com'],fail_silently=False)

    return render(request,'index.html')



def mail2(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('indexxx.html', {
                'name': name,
                'email': email,
                'content': content
            })

            send_mail('The contact form subject', content, 'abrhambelete.haile@gmail.com', [email], html_message=html)

            # return redirect('index.html')
    else:
        form = ContactForm()

    return render(request, 'indexx.html', {
        'form': form
    })