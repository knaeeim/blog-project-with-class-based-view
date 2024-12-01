from django.urls import path, include
from .views import *
urlpatterns = [
    # path('add_post/', add_post, name="add_post"),
    path('add_post/', AddPost.as_view(), name="add_post"),
    # path('edit/<int:id>', edit_post, name="edit_post"),
    path('edit/<int:id>', EditPost.as_view(), name="edit_post"),
    # path('delete/<int:id>', delete_post, name="del_post"),
    path('delete/<int:id>', DeletePost.as_view(), name="del_post"),
    path('details/<int:id>', DetailsPostView.as_view(), name="details_post"),
]