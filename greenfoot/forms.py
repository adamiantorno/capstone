from django import forms


from .models import Vehicle, Profile, User

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'name',
            'style'
        ]

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(placeholder="ex. ''Dad's Cadillac''")
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'  


class TravelForm(forms.Form):
    distance = forms.IntegerField(label="Distance Travlled (km)", min_value=0, required=True)
    vehicle = forms.ModelChoiceField(
        queryset=None,
        label='Vehicle',
        empty_label='Add New Vehicle'
    )

    def __init__(self, current_user, *args, **kwargs):
        super(TravelForm, self).__init__(*args, **kwargs)
        self.fields['vehicle'].queryset = Vehicle.objects.filter(profile=Profile.objects.get(user=current_user))
        self.fields['vehicle'].widget.attrs['id'] = 'vehicles'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'  
        
