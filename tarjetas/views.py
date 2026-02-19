from django.shortcuts import render

# Create your views here.
def index(request):
    data = [
        {
            'nombre': 'Autobiografía de un Yogui',
            'precio': '20.000',
            'autor': 'Paramahansa Yogananda',
            'imagen': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTzO_sgx3bzgzSSILwPL_63SIdaEyCUxQZbQ&s',
        },
        {
            'nombre': 'Kriya Yoga',
            'precio': '20.000',
            'autor': 'Paramahamsa Hariharananda',
            'imagen': 'https://m.media-amazon.com/images/I/81Nz8TqNMML._AC_UF1000,1000_QL80_.jpg',
        },
        {
            'nombre': 'Secretos Revelados de Kriya Yoga',
            'precio': '25.000',
            'autor': 'J.C. Stevens',
            'imagen': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMR69ZJ7CwJ2FgwKVpicdCq1Jd0RCxbJNoug&s',
        },
        {
            'nombre': 'El Nuevo Sendero',
            'precio': '25.000',
            'autor': 'Swami Kriyananda',
            'imagen': 'https://images.cdn1.buscalibre.com/fit-in/360x360/e9/ea/e9ea62258e8b3d5708371bd9f1de057d.jpg',
        },
        {
            'nombre': 'Raya Yoga',
            'precio': '25.000',
            'autor': 'Swami Kriyananda',
            'imagen': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzvpnETJ3t-gVpYlKt74W-rWjwjDr91iw5fg&s',
        },
        {
            'nombre': 'El Yoga del Bhagavad Guita',
            'precio': '23.000',
            'autor': 'Paramahansa Yogananda',
            'imagen': 'https://images.cdn3.buscalibre.com/fit-in/360x360/19/23/19236668b071e8d15286e0fe249ff78a.jpg',
        },
    ]
    contexto = {'data': data}
    return render(request, 'tarjetas/index.html', contexto)