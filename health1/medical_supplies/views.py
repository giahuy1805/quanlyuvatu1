
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import Thuoc
from .forms import ThuocForm
from .forms import DonThuocForm, ChiTietDonThuocForm
from .models import DonThuoc, ChiTietDonThuoc

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Đăng ký thành công! Bạn có thể đăng nhập.')
            return redirect('login')  # Điều hướng đến trang đăng nhập
    else:
        form = SignUpForm()
    return render(request, 'medical_supplies/register.html', {'form': form})

def home(request):
    return render(request, 'medical_supplies/home.html')

@login_required
def index(request):
    return render(request, 'medical_supplies/index.html')

def danh_sach_thuoc(request):
    danh_sach = Thuoc.objects.all()  # Lấy tất cả các thuốc từ cơ sở dữ liệu
    return render(request, 'medical_supplies/danh_sach_thuoc.html', {'danh_sach': danh_sach})

def them_thuoc(request):
    if request.method == 'POST':
        form = ThuocForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_thuoc')
    else:
        form = ThuocForm()
    return render(request, 'medical_supplies/them_thuoc.html', {'form': form})

def sua_thuoc(request, thuoc_id):
    thuoc = get_object_or_404(Thuoc, id=thuoc_id)
    if request.method == 'POST':
        form = ThuocForm(request.POST, instance=thuoc)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_thuoc')
    else:
        form = ThuocForm(instance=thuoc)
    return render(request, 'medical_supplies/sua_thuoc.html', {'form': form})

def xoa_thuoc(request, thuoc_id):
    thuoc = get_object_or_404(Thuoc, id=thuoc_id)
    if request.method == 'POST':
        thuoc.delete()
        return redirect('danh_sach_thuoc')
    return render(request, 'medical_supplies/xoa_thuoc.html', {'thuoc': thuoc})

@login_required
def tao_don_thuoc(request):
    if request.method == 'POST':
        don_thuoc_form = DonThuocForm(request.POST)
        if don_thuoc_form.is_valid():
            # Lưu đơn thuốc và gán tài khoản tạo đơn
            don_thuoc = don_thuoc_form.save(commit=False)
            don_thuoc.user = request.user  # Gán tài khoản người dùng hiện tại
            don_thuoc.save()

            # Lưu các chi tiết đơn thuốc
            for i in range(len(request.POST.getlist('thuoc'))):
                thuoc_id = request.POST.getlist('thuoc')[i]
                so_luong = request.POST.getlist('so_luong')[i]
                if thuoc_id and so_luong:
                    ChiTietDonThuoc.objects.create(
                        don_thuoc=don_thuoc,
                        thuoc_id=thuoc_id,
                        so_luong=so_luong
                    )
            return redirect('danh_sach_don_thuoc')  # Chuyển hướng đến danh sách đơn thuốc
    else:
        don_thuoc_form = DonThuocForm()
        chi_tiet_form = ChiTietDonThuocForm()

    return render(request, 'medical_supplies/tao_don_thuoc.html', {
        'don_thuoc_form': don_thuoc_form,
        'chi_tiet_form': chi_tiet_form,
        'username': request.user.username,
    })

def danh_sach_don_thuoc(request):
    don_thuoc_list = DonThuoc.objects.all().order_by('-ngay_tao')
    return render(request, 'medical_supplies/danh_sach_don_thuoc.html', {
        'don_thuoc_list': don_thuoc_list,
    })