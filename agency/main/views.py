from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .forms import UserRegisterForm, UserLoginForm, FilterRealEstate, FullFilterRealEstate, UserStayOwner, UserRequest, AddRealEstateForm
from .models import RealEstate, Buyer, Request, Owner, Image, Category, Area, Discount, Realtor
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.views.generic import CreateView
from django.core.files.base import ContentFile

def index(request):
    filter_re = FilterRealEstate()
    return render(request, 'main/index.html', {'context': 'context', 'filter_re': filter_re})


def add_new_estate(request):
    if request.method == 'GET':
        form = AddRealEstateForm()
        return render(request, 'main/add_new_estate.html', {'form': form})
    elif request.method == 'POST':
        owner = Owner.objects.get(user=request.user)
        form = AddRealEstateForm(request.POST)
        if form.is_valid():
            estate = RealEstate.objects.create(
                category=Category.objects.get(pk=int(form.cleaned_data['category'])),
                owner=owner,
                description=form.cleaned_data['description'],
                number_of_rooms=form.cleaned_data['number_of_rooms'],
                area=Area.objects.get(pk=int(form.cleaned_data['area'])),
                address=form.cleaned_data['address'],
                price=form.cleaned_data['price'],
                total_area=form.cleaned_data['total_area'],
                floor=form.cleaned_data['floor'],
                max_floor=form.cleaned_data['max_floor'],
                type_real_estate=form.cleaned_data['type_real_estate']
                )
            for f in request.FILES.getlist('photos'):
                data = f.read()
                photo = Image(img=f, real_estate=estate)
                photo.img.save(f'{f.name}{estate.pk}', ContentFile(data))
                photo.save()
            return redirect(estate)
        else:
            return render(request, 'main/add_new_estate.html', {'form': form})


def estate_detail(request, estate_id):
    estate = RealEstate.objects.get(pk=estate_id)
    price_for_meter = round(int(estate.price) / int(estate.total_area), 2)
    have_request = False
    user_have_request = estate.e_request.filter(real_estate=estate_id)
    if user_have_request.count() > 0:
        print(user_have_request[0].buyer.user)
        if user_have_request[0].buyer.user == request.user:
            have_request = True
    if request.POST:
        request_form = UserRequest(data=request.POST)
        if request_form.is_valid():
            # new_e_request = request_form.save(commit=False)
            new_buyer = Buyer(first_name=request.POST['first_name'], phone=request.POST['phone'], user=request.user)
            new_buyer.save()
            new_e_request = Request(real_estate=estate, buyer=new_buyer, request_status='Создана')
            new_e_request.save()
            messages.success(request, 'Заявка создана')
            return redirect(request.path)
    else:
        request_form = UserRequest()

    return render(request, 'main/estate_detail.html', {
        'estate': estate,
        'form': request_form,
        'price_for_meter': price_for_meter,
        'have_request': have_request})


def filtered_real_estate(request):
    if request.method == 'POST':
        params = request.POST
        estate = RealEstate.objects.filter(
            category=params['category']
            )
        if 'type_real_estate' in params and params['type_real_estate'] != '':
            estate = estate.filter(type_real_estate=params['type_real_estate'])
        if 'area' in params and params['area'] != '':
            estate = estate.filter(area=params['area'])    
        if 'price' in params and params['price'] != '':
            estate = estate.filter(price__lte=params['price'])
        if 'number_of_rooms' in params and params['number_of_rooms'] != '':
            estate = estate.filter(number_of_rooms=params['number_of_rooms'])
        if 'total_area' in params and params['total_area'] != '':
            estate = estate.filter(total_area=params['total_area'])
        sidefilter_form = FullFilterRealEstate(request.POST)

        # paginator = Paginator(estate, 2)
        # page_number = request.GET.get('page')
        # page_obj = paginator.get_page(page_number)

        return render(request, 'main/estate_list.html', {
            'estate_list': estate, 
            'sidefilter': sidefilter_form
            })


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна')
            return redirect('/')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')


def user_logout(request):
    logout(request)
    return redirect('/')


def user_get_owner_status(request):
    if request.method == 'POST':
        form = UserStayOwner(data=request.POST)
        if form.is_valid():
            owner_user = form.save(commit=False)
            owner_user.user = request.user
            owner_user.save()
            own = Group.objects.get(name='owners')
            request.user.groups.add(own)
            return redirect('/')
        else:
            messages.error(request, 'Ошибка подтверждения')
    else:
        form = UserStayOwner()
    return render(request, 'main/stay_owner.html', {'form': form})


def discount_list(request):
    discounts = Discount.objects.all()
    return render(request, 'main/discounts_list.html', {'disc_list': discounts})


def realtor_list(request):
    realtors = Realtor.objects.all()
    return render(request, 'main/realtor_list.html', {'realtor_list': realtors})
