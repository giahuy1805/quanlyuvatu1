from django.db import models
from django.contrib.auth.models import User


class Thuoc(models.Model):
    ten_thuoc = models.CharField(max_length=255)  # Tên thuốc
    mo_ta = models.TextField(blank=True, null=True)  # Mô tả thuốc
    gia = models.DecimalField(max_digits=10, decimal_places=2)  # Giá thuốc
    so_luong = models.IntegerField()  # Số lượng tồn kho

    def __str__(self):
        return self.ten_thuoc


class DonThuoc(models.Model):
    ten_benh_nhan = models.CharField(max_length=255)
    ngay_tao = models.DateTimeField(auto_now_add=True)
    ghi_chu = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Liên kết với tài khoản tạo đơn

    def __str__(self):
        return f"Đơn thuốc của {self.ten_benh_nhan} - {self.ngay_tao.strftime('%Y-%m-%d')}"

class ChiTietDonThuoc(models.Model):
    don_thuoc = models.ForeignKey(DonThuoc, on_delete=models.CASCADE, related_name='chi_tiet')
    thuoc = models.ForeignKey(Thuoc, on_delete=models.CASCADE)
    so_luong = models.IntegerField()

    def __str__(self):
        return f"{self.thuoc.ten_thuoc} - {self.so_luong}"