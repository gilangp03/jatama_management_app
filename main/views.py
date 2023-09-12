from django.shortcuts import render

# Create your views here.

def show_main(request):
    return render(request, "main.html")


def show_inventory(request):
    context = {
        'name': 'Daxe',
        'stock' : 10,
        'price' : 'Rp 500.000',
        'detail' : 'Kursi kotak dengan 3 warna, hitam, coklat tua, dan krim'
    }
    return render(request, "inventory.html", context)