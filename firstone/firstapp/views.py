from django.shortcuts import render
from .models import Chaivariety,stores
from django.shortcuts import get_object_or_404
from .forms import chaiform
# Create your views here.



# for frontend part here is we do getting request from database
def all(request):
    chais=Chaivariety.objects.all()
    return render(request,'firstapp/all.html',{'chais':chais})

def details(request,chai_id):
    chai=get_object_or_404(Chaivariety,pk=chai_id)
    return render(request,'firstapp/details.html',{'chai':chai})


#in django we write first the post method and in this also we check the correct value given acc to field type
def chai_store(request):
    storess=None
    if request.method == 'POST':
        form=chaiform(request.POST)
        if form.is_valid():
           chai_var= form.cleaned_data['your_chai_variety']
           storess=stores.objects.filter(chai_variety=chai_var)
    else:
        form=chaiform()       



    return render(request,'firstapp/stores.html',{'storess':storess,'form':form})