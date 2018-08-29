from django.shortcuts import render
import csv

# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
##    # Generate counts of some of the main objects
##    num_books=Book.objects.all().count()
##    num_instances=BookInstance.objects.all().count()
##    # Available books (status = 'a')
##    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
##    num_authors=Author.objects.count()  # The 'all()' is implied by default.
##    
    # Render the HTML template index.html with the data in the context variable
    with open('../Snow day model/result.csv', 'r') as fin:
        reader = csv.reader(fin)
        lines = [line for line in reader]
        
    prob = int(float(lines[0][0]) * 100 + 0.5)
    return render(
        request,
        'index.html',
        context={'prob': prob, 'img': '../static/snowflake.png' if prob > 50 else '../static/banana.png'}
    )
