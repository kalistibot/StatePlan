from django.contrib import admin

from .models import Record

class RecordAdmin(admin.ModelAdmin):
	list_display = ['Subject','Program','Section']

	# """docstring for ClassName"""
	# def __init__(self, arg):
	# 	super(ClassName, self).__init__()
	# 	self.arg = arg
		


admin.site.register(Record,RecordAdmin)

