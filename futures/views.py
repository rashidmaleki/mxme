from django.shortcuts import render
from django.views.generic import View, UpdateView
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from json import dumps
from .mexc import MexcApi
from .models import Setting
from .forms import SettingForm
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect

# Create your views here.


class DashboardView(LoginRequiredMixin, View):
    template_name = 'futures/dashboard.html'

    def get(self, request, *args, **kwargs):
        context = {
            "current_page":"dashboard"
        }
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "dashboard"
        return context

class NewOrderView(LoginRequiredMixin, View):
    template_name = 'futures/new_order.html'
    mexc = MexcApi()

    def get(self, request, *args, **kwargs):
        symbols = self.mexc.all_contract()
        
        context = {
            "current_page":"new_order",
            "symbols": symbols['data']
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        params = {
            "symbol": request.POST['symbol'],
            "price": request.POST['price'],
            "vol": request.POST['vol'],
            "leverage": request.POST['leverage'],
            "side": request.POST['side'],
            "type": request.POST['type'],
            "openType": request.POST['openType'],
            "positionMode": request.POST['positionMode']
        }

        user_key, created = Setting.objects.get_or_create(
        user=self.request.user)
        
        mexc = MexcApi()
        mexc.api_key = user_key.api_key
        mexc.api_sec = user_key.secret_key
        mexc.params = dumps(params)
        context = mexc.order_new()

        return render(request, self.template_name, context)
   

class OrderListView(LoginRequiredMixin, View):
    template_name = 'futures/order_list.html'
    
    def get(self, request, *args, **kwargs):

        params = {
            "page_num": 1,
            "page_size": 20,
        }

        user_key, created = Setting.objects.get_or_create(
                user=self.request.user)
        
        mexc = MexcApi()
        mexc.api_key = user_key.api_key
        mexc.api_sec = user_key.secret_key
        mexc.params = dumps(params)
        order_list = mexc.order_list()
        orders = order_list
        
        context = {
            "current_page":"order_list",
            "orders":orders,
        }
        return render(request, self.template_name, context)

class SettingView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Setting
    form_class = SettingForm
    template_name = 'futures/setting.html'
    success_message = "Setting updated!"

    def get_object(self):
        setting, created = self.model.objects.get_or_create(
            user=self.request.user)
        return setting

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "setting"
        return context
    
    def get_success_url(self):
        return reverse('setting')
