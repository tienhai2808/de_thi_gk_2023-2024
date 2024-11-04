from django.db import models

# Create your models here.
class Kho(models.Model):
  ten = models.CharField(max_length=100)
  dia_chi = models.CharField(max_length=255, blank=True)
  
  def __str__(self):
    return self.ten
  
  
class HangHoa(models.Model):
  ten = models.CharField(max_length=200)
  mo_ta = models.TextField(blank=True)
  don_vi_tinh = models.CharField(max_length=7, choices=(('Kg', 'Kg'), ('Cái', 'Cái'), ('Chai', 'Chai'), ('Hộp', 'Hộp')))
  kho = models.ManyToManyField(Kho, through='KhoHangHoa')
  
  def __str__(self):
    return self.ten
  
  
class KhoHangHoa(models.Model):
  hang_hoa = models.ForeignKey(HangHoa, on_delete=models.PROTECT)
  kho = models.ForeignKey(Kho, on_delete=models.PROTECT)
  so_luong = models.IntegerField(default=0)
  #5$uiKlq9
  