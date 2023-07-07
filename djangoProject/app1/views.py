from django.shortcuts import render, redirect
from app1.models import WriteSomething
from app1.forms import WriteSomethingForm

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

    return render(request, "community.html", {"data_list": data_list, "sort_by": sort_by, "search_query": search_query})


def create(request):
    if request.method == 'POST':
        form = WriteSomethingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('community')
    else:
        form = WriteSomethingForm()

    return render(request, 'create.html', {'form': form})
