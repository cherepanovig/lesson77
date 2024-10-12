from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

# def post_list(request):  # без выбора количества постов на странице
#     post_list = Post.objects.all().order_by('-pub_date')
#     paginator = Paginator(post_list, 3)  # Показывать 3 поста на странице
#
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # Если страница не является целым числом, то показываем первую страницу.
#         posts = paginator.page(1)
#     except EmptyPage:
#         # Если страница больше максимальной, то показываем последнюю страницу результатов.
#         posts = paginator.page(paginator.num_pages)
#
#     return render(request, 'blog/post_list.html', {'posts': posts})

def post_list(request):  # с выбором количества постов на странице

    # получение всех объектов модели Post из БД с сортировкой по дате публикации в порядке убывания
    post_list = Post.objects.all().order_by('-pub_date')

    # Получаем количество элементов на странице из GET-параметра
    items_per_page = request.GET.get('items', 3)

    # Попытка преобразовать полученный параметр в целое число. Если это не удается
    # (например, если передана строка), используем значение по умолчанию 3
    try:
        items_per_page = int(items_per_page)
    except ValueError:
        items_per_page = 3

    # Создание экземпляра класса Paginator с передачей списка постов и количества элементов на странице
    paginator = Paginator(post_list, items_per_page)

    page = request.GET.get('page')  # Получение номера страницы из GET-запроса
    try:
        posts = paginator.page(page)  # Получение страницы с постами
    except PageNotAnInteger:  # Если номер страницы не является целым числом, показывается первая страница
        posts = paginator.page(1)
    except EmptyPage:  # Если номер страницы больше максимального, показывается последняя страница
        posts = paginator.page(paginator.num_pages)

    # Рендеринг шаблона с передачей контекста, содержащего список постов и количество элементов на странице
    return render(request, 'blog/post_list.html', {'posts': posts, 'items_per_page': items_per_page})


