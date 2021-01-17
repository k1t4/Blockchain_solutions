from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='blocks/', permanent=True)),
    path('blocks/', views.blocks, name="blocks"),
    path('blocks/<int:pk>', views.block, name="block"),
]
