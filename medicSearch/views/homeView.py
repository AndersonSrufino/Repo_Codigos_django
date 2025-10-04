from django.http import HttpResponse

def home_view(request):
    return HttpResponse('<h1>Olá mundo!</h1>')

def home(request):
    return HttpResponse("<h1>Página Inicial de Teste</h1><p>Se você está vendo isso, a view e a URL estão funcionando!</p>")