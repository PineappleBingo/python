from django.shortcuts import render

posts = [
    {
        'author' : 'David',
        'title' : 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 31, 2021'    
    },
    {
        'author' : 'Jinho',
        'title' : 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'November 1, 2021'    
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
