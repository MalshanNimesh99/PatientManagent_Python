from django import forms
from .models import Patient , Prescription

class DateInput(forms.DateInput):
     input_type = 'date'

class PatientForm(forms.ModelForm):

    class Meta:
        widgets = {'birthday':DateInput()}
        model = Patient
        #fields = '__all__' 
        fields = ('fullname','mobile','pat_code', 'birthday')
        labels = {
            'fullname' : 'Full Name',
            'mobile' : 'Mobile',
            'pat_code' : 'Patient Code',
            'birthday' : 'Birthday'
        }

class PrescriptionForm(forms.ModelForm):

    class Meta:
        widgets = {'date':DateInput()}
        model = Prescription
        fields = ('fullname','mobile','pat_code','prescription','date')
        labels = {
            'fullname' : 'Full Name',
            'mobile' : 'Mobile',
            'pat_code' : 'Patient Code',
            'prescription' : 'Prescription',
            'date' : 'Date'
        }
        
        
    

        
    

