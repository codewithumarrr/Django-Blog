from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'newsportalapp/index.html',{})


def Cnews_view(request):
    n1 = "today was a great day"
    n2 = 'torawari MNA zahor Khadukhel is fighting again for PTI'
    n3 = 'shahin shah is remarkably good with new ball'
    n4 = 'pakistan is going through a hard time'
    d  = {'n1':n1,'n2':n2,'n3':n3,'n4':n4}
    return render(request,'newsportalapp/cnews.html',d)

