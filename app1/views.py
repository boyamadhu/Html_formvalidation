from django.shortcuts import render
from app1.forms import *
from app1.models import *
# Create your views here.

def topic_(request):
    TO=topic_form()
    d={'TO':TO}
    if request.method=='POST':
        TO1=topic_form(request.POST)
        if TO1.is_valid():
            tn=TO1.cleaned_data['topic_name']
            TO2=topic.objects.get_or_create(topic_name=tn)[0]
            TO2.save()
            d1={'topic':topic.objects.all()}
            return render(request,'display_topic.html',d1)
    return render(request,'topic_.html',d)