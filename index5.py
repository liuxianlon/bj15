from django.http import HttpResponse

def index(request):
    return HttpResponse('这个是在dev中创建的文件')

