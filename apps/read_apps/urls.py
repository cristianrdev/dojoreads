from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard ),
    path('new_book', views.new_book ),
    path('book_detail/<num>', views.book_detail ),
    path('<book_id>/delete_review/<review_id>', views.delete_review ),
    path('add_review/<book_id>', views.add_review ),
    path('delete_book/<book_id>', views.delete_book ),
    path('user_detail/<user_id>', views.user_detail ),

    # path('register', views.register, name = "register"),
    # path('login', views.login, name = "login"),
    # path('logout', views.logout ),

]