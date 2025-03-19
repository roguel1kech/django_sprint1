from django.shortcuts import render
from django.http import Http404


posts = [{'id': 0,
          'location': 'Остров отчаянья',
          'date': '30 сентября 1659 года',
          'category': 'travel',
          'text': ("Наш корабль, застигнутый в открытом море страшным штормом,"
                   "потерпел крушение. Весь экипаж, кроме меня, утонул; я же,"
                   "тут была слишком длинная строка"
                   "тут была слишком длинная строка."),
          },
         {'id': 1,
          'location': 'Остров отчаянья',
          'date': '1 октября 1659 года',
          'category': 'not-my-day',
          'text': ("тут была слишком длинная строка"
                   "тут была слишком длинная строка"
                   "тут была слишком длинная строка"
                   "тут была слишком длинная строка"
                   "тут была слишком длинная строка"
                   "тут была слишком длинная строка"
                   "тут была слишком длинная строка"),
          },
         {'id': 2,
          'location': 'Остров отчаянья',
          'date': '25 октября 1659 года',
          'category': 'not-my-day',
          'text': ("тут была слишком длинная строка."
                   "тут была слишком длинная строка"
                   "тут была слишком длинная строка"
                   "тут была слишком длинная строка."),
          },
         ]


def index(request):
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)


def post_detail(request, id):
    post = next((p for p in posts if p['id'] == id), None)
    if post is None:
        raise Http404("Пост не найден")
    context = {
        'post': post,
    }
    return render(request, 'detail.html', context)


def category_posts(request, category_slug):
    context = {
        'category_slug': category_slug,
    }
    return render(request, 'category.html', context)
