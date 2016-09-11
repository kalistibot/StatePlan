from django.contrib import admin

from .models import TMACSP_record 

class RecordAdmin(admin.ModelAdmin):
	list_display = ['id','Subject_Population','Program_Category','Section']

	# """docstring for ClassName"""
	# def __init__(self, arg):
	#     super(ClassName, self).__init__()
	#     self.arg = arg
		
admin.site.register(TMACSP_record,RecordAdmin)

