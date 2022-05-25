from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, DetailView, TemplateView, ListView

from .models import Patient, Record


class PatientCreateView(CreateView):
    model = Patient
    template_name = 'main/patient-create.html'
    fields = ['name', 'email', 'biography']


class PatientDetailView(CreateView):
    model = Record
    fields = ['details', 'patient', 'doctor']
    template_name = 'main/patient-detail.html'

    def get_context_data(self, **kwargs):
        context = super(PatientDetailView, self).get_context_data(**kwargs)

        patient = Patient.objects.get(id=self.kwargs['pk'])
        context['patient'] = patient
        context['record_list'] = Record.objects.filter(patient=patient)
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.patient = Patient.objects.get(id=self.kwargs['pk'])
        obj.doctor = self.request.user
        form.save()
        return render(self.request, self.template_name, self.get_context_data())


class IndexTemplateView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['patients'] = Patient.objects.all()
        return context


class SearchResultsView(ListView):
    model = Patient
    template_name = 'main/search_results.html'

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data()
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Patient.objects.filter(
            Q(name__icontains=query)
        )
        return object_list


class AddToMyPatientsView(View):
    def get(self, request, pk):
        patient = Patient.objects.get(id=pk)
        user = request.user
        user.my_patients.add(patient)
        return redirect('patient-detail', pk=patient.id)

