from django.shortcuts import render, redirect
from .forms import PatientForm ,PrescriptionForm
from .models import Patient
from django.contrib import messages

# Create your views here.

def patient_home(request):
    return render(request, "patient_register/patient_home.html")

def patient_list(request):
    context = {"patient_list" : Patient.objects.all()} 
    return render(request, "patient_register/patient_list.html",context)

def patient_form(request, id=0):
    if request.method == "GET":
        if id==0:    
            form = PatientForm()
        else:
            patient = Patient.objects.get(pk=id)
            form = PatientForm(instance=patient)    
        return render(request, "patient_register/patient_form.html",{'form':form})
    else:
        if id == 0:
            form = PatientForm(request.POST)
        else:
            patient = Patient.objects.get(pk=id)
            form = PatientForm(request.POST, instance=patient)  
        if form.is_valid():
            form.save()
        return redirect('/list')

def patient_delete(request,id):
    patient = Patient.objects.get(pk=id)
    patient.delete()
    return redirect('/list')

def patient_prescription(request, id=0):
    if request.method == "GET":
        if id==0:    
            form = PrescriptionForm()
        else:
            prescription = Prescription.objects.get(pk=id)
            form = PrescriptionForm(instance=prescription)    
        return render(request, "patient_register/patient_prescription.html",{'form':form})
    else:
        if id == 0:
            form = PrescriptionForm(request.POST)
        else:
            prescription = Prescription.objects.get(pk=id)
            form = PrescriptionForm(request.POST, instance=prescription)  
        if form.is_valid():
            form.save()
            messages.success(request, 'Prescription saved successfully.')
        return redirect('/list')