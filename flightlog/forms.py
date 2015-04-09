from django.forms import ModelForm
from flightlog.models import Trip

class CreateTripForm(ModelForm):
    class Meta:         
        model = Trip
        fields = ['takeoff','landing','date_start','date_end']