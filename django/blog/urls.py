from django.urls import path, re_path

from . import views # 상대 경로 import
# from blog import views <- 절대 경로 import

urlpatterns = [
    path('', views.post_list),
    # path('detail/', views.post_detail),
    re_path(r'(?P<pk>\d+)/$', views.post_detail),
    # 숫자가 1개이상 반복되는 정규표현식, 해당 반복구간을 그룹으로 묶고, 그룹 이름을 pk로 지정
    # re.compile(r'(?P<pk>\d+)')
]
