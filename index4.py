from django.http import HttpResponse

def index(request):
    return HttpResponse('这个是dis中创建的文件')

