from django.shortcuts import render
import datetime

# Create your views here.
def display_view(request):
    date=datetime.datetime.now()
    my_dict={'insert_date':date}
    return render(request,'testapp/wish.html',context=my_dict)
