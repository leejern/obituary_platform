from django.shortcuts import render, redirect
from .forms import ObituaryForm
from .models import Obituary
from datetime import datetime

def home(request):
    obituaries = Obituary.objects.all()
    context = {'obituaries': obituaries}
    return render(request, 'obituary_platform/home.html', context)

def create_obituary(request):
    if request.method == "POST":
        form = ObituaryForm(request.POST)
        if form.is_valid():
            obituary = form.save(commit=False)
            obituary.submission_date = datetime.now()
            obituary.save()
            return redirect('home')  # Assuming 'home' is the name of your home URL pattern
    else:
        form = ObituaryForm()
    
    context = {'form': form}
    return render(request, 'obituary_platform/obituary_form.html', context)


def obituary_info(request, slug):
    obituary = Obituary.objects.get(slug=slug)
    print(obituary)
    context = {'obituary': obituary}
    return render(request, 'obituary_platform/obituary_info.html', context)
# def obituary_list(request):
#     return render(request, 'obituary_platform/obituary_list.html') 


# def contact(request):
#     return render(request, 'obituary_platform/contact.html')

# def search(request):
#     return render(request, 'obituary_platform/search.html')

# def faq(request):
#     return render(request, 'obituary_platform/faq.html')


# def about(request):
#     return render(request, 'obituary_platform/about.html')