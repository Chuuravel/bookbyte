from django.shortcuts import render
from book.models import BookInfo

# Create your views here.
def best_seller(request):
    # 모델이 학습한 베스트셀러를 반환 (추후 요수정)
    all_book = BookInfo.objects.all()
    context = {
        "all_book" : all_book,
    }

    return render(request, "book/best_seller.html", context)