from django.shortcuts import render

# Create your views here.
def index(request):
    data = [
        {
            'nombre': 'a',
            'precio': 'b',
            'categoria': 'c',
            'imagen': '',
        },
        {
            'nombre': '',
            'precio': '',
            'categoria': '',
            'imagen': '',
        },
        {
            'nombre': '',
            'precio': '',
            'categoria': '',
            'imagen': '',
        },
        {
            'nombre': '',
            'precio': '',
            'categoria': '',
            'imagen': '',
        },
        {
            'nombre': '',
            'precio': '',
            'categoria': '',
            'imagen': '',
        },
        {
            'nombre': '',
            'precio': '',
            'categoria': '',
            'imagen': '',
        },
    ]
    contexto = {'data': data}
    return render(request, 'tarjetas/index.html', contexto)