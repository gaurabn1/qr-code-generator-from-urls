from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('qr_code_generator/', qr_code_generator, name="qr_code_generator"),
]