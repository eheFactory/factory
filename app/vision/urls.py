from django.urls import path, include
from . import views

app_name = 'visionlab'

urlpatterns = [
    path('averagingBlur/', views.vlAveragingBlurView.as_view(), name='vlAveragingBLur'),
    path('medianBlur/', views.vlMedianBlurView.as_view(), name='vlMedianBlur'),
    path('gaussianBlur/', views.vlGaussianBlurView.as_view(), name='vlGaussianBlur')
]