from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views import generic
from django.shortcuts import render, get_object_or_404

from polls.models import company 

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_vendor_list'

	def get_queryset(self):
		return Vendor.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = company
	template_name = 'polls/detail.html'


