from django.urls import path

from . import views # 상대 경로 import
# from blog import views <- 절대 경로 import

urlpatterns = [
    path('', views.post_list),
    path('detail/', views.post_detail),
]
