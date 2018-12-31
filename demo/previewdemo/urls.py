from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from . import views as v

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html')),
    path('create/', v.Create.as_view(), name='create'),
    path('edit/<int:pk>', v.Edit.as_view(), name='edit'),
    path('view/<int:pk>', v.Detail.as_view(), name='view'),
]
