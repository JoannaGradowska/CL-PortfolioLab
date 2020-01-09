from django.shortcuts import render
from django.views.generic.base import View

from charity_donation.models import Donation


class LandingPage(View):
    def get(self, request):
        donations = Donation.objects.all()
        bags = 0
        for bag in donations:
            bags += bag.quantity
        i = []
        for d in donations:
            if d.institution_id not in i:
                i.append(d.institution_id)
        organizations = len(i)
        return render(request, 'index.html', context={
            "bags": bags,
            "organizations": organizations,
        })


class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')
