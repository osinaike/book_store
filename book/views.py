from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from book.models import Publisher, Book, Author
from django.db.models import Count, Max, Min, Sum, Avg, Q, F, DecimalField, ExpressionWrapper
from .forms import BookForm


def index(request):
    queryset = Publisher.objects.exclude(name="Mycat")
    return render(request, "book/index.html", context={"publishers": list(queryset)})


def publisher_details(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    return render(request, "book/publisher-detail.html", context={"publisher": publisher})


def book_list(request):
    queryset = Book.objects \
        .select_related("publisher") \
        .filter(title=F('slug')) \
        .annotate(discounted_price=ExpressionWrapper(F('price') * 0.8, output_field=DecimalField()))
    result = queryset.aggregate(count=Count('id'), average=Avg('price'))
    return render(request, "book/book-list.html", context={"books": list(queryset), "result": result})

    # .filter(Q(title__icontains="the")) | ~Q(price__isnull=True)
    # books = list(queryset)
    # book = queryset[0]
    # queryset = [Book.objects.all()]


def author_list(request):
    # queryset = Book.objects.annotate(Count('id')) # outputs the book table in the order of ID
    queryset = Book.objects.filter(authors__books__publisher_id__lt=5)

    return render(request, "book/author-list.html", context={"author": list(queryset)})


def book_create(request):
    if request.method == 'GET':
        pass
    elif request.methgod == 'POST':
        pass
    form = BookForm()

    return render(request, "book/book-create.html", context={"form": form})