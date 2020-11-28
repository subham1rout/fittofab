from django import forms
from heartrates.models import HeartrateReading
import serial


POSITION=[
    ('idle','Idle'),
    ('talking','Talking'),
    ('walking','Walking')
]

class HearttestForm(forms.ModelForm):
    position = forms.CharField(widget=forms.HiddenInput(),initial='Idle') 
    print('Arduino work')
    ard=serial.Serial('COM3',9600)
    print('success',ard)
    dat=ard.readline().decode('ascii')
    ad=int(dat)
    print('data=',ad,type(ad))
    heartrate=forms.IntegerField(widget=forms.HiddenInput(),initial=ad)
    

    class Meta:
        model=HeartrateReading
        fields=('heartrate','position')
