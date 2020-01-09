from django.shortcuts import render
from django.views.generic.base import View

from charity_donation.models import Donation


class LandingPage(View):
    def get(self, request):
        donations = Donation.objects.all()
        bags = 0
        for bag in donations:
            bags += bag.quantity
        return render(request, 'index.html', context={
            "bags": bags
        })


class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')
