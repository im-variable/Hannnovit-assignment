from django import forms
from .models import Employee, City
from .validator import validate_age
from django.core.validators import RegexValidator


GENDER_CHOICES= [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ]


alphabet = RegexValidator(r'^[a-zA-Z ]*$', 'Only alphabets are allowed.')
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class EmployeeForm(forms.ModelForm):

    name= forms.CharField(validators=[alphabet])
    pan_number= forms.CharField(validators=[alphanumeric])
    age= forms.IntegerField(validators=[validate_age])
    gender= forms.CharField(label='Select your gender', widget=forms.Select(choices=GENDER_CHOICES))

    email = forms.EmailField()
    city = forms.ModelChoiceField(City.objects, required=True)
    class Meta:
        model = Employee
        fields = ['name', 'pan_number', 'age', 'gender', 'email', 'city']

    def clean_name(self):
        return self.cleaned_data.get('name', '').strip()