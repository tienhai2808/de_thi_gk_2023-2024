from django.shortcuts import render, get_object_or_404, redirect
from .forms import HangHoaForm
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
  return render(request, 'index.html')

def suahanghoa(request, id_hang_hoa=None):
  if id_hang_hoa:
    hang_hoa = get_object_or_404(HangHoa, id=id_hang_hoa)
    title = 'SỬA THÔNG TIN MẶT HÀNG'
    button = 'Sửa'
  else:
    hang_hoa=None
    title = 'THÊM MỚI MẶT HÀNG'
    button = 'Thêm'
  form = HangHoaForm(instance=hang_hoa)
  if request.POST:
    form = HangHoaForm(request.POST, instance=hang_hoa)
    if form.is_valid():
      hang_hoa_update = form.save()
      if not id_hang_hoa:
        messages.success(request, f'Thêm mặt hàng {hang_hoa_update.ten} thành công')
      else:
        messages.success(request, f'Các thông tin điều chỉnh của mặt hàng {hang_hoa_update.ten} đã được lưu')
      return redirect('/dshanghoa/')
  return render(request, 'suahanghoa.html', {'form': form, 'title': title, 'button': button})\
    
def dshanghoa(request):
  hanghoas = HangHoa.objects.all()
  for hh in hanghoas:
    # list_ton_kho = []
    # for khh in hh.khohanghoa_set.all():
    #   list_ton_kho.append(khh.so_luong)
    # hh.ton_kho = sum(list_ton_kho)
    hh.ton_kho = sum([khh.so_luong for khh in hh.khohanghoa_set.all()])
  title = 'DANH SÁCH HÀNG HÓA'
  return render(request, 'dshanghoa.html', {'hanghoas': hanghoas, 'title': title})