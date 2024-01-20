from django.shortcuts import render, redirect, get_object_or_404
from .models import Category


def index(request):
    return render(request, 'common/index.html')


def category_details(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    categories = Category.objects.all()

    context = {
        'category': category,
        'categories': categories
    }

    if request.method == 'GET':
        return render(request, 'category/category_details.html', context)


def category_list(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }
    if request.method == 'GET':
        return render(request, 'category/category_list.html', context)


def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    context = {
        'category': category
    }

    if request.method == 'GET':
        return render(request, 'category/delete_category.html', context)

    elif request.method == 'POST':
        category.delete()
        return redirect('category_list')


def update_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    categories = Category.objects.all()

    context = {
        'category': category,
        'categories': categories,
    }

    if request.method == 'GET':
        return render(request, 'category/update_category.html', context)

    elif request.method == 'POST':
        data = request.POST
        category.name = data.get('name', category.name)
        category.description = data.get('description', category.description)
        image = request.FILES.get('image', None)
        if image:
            category.image = image

        parent_id = data.get('parent', None)
        category.parent = get_object_or_404(Category, id=parent_id) if parent_id else None
        category.save()
        return redirect('category_list')


def create_category(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
        'title': 'title',
        'some': 'some'
    }

    if request.method == 'GET':
        return render(request, 'category/create_category.html', context)

    elif request.method == 'POST':
        data = request.POST
        name = data.get('name', '')
        description = data.get('description', '')
        image = request.FILES.get('image', None)
        parent_id = data.get('parent', None)
        parent = get_object_or_404(Category, id=parent_id) if parent_id else None
        Category.objects.create(
            name=name,
            description=description,
            image=image,
            parent=parent
        )

        return redirect('category_list')




