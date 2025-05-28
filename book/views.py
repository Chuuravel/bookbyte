from django.shortcuts import render, redirect, get_object_or_404
from book.models import BookInfo
from django.contrib.auth.models import User

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from book.forms import ReviewForm
from book.models import Review

# Create your views here.
def best_seller(request):
    # 모델이 학습한 베스트셀러를 반환 (추후 요수정) - 10개만 표시
    all_book = BookInfo.objects.all()

    # 페이징
    page = request.GET.get('page')
    page_obj, paginator, custom_range = paging_page.by_pagination(all_book, page)

    context = {
        "all_book" : all_book,
        # for paging
        "page_obj" : page_obj,
        "paginator" : paginator,
        "custom_range" : custom_range,
    }

    return render(request, "book/best_seller.html", context)

# 추천도서목록
def recommended_book(request):
    # 요청에 포함된 사용자가 로그인하지 않은 경우/users/login/ URL 로 리다이렉트
    if not request.user.is_authenticated:
        return redirect("users:login")
    
    # 모델이 학습한 추천도서를 반환 (추후 요수정)
    all_book = BookInfo.objects.all()

    # 페이징
    page = request.GET.get('page')
    page_obj, paginator, custom_range = paging_page.by_pagination(all_book, page)

    context = {
        "all_book" : all_book,
        # for paging
        "page_obj" : page_obj,
        "paginator" : paginator,
        "custom_range" : custom_range,
    }
    return render(request, "book/recommended_book.html", context)

# 전체 도서 목록
def show_all_book(request):
    # 요청에 포함된 사용자가 로그인하지 않은 경우/users/login/ URL 로 리다이렉트
    if not request.user.is_authenticated:
        return redirect("users:login")
    
    all_book = BookInfo.objects.all()

    # 페이징
    page = request.GET.get('page')
    page_obj, paginator, custom_range = paging_page.by_pagination(all_book, page)

    context = {
        "all_book" : all_book,
        # for paging
        "page_obj" : page_obj,
        "paginator" : paginator,
        "custom_range" : custom_range,
    }
    return render(request, "book/show_all_book.html", context)

# 책 상세페이지
def detail(request, pk):
    # 요청에 포함된 사용자가 로그인하지 않은 경우/users/login/ URL 로 리다이렉트
    if not request.user.is_authenticated:
        return redirect("users:login")
    
    book = get_object_or_404(BookInfo, id = pk)
    
    context = {
        "book" : book,
    }
    return render(request, "book/detail_book.html", context)

# 리뷰 작성
def create_review(request, pk):
    # 요청에 포함된 사용자가 로그인하지 않은 경우/users/login/ URL 로 리다이렉트
    if not request.user.is_authenticated:
        return redirect("users:login")
    
    # 폼 입력값이 있는 경우 저장
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            title = request.POST.get('title', None)
            content = request.POST.get('content', None)
            grade = request.POST.get('grade', None)

            # 유저 정보
            # 로그인한 유저            
            user = get_object_or_404(User, id = request.user.id)

            # 책 정보
            book = get_object_or_404(BookInfo, id = pk)

            # 리뷰 정보 저장
            review = Review()
            review.user_id = user
            review.book_id = book
            review.title = title
            review.content = content
            review.grade = grade
            review.is_bookbyte = True
            review.save()

            # 마이리뷰조회로 이동
            return redirect("book:show_review")
        else:
            context = load_init.review()
            return render(request, "book/create_review.html", context)

    else:
        context = load_init.review()
        return render(request, "book/create_review.html", context)
    
def show_review(request):
    # 요청에 포함된 사용자가 로그인하지 않은 경우/users/login/ URL 로 리다이렉트
    if not request.user.is_authenticated:
        return redirect("users:login")

    # 마이리뷰조회
    reviews = Review.objects.filter(user_id = request.user.id)
    context = {
        "reviews" : reviews,
    }
    return render(request, "book/show_review.html", context)


# 초기 로드
class load_init():
    # 초기화면(빈form)로드
    def review():
        form = ReviewForm()
        context = {
            "form" : form,
        }
        return context

class paging_page():
    def by_pagination(book_info, page):
        # 페이징
        paginator = Paginator(book_info, 10) # 한 페이지에 10레코드씩 표시
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

        return page_obj, paginator, custom_range

