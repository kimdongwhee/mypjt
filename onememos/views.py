from django.shortcuts import render
from django.http import HttpResponse #해당 페이지에대한 응답관련 라이브러리 
from .models import *

def main(request):  #requests에 주소가 매게변수로 들어감 / index 또는 main으로 기재해도됨
    #요청에 따른 응답으로 뿌려주겠음
    #return HttpResponse("OneMemos!Hello, World!:-)"
    return render(request, "main.html") #templates>main.html을 틀어놓은다.

def createMemo(request): #requests에 주소가 매게변수로 들어감 / index 또는 main으로 기재해도됨
    #요청에 따른 응답으로 뿌려주겠음
    #방식으로는 Get과 Post 방식이있음 ▷ request.GET, request.POST 등 ▷ 사전형 데이터
    #memoContent = request.GET["memoContent"]  memocontent 데이터인자를 받아 get한 후 페이지 로드
    #/onememos/createMemo/?memoContent=데이터값 형태의 url
    # memoContent = request.GET["memoContent"]
    memoContent = request.POST["memoContent"] 
    memoName = request.POST["memoName"]
    memoEmail = request.POST["memoEmail"]
    return HttpResponse("Create Memo = "+ memoContent + memoName + memoEmail)