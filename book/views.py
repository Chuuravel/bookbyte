from django.shortcuts import render

# Create your views here.
def best_seller(request):
    return render(request, "book/best_seller.html")