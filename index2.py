from django.http import HttpResponse

def index2(request):
    return HttpResponse('你好，很高兴认识你')


def index(request):
    return HttpResponse('怎么找不到')
