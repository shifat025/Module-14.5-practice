from django.shortcuts import render,redirect
from .Form import ExampleForm

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # form.save()
            print(form.cleaned_data)
		
    else:
        form = ExampleForm()
    return render(request, 'form.html',{'form':form})