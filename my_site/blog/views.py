from http.client import HTTPResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from urllib import request
from django.shortcuts import render
from .models import Post
from .forms import CommentForm
from django.views.generic import ListView, DetailView
from django.views import View

def get_date(post):
    return post['date']

class StartPageView(ListView):
    template_name= "blog/index.html"
    model= Post 
    ordering= ["-date"]
    context_object_name= "posts"
    def get_queryset(self):
        queryset= super().get_queryset()
        data = queryset[:3]
        return data
class AllPostView(ListView):
     template_name= "blog/all-post.html"
     model= Post 
     ordering= ["-date"]
     context_object_name= "all_posts"

class PostDetail(View):
    def is_stored_post(self ,request,post_id ):
        stored_post= request.session.get("stored_post")
        if stored_post is not None:
            is_savedfor_later= post_id in stored_post
        else:
            is_savedfor_later=False
        return is_savedfor_later
    
    
    def get(self, request, slug):
        post= Post.objects.get(slug= slug)
       
        context={
            "post":post,
            "post_tags":post.tag.all(),
            "comment_form": CommentForm(),
            "savedforlater": self.is_stored_post(request, post.id)
            

        }
        return render(request, "blog/post-detail.html",context)


    def post(self,request, slug):
        comment_form= CommentForm(request.POST)
        post= Post.objects.get(slug= slug)
        if comment_form.is_valid():
            comment= comment_form.save(commit=False)
            comment.post=post
            comment.save()
            
             
            return HttpResponseRedirect(reverse("posts-detail", args=[slug]))
        context={
            "post":post,
            "post_tags":post.tag.all(),
            "comment_form": comment_form,
            "savedforlater": self.is_stored_post(request, post.id)

        }
        
        return render(request, "blog/post-detail.html",context)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["post_tags"] =self.object.tag.all() 
    #     context["comment_form"]= CommentForm()
    #     return context
    
class ReadLaterView(View):
    def get(self, request):
        stored_post= request.session.get("stored_post")

        context= {}
        if stored_post is None or len(stored_post) ==0:
            context["posts"]=[]
            context["has_posts"]=False
        else:
            posts =Post.objects.filter(id__in=stored_post)
            context["posts"]=posts
            context["has_posts"]= True
        return render(request, "blog/stored_post.html", context)



    def post(self, request):
        stored_post= request.session.get("stored_post")
        if stored_post is None:
            stored_post= []
        post_id=int(request.POST["post_id"])
        if post_id not in stored_post:
          stored_post.append(post_id) 
          
        else:
            stored_post.remove(post_id)
        request.session["stored_post"]= stored_post
        return HttpResponseRedirect("/blog/")



    
  


        

# Create your views here.

# def startpage(request):
#     latest_post= Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html",{"posts":latest_post} )
   
# def posts(request):
#     all_posts= Post.objects.all().order_by("-date")
#     return render(request,"blog/all-post.html",{
#         "all_posts": all_posts
#     } )
# def posts_detail(request,slug):
#     identified_post= Post.objects.get(slug=slug)

#     return render(request, "blog/post-detail.html",{
#         "post":identified_post,
#         "post_tags":identified_post.tag.all()

#     })