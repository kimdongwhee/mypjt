from django.contrib import admin
from django.urls import path, include #path함수, include 함수사용을 위해 호출
#urlpatterns 정리
# └ /(슬래시)는 기본적으로 장고가 알아서하지만 특별한 경우가 아니라면 /(슬래시)를 붗여주자
# └ 마지막에 ,(콤마)를 생략해도되고 붙여도됨
# └ 서버구동시 변화가 감지되면서 자동으로 리로더
# └ 잘못된 코드로 오류가 나면 서버구동이 자동적으로 감지하고 에러를냄. 수정되면 다시 재구동함.
# └ 초기화면 view.index 또는 views.main으로 해도됨.
urlpatterns = [
    #하위앱에 대한 url주소와 urls.py (앱명.urls 기재) 경로
    path('admin/', admin.site.urls),
    path("onememos/", include("onememos.urls")), #onememos 앱 하위에 urls
]