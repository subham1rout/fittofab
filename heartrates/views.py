from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from .forms import HearttestForm
import serial


def index(request):
    if request.method=="POST":
        age=int(request.POST["age"])
        if age>0 and age<220:
            heartrate=220-age
        else:
            heartrate=None
        args={'age':age,'heartrate':heartrate}
        return render(request,'heartrates/index.html',args)
    else:
        age=1
        heartrate=219
        args={'age':age,'heartrate':heartrate}
        return render(request,'heartrates/index.html',args)


class HearttestView(LoginRequiredMixin,TemplateView):
    template_name='heartrates/hearttest.html'

#     def get(self,request):
#         form=HearttestForm()
#         return render(request,self.template_name,{'form':form})

#     def post(self,request):
#         form=HearttestForm(request.POST)
#         if form.is_valid():
#             heartrate_reding = form.save(commit=False)
#             heartrate_reding.user=request.user
#             heartrate_reding.save()
#             heartrate=form.cleaned_data['heartrate']
#             position=form.cleaned_data['position']
#         args={'form':form,'heartrate':heartrate,'position':position}
#         return render(request,self.template_name,args)
        

@login_required
def lessons(request):
    return render(request,'heartrates/lessons.html')