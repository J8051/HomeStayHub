from django.shortcuts import render
from .models import Accomodations


# Create your views here.
def index(request):
  accomodations = Accomodations.objects.all()
  return render(request, 'accomodations/index.html', {
    'accomodations': accomodations
  })

def accomodation_details(request, place_slug):
    selectedBook = Accomodations.objects.get(slug=place_slug)
    return render(request, 'accomodations/accomodation-details.html', {
        'accomodation': selectedBook
    })
  