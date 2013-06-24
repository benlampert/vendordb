from django.contrib import admin
from polls.models import company

class VendorAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 		{'fields': ['name']}),
		('Date Information', {'fields': ['pub_date']}),
		('Description', {'fields': ['description']}),
		]

	list_display = ('name', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['name', 'description']


admin.site.register(company, VendorAdmin)


