from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                subject=f"Contact Form Submission from {name}",
                message=message,
                from_email=email,  # User's email
                recipient_list=['your_email@example.com'],  # Replace with your email
                fail_silently=False,
            )
            return HttpResponseRedirect('/success/')  # Redirect after successful submission
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})
