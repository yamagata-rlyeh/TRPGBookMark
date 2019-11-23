from django.shortcuts import render
from django.utils import timezone
from .models import CharacterSheet
from .forms import PostForm, UserForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

def welcome(request):
    return render(request, 'submitbox/welcome.html')
    
def login_form(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        #入力されたIDとPassの組み合わせが存在すればそのユーザーの保管庫に移動
        return redirect('post_list')
    else:
        form = UserForm()
    return render(request, 'submitbox/new_user_add.html', {'form': form})

def new_user_add(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            #post = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            #post.save()
            return redirect('post_list')
    else:
        form = UserForm()
    return render(request, 'submitbox/new_user_add.html', {'form': form})

def post_list(request):

    if request.method =="POST":
        posts = CharacterSheet.objects.filter(character_name__contains= request.POST.get('search_text')).order_by('pk')
    else:
        posts = CharacterSheet.objects.filter(published_date__lte=timezone.now()).order_by('pk')
    return render(request, 'submitbox/post_list.html', {'posts': posts})


def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'submitbox/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(CharacterSheet, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'submitbox/post_edit.html', {'form': form})

def user_list(request):
    posts = CharacterSheet.objects.filter(user_name='').order_by('pk')
    return render(request, 'submitbox/post_list.html', {'posts': posts})

def post_delete(request,pk):
    post = get_object_or_404(CharacterSheet, pk=pk)
    post.delete()
    return redirect('post_list' )


    


