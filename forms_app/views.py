from django.shortcuts import render
from .forms import FormName
from .models import Feedback

def form_name_view(request):
    form=FormName()
    profile_pic_url = None

    if request.method == 'POST':
        form = FormName(request.POST, request.FILES)
        if form.is_valid():
            name=form.cleaned_data['name']
            email = form.cleaned_data['email']
            feedback = form.cleaned_data['feedback']
            profile_pic = form.cleaned_data.get('profile_pic')

            feedback_instance = Feedback.objects.create(
                name=name,
                email=email,
                feedback=feedback,
                profile_pic=profile_pic
            )
            if profile_pic:
                profile_pic_url = feedback_instance.profile_pic.url

            #print header and top line
            print("\n" + "=" * 50)
            print("User Form Submission".center(50))
            print("=" * 50)
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"feedback: {feedback}")
            if profile_pic:
                print(f"Profile Picture: {profile_pic_url}")
            print("=" * 50 + "\n")
            # iterate and print each field on a new line
            for field, value in form.cleaned_data.items():
                print(f"{field.capitalize()}: {value}")

            #print bottom line
            print("=" * 50 + "\n")

    return render(request, 'forms_app/forms_page.html', {
        'form': form,
        'profile_pic_url' : profile_pic_url
    })

# Create your views here.
