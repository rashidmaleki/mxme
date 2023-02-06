from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('new-order/', views.NewOrderView.as_view(), name='new-order'),
    path('order-list/', views.OrderListView.as_view(), name='order-list'),
    path('setting/', views.SettingView.as_view(), name='setting'),
]
