from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from .forms import *


def create_checklist(request):
    if request.method == 'POST':
        checklist_form = ChecklistForm(request.POST)
        if checklist_form.is_valid():
            checklist = checklist_form.save()
            task_formset = TaskFormSet(request.POST, instance=checklist)
            if task_formset.is_valid():
                task_formset.save()
                return HttpResponseRedirect(reverse('create_checklist'))
    else:
        checklist_form = ChecklistForm()
        task_formset = TaskFormSet(instance=Checklist())

    return render(request, 'checklist/create_checklist.html',
                  {'checklist_form': checklist_form, 'task_formset': task_formset})


def checklist(request):
    return render(request, 'checklist/checklist_service.html')


def checklist_service(request):
    return render(request, 'checklist/checklist_service.html')


def checklist_mall(request):
    return render(request, 'checklist/checklist_mall.html')


def checklist_plazma(request):
    return render(request, 'checklist/checklist_plazma.html')


def checklist_nagornoe(request):
    return render(request, 'checklist/checklist_nagornoe.html')
