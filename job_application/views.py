from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ApplicationForm
from .models import Form
from django.core.mail import EmailMessage

def index(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            date = form.cleaned_data.get('date')
            occupation = form.cleaned_data.get('occupation')

            Form.objects.create(
                first_Name=first_name,
                last_Name=last_name,
                email=email,
                date=date,
                occupation=occupation
            )

            messages.success(request, f"Thank you {first_name}! Your application has been submitted successfully.")

            # Send email notification
            try:
                email_message = EmailMessage(
                    "Form Submission Confirmation",
                    f"Thank you {first_name}! Your application has been submitted successfully.",
                    to=[email]
                )
                email_message.send()
            except Exception as e:
                # Log the error but don't stop the form submission
                print(f"Email sending failed: {e}")
            
            return redirect('index')
    else:
        form = ApplicationForm()
            
    return render(request, 'index.html', {'form': form})


def about(request): 
    return render(request, 'about.html')
