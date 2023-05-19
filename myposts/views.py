from django.shortcuts import render, redirect
from .models import Diaries, Notice, Comment
from .forms import DiaryForm

# Create your views here.
def main_page(request):
    diaries = Diaries.objects.filter(deleted=0)
    notice = Notice.objects.first()
    return render(request, 'myposts/main.html', {'diaries':diaries, 'notice':notice})

def diary_post(request):
    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.save()
            return redirect('main_page')
    else:
        form = DiaryForm()
    return render(request, 'myposts/diary_post.html', {'form': form})

def diary_detail(request, pk):
    diary = Diaries.objects.get(id=pk)
    comments = Comment.objects.filter(diary = diary)
    return render(request, 'myposts/diary_detail.html', {'diary': diary, 'comments' : comments})

def diary_delete(request, pk):
    diary = Diaries.objects.get(id=pk)
    diary.deleted = 1
    diary.save()
    return redirect('main_page')

def add_comment(request, pk):
    diary = Diaries.objects.get(id=pk)
    
    if request.method == "POST":
        text = request.POST.get('commentInput')
        Comment.objects.create(diary=diary, contents=text)
        
    return redirect('diary_detail', pk=diary.pk)