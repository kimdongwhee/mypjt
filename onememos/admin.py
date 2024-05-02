from django.contrib import admin
#onememos app의 models.py에 생성한 Memo_TB란 테이븍 클랙스 임포트
from onememos.models import Memo_TB 
# Register your models here.
admin.site.register(Memo_TB)