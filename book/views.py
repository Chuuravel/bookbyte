from django.shortcuts import render
from book.models import BookInfo
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def best_seller(request):
    # 모델이 학습한 베스트셀러를 반환 (추후 요수정) - 10개만 표시
    all_book = BookInfo.objects.all()
    context = {
        "all_book" : all_book,
    }

    return render(request, "book/best_seller.html", context)

# 추천도서목록
def recommended_book(request):
    # 모델이 학습한 추천도서를 반환 (추후 요수정)
    all_book = BookInfo.objects.all()
    context = {
        "all_book" : all_book,
    }
    return render(request, "book/recommended_book.html", context)

def show_all_book(request):
    # 전체 도서를 반환
    all_book = BookInfo.objects.all()

    # 페이징
    page = request.GET.get('page')
    paginator = Paginator(all_book, 10) # 한 페이지에 10레코드씩 표시
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1 # 페이지 정보가 없는 경우 첫 페이지를 표시
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages # 마지막 페이지를 접속
        page_obj = paginator.page(page)

    # 현재 페이지를 기준으로 총 5개의 페이지만 표시
    left_index = (int(page) - 2)
    if left_index < 1:
        left_index = 1 # 최솟값은 1로 설정

    right_index = (int(page) + 2)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages # 최댓값은 최대페이지수로 설정

    custom_range = range(left_index, right_index+1) # 마지막 숫자도 포함(+1)

    context = {
        "all_book" : all_book,
        "page_obj" : page_obj,
        "paginator" : paginator,
        "custom_range" : custom_range,
    }
    return render(request, "book/show_all_book.html", context)