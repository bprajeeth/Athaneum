import email
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from books.forms import userform
from books.models import Book,BookUser
from django.http import HttpResponse , HttpResponseRedirect
# Create your views here.
def home(request):
    book_data = Book.objects.all()
    book_template = loader.get_template("homepage.html")
    context = {"books_data":book_data}
    html_data = book_template.render(context)
    return HttpResponse(html_data)    

def make_reservation(request):
    '''
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = userform(request.POST)
        form.save()
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/success')
        try:
            curr_book = Book.objects.all(isbn = BookUser.isbn)
            if curr_book.books_count == 0:
                object.status = None
                object.save()
                return HttpResponseRedirect("/fail")
            curr_book.books_count -= 1
            curr_book.save()
            object.save()
            return HttpResponseRedirect("/success")
        except:
            object.status = None
            object.save()
            return HttpResponseRedirect("/fail")
    '''
    if request.method == 'POST':
        book_isbn = request.POST['isbn'] # VALUE INSIDE BRACKETS ARE ID FROM HTML TAGS
        user_email = request.POST['mail_id']
        username = request.POST['name']
        dept = request.POST['dept']
        type = request.POST['type']
        try:
            user = BookUser(isbn=book_isbn, email_id=user_email, name=username, dept=dept, type=type)
            book_save = Book.objects.get(isbn=book_isbn)
            book_save.books_count-=1
            book_save.save()
            user.save()         

            return HttpResponseRedirect("/success")
        except:
            return HttpResponseRedirect("/fail")
    else:
        return render(request, "reserve.html")        
def failure(request):
    return render(request,"fail.html")

def successfull(request):
    return render(request,"success.html")       

def show_reservation(request):
    user_data = BookUser.objects.all()
    book_template = loader.get_template("show_reservation.html")
    context = {"users_data":user_data}
    html_data = book_template.render(context)
    return HttpResponse(html_data)   

def cancel_reservation(request):
    if request.method == 'POST':
        book_isbn = request.POST['isbn'] # VALUE INSIDE BRACKETS ARE ID FROM HTML TAGS
        user_email = request.POST['mail_id']
        username = request.POST['name']
        try:
            user = BookUser.objects.get(isbn=book_isbn, email_id=user_email, name = username)
            user.delete()
            print("           ",user)
            # user = BookUser(isbn=book_isbn, email_id=user_email, name=username)
            book_save = Book.objects.get(isbn=book_isbn)
            # print("             ",book_save)
            # print("             ",user)
            book_save.books_count+=1
            book_save.save()
            return HttpResponseRedirect("/success")
        except:
            return HttpResponseRedirect("/fail")
    else:
        return render(request, "cancel.html")     