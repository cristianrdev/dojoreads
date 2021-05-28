from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from apps.login_app.models import User
from apps.read_apps.models import Book, Author, Review
from .forms.new_book import BookForm, AuthorForm, ReviewForm


def dashboard(request):
    #verifica si hay sesión
    if 'id' not in  request.session :
            #si no hay sesión devuelve al login
            return redirect('/')
    else:
        if request.method == 'GET':         
            active_user = User.objects.get(id = int(request.session['id']) )
            all_books = Book.objects.all()
            all_reviews = Review.objects.all()
            context = {
                    'active_user' : active_user,
                    'all_books': all_books,
                    'all_reviews' : all_reviews.order_by("-created_at")[:3],
                }
            return render(request, 'dashboard.html', context)


def new_book(request):
    if 'id' not in  request.session :
        #si no hay sesión devuelve al login
        return redirect('/')
    else:
        active_user = User.objects.get(id = int(request.session['id']) )
        all_authors = Author.objects.all()
        

        bookform = BookForm()
        authorform = AuthorForm()
        reviewform = ReviewForm()

        if request.method == 'GET': 
            context = {
                'active_user' : active_user,
                'bookform' : bookform,
                'authorform' : authorform,
                'reviewform' : reviewform,
                'all_authors' : all_authors,
                
                
            }
            return render(request, 'new_book.html', context)

        else: #guardar libro y su autor
            this_user = User.objects.get(id = int(request.session['id']) )

            print(f"usuario {request.session['id']} ")
            print(f"title :{request.POST['title']}")
            print(f"name author :{request.POST['name']}")
            print(f"review :{request.POST['review']}")
            print(f"rating{request.POST['rating']}")
            
            if request.POST['name']:
                #nuevo autor 
                this_author = Author.objects.create(
                    name = request.POST['name'],
                    uploaded_by = this_user,              
                )
            else:
                #autor preexistente de la lista
                this_author = Author.objects.create(
                    name = request.POST['author'],
                    uploaded_by = this_user,
                    )

            new_book = Book.objects.create(
                title = request.POST['title'], 
                author = this_author,
                uploaded_by = this_user,
            )


            new_review = Review.objects.create(
                review = request.POST['review'],
                rating = request.POST['rating'],
                uploaded_by = this_user,
                book = new_book

            )

            return redirect('/')


def book_detail(request, num):
    if 'id' not in  request.session :
        #si no hay sesión devuelve al login
        return redirect('/')
    else:
        review_form = ReviewForm()
        active_user = User.objects.get(id = int(request.session['id']) )
        this_book = Book.objects.get(id = num)
        # this_author = Author.objects.get(id = this_book.authors.id)
        this_author = this_book.author
        all_reviews_of_this_book = this_book.review_book.all()
        user_review_this_book = False
        user_upload_this_book = False

        for  rev in all_reviews_of_this_book:
            if active_user.id == rev.uploaded_by.id:
                print("YA HA SIDO COMENTADO POR MI")
                user_review_this_book = True
            else:
                print("NO LO HE COMENTADO AUN")

        if active_user == this_book.uploaded_by:
            user_upload_this_book = True
            print("Yo lo publiqué")

        context = {
            'review_form' : review_form,
            'active_user' : active_user,
            'this_book' : this_book,
            'this_author' : this_author,
            'all_reviews_of_this_book' : all_reviews_of_this_book,
            'user_review_this_book' : user_review_this_book,
            'user_upload_this_book' : user_upload_this_book,
        }

        return render(request, 'book_detail.html', context)

def delete_review(request, book_id, review_id ):
    if 'id' not in  request.session :
        #si no hay sesión devuelve al login
        return redirect('/')
    else:
        comment_to_delete = Review.objects.get(id = int(review_id))
        if comment_to_delete.uploaded_by.id == int(request.session['id']):
            print('pasó por acá'*20)
            comment_to_delete.delete()
        return redirect("/books/book_detail/"+ str(book_id))


def add_review(request, book_id):
    if 'id' not in  request.session :
        #si no hay sesión devuelve al login
        return redirect('/')
    else:
        this_book = Book.objects.get(id = int(book_id))
        active_user = User.objects.get(id = int(request.session['id']) )

        new_review = Review.objects.create(
                review = request.POST['review'],
                rating = request.POST['rating'],
                uploaded_by = active_user,
                book = this_book,
        )
        return redirect("/books/book_detail/"+ str(book_id))


def delete_book(request, book_id):
    if 'id' not in  request.session :
        #si no hay sesión devuelve al login
        return redirect('/')
    else:
        this_book = Book.objects.get(id = int(book_id))
        this_book.delete()
        return redirect('/')

def user_detail(request, user_id):
    if 'id' not in  request.session :
        #si no hay sesión devuelve al login
        return redirect('/')
    else:
     
        active_user = User.objects.get(id = int(request.session['id']) )
        this_user = User.objects.get(id =int(user_id) )
      

        all_user_reviews= this_user.review_uploaded_by.all()
        reviews_counter = all_user_reviews.count()
        context = {
            "this_user" : this_user,
            "all_user_reviews" : all_user_reviews,
            "reviews_counter" : reviews_counter,
            "active_user" : active_user,
        }
       
        return render(request, "user_detail.html", context)














