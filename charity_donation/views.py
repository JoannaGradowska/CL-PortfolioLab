from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.views.generic.base import View

from charity_donation.models import Donation, Institution, Category


class LandingPage(View):
    def get(self, request):
        donation_set = Donation.objects.aggregate(Sum('quantity'))

        supported_organizations = Institution.objects.exclude(donation__isnull=True).count()

        institutions = Institution.objects.filter()

        foundations = institutions.filter(type=1)
        organizations = institutions.filter(type=2)
        charities = institutions.filter(type=3)

        return render(request, 'index.html', context={
            "bags": donation_set.get('quantity__sum'),
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
