from django.shortcuts import render
from .forms import InputTextForm

def home_page(request):
    if request.method == "POST":
        to_translate_text = request.POST.get("text")
        return HttpResponse()
    else:
        input_form = InputTextForm()
        return render(request, 'home_page.html', {"inputform": input_form})
