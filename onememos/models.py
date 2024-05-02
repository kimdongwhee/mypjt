from django.db import models

# onememos 테이블 클래스 생성 코드
# └ idx 필드 : PK (primary Key)
# └ memo_text 필드
# └ pubished_date 필드
class Memo_TB(models.Model):
    memo_text = models.CharField(max_length=250) #문자형 필드 : models.데이터타입, 최대길이 200
    writer_nm = models.CharField(max_length=20)
    writer_mail = models.CharField(max_length=30)
    published_date = models.DateTimeField(auto_now_add=True) #날짜형 필드 : models.데이터타입 + 현재 시간이 자동으로 입력되도록 auto_now_add=True 설정

    #작성된 메모 텍스트를 반환
    def __str__(self):
        return self.memo_text