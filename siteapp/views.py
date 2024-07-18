from django.shortcuts import render
from siteapp.models import Review
# Create your views here.

def reviews(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(
        request,
        template_name="index.html",
        context=context,
    )