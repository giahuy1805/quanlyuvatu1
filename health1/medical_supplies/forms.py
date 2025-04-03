from django import forms
from django.contrib.auth.models import User
from .models import Thuoc, DonThuoc, ChiTietDonThuoc

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Mật khẩu không khớp!")

class ThuocForm(forms.ModelForm):
    class Meta:
        model = Thuoc
        fields = ['ten_thuoc', 'mo_ta', 'gia', 'so_luong']
        widgets = {
            'ten_thuoc': forms.TextInput(attrs={'class': 'form-control'}),
            'mo_ta': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'gia': forms.NumberInput(attrs={'class': 'form-control'}),
            'so_luong': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class DonThuocForm(forms.ModelForm):
    class Meta:
        model = DonThuoc
        fields = ['ten_benh_nhan', 'ghi_chu']
        widgets = {
            'ten_benh_nhan': forms.TextInput(attrs={'class': 'form-control'}),
            'ghi_chu': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ChiTietDonThuocForm(forms.ModelForm):
    class Meta:
        model = ChiTietDonThuoc
        fields = ['thuoc', 'so_luong']
        widgets = {
            'thuoc': forms.Select(attrs={'class': 'form-control'}),
            'so_luong': forms.NumberInput(attrs={'class': 'form-control'}),
        }