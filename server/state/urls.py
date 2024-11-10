from django.urls import path
from django.views.generic import TemplateView

from .views import StateData, StateDataCreate

urlpatterns = [
    path('game/', StateDataCreate.as_view(), name='user-create'),
    path('game/<slug:tg_name>/', StateData.as_view(), name='user-info'),
    path('', TemplateView.as_view(template_name='index.html'), name='game'),
]