from django.urls import path

from SecondCategoryTree.categories import views

urlpatterns = (
    path('', views.index, name='index'),
    path('categories/<int:category_id>/', views.category_details, name='category_details'),
    path('categories/', views.category_list, name='category_list'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('update_category/<int:category_id>/', views.update_category, name='update_category'),
    path('create_category/', views.create_category, name='create_category')
)
