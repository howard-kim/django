from blog.models import Post, Comment
from django.shortcuts import render, redirect

def post_list(request):
    posts = Post.objects.all()
    ctx = {
        "posts": posts,
    }
    # print(ctx)
    return render(request, "post_list.html", ctx)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        comment_content = request.POST["comment"]
        Comment.objects.create(
            post = post,
            content=comment_content,
        )

        
    # print(post)

    ctx = {
        "post": post,
    }
    return render(request, "post_detail.html", ctx)

def post_add(request):
    # print(request.POST)
    if request.method == "POST":
        print(request.FILES)
        print("method POST")
        title = request.POST["title"]
        content = request.POST["content"]
        thumbnail = request.FILES["thumbnail"]
        post = Post.objects.create(
            title = title,
            content = content,
            thumbnail = thumbnail,
        )
        return redirect(f"/posts/{post.id}/")

        # print(title)
        # print(content)
        
    else:
        print("method GET")
    
    return render(request, "post_add.html")