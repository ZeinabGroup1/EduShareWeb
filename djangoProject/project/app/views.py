from django.shortcuts import get_object_or_404, render, redirect
from app.models import WriteSomething
from app.forms import WriteSomethingForm

def index(request):
    return render(request, "index.html")

def community(request):
    sort_by = request.GET.get('sort', 'newest')
    search_query = request.GET.get('search', '')

    if sort_by == 'newest':
        data_list = WriteSomething.objects.order_by('-id')
    elif sort_by == 'oldest':
        data_list = WriteSomething.objects.order_by('id')
    else:
        data_list = WriteSomething.objects.all()

    if search_query:
        data_list = data_list.filter(title__icontains=search_query)

    return render(request, "community2.html", {"data_list": data_list, "sort_by": sort_by, "search_query": search_query})

def content(request,content_id):
    data = get_object_or_404(WriteSomething, id=content_id)
    return render(request, "content.html",{"data":data})

def create(request):
    if request.method == 'POST':
        form = WriteSomethingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('community')
    else:
        form = WriteSomethingForm()

    return render(request, 'create.html', {'form': form})
