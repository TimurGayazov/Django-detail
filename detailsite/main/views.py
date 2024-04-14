from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *


def home_page(request):
    det_name = request.GET.get('name')
    det_color = request.GET.get('color')
    det_material = request.GET.get('material')
    if not det_name:
        det_name = ''
    if not det_color:
        det_color = ''
    if not det_material:
        det_material = ''

    if det_name or det_color or det_material:
        if det_name:
            det_name = det_name[0].upper() + det_name[1:].lower()
        if det_color:
            det_color = det_color[0].upper() + det_color[1:].lower()
        if det_material:
            det_material = det_material[0].upper() + det_material[1:].lower()
        details = Detail.objects.filter(detail_name__icontains=det_name, detail_color__icontains=det_color,
                                        detail_material__icontains=det_material)
    else:
        details = Detail.objects.all()
    context = {'details': details, 'det_name': det_name, 'det_color': det_color, 'det_material': det_material}
    return render(request, 'main/home.html', context)


def detail_page(request, pk):
    detail = Detail.objects.get(id=pk)
    context = {'detail': detail}
    return render(request, 'main/detail.html', context)


def create_detail(request):
    if request.method == 'POST':
        form = DetailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            pass

    form = DetailForm()
    data = {
        'form': form,
    }
    return render(request, 'main/create_detail.html', data)
