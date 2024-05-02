#라이브러리
from django.urls import path
from . import views

urlpatterns = [
    #path(1."", 2.어떤 것, 즉, view 파일에서 정의한 함수, name="대표키워드")
    #"" 웹 주소~~(http://locaalhost:*****/onememos/)와 같은의미, 2는 어떤것(view)
    path("", views.main, name="main"), #view파일에서 지정한 main 함수로 연결(views에서 정의한 함수명과 동일하게 설정) + (name 생략가능)
    path("createMemo/", views.createMemo) #onememos/createMemo url. view의 createMemo 함수 호출
]