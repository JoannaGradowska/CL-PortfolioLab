from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic.base import View

from charity_donation.models import Donation, Institution, Category


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
        supported_organizations = len(i)

        institutions = Institution.objects.all()

        foundations = institutions.filter(type=1)
        organizations = institutions.filter(type=2)
        charities = institutions.filter(type=3)

        return render(request, 'index.html', context={
            "bags": bags,
            "supported_organizations": supported_organizations,
            "foundations": foundations,
            "organizations": organizations,
            "local_charities": charities,
        })


class AddDonation(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.all().order_by('id')
        institutions = Institution.objects.all()
        return render(request, 'form.html', context={
            "categories": categories,
            "institutions": institutions,
        })
