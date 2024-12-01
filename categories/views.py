from django.shortcuts import render, redirect
from .forms import CategoryForm
from django.contrib import messages
# Create your views here.
def add_categories(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category added successfully")
            return redirect('add_categories')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})