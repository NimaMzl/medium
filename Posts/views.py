from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.core.paginator import Paginator



def blog_list(request):

    all_articles=Article.publish.all()

    featured_articles=Article.publish.all().order_by('-created')[:4]


    paginator = Paginator(all_articles, 1)

    page_number = request.GET.get("page")

    blog_list = paginator.get_page(page_number)


    context={
        "articles":featured_articles,
        "page":blog_list,
        
    }

    return render(request,"blogs/list.html",context)

def blog_detail(request,Slug):
    article=Article.publish.get(slug=Slug)
    

    context={
        "article":article,
        
    }
    return render(request,"blogs/detail.html",context)

def blog_author(request,Author):
    Post=Article.publish.filter(author__username=Author)



    context={
        "Post_Author":Post[0].author,
        "post":Post,
        
    }

    return render(request,"blogs/author.html",context)

