from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post, Comment
from .forms import NewCommentForm

def home(request):
    all_posts = Post.objects.all()[:10] # show only first 10 posts

    return render(request, 'blog/home.html', {'posts': all_posts})

def blog(request):
    all_posts = Post.objects.all()

    return render(request, 'blog/blog.html', {'posts': all_posts})


def post_single(request, post):
    #return render(request, 'blog/single.html', {'post' : post})
    post = get_object_or_404(Post, slug=post)

    comments = post.comments.filter(status=True)

    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False) #don't commit yet, because we need to associate the comment to the post
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/' + post.slug)
    else:
        comment_form = NewCommentForm()

    return render(request, 'blog/single.html', {'post': post, 'comments':  user_comment, 'comments': comments, 'comment_form': comment_form, })
