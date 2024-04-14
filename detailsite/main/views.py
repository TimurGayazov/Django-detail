from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import *
from .forms import *


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = LoginForm()
    if request.user.is_authenticated and request.user != 'AnonymousUser':
        return redirect("profile")
    else:
        return render(request, "main/login.html", {"form": form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


def profile(request):
    user = User.objects.get(id=request.user.id)
    context = {'user': user}
    return render(request, 'main/profile.html', context)


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


def delete_detail(request, pk):
    if request.user.is_authenticated:
        product = Detail.objects.get(id=pk)
        product.delete()
        return redirect('home')
    else:
        return redirect('home')


class UpdateDetail(UpdateView):
    model = Detail
    form_class = DetailForm
    template_name = 'main/update_detail.html'
    success_url = reverse_lazy("home")
