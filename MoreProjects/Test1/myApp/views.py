from django.shortcuts import render
from .forms import myForm
from .models import MyModel
# Create your views here.
def home_view(request):
   form = myForm()
   if request.method == "POST":
      form = myForm(request.POST)
      if form.is_valid():
         model = MyModel(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
         print(form.cleaned_data['password'])
         model.save()
      else:
         form = myForm()

   return render(request,"myApp/index.html",{'form':form})