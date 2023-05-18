from django.shortcuts import render, redirect
from .models import Diaries, Notice
from .forms import DiaryForm

# Create your views here.
def main_page(request):
    diaries = Diaries.objects.all()
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
    return render(request, 'myposts/diary_detail.html', {'diary': diary})