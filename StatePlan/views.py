from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import Http404
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SearchForm
from StatePlan.models import Record
from django.views.generic.list import ListView


def index(request):
    query_list = Record.objects.all()
    subjectquery = request.GET.get("sq")
    programquery = request.GET.get("pq")
    
    ## This should be after the And attempt, which isn't working now.


    if subjectquery and programquery:
        query_list = query_list.filter(
            Q(Subject__iexact=subjectquery)
            )
        query_list= query_list.filter(
            Q(Program__iexact=programquery)
            )
  


    if subjectquery or programquery:
        query_list = query_list.filter(
            Q(Subject__iexact=subjectquery) |
            Q(Program__iexact=programquery) |
            Q(Section__iexact=subjectquery)
            ).distinct()
    return render(request,'StatePlan/index.html',{
        'query_list': query_list,
        })


   
def record_detail(request, id):
    try:
        record = Record.objects.get(id=id)
    except Record.DoesNotExist:
        raise Http404('This item does not exist')

    return render(request, 'StatePlan/record_detail.html', {

            'record': record,
        })


def record_list(request):
    records = Record.objects.all() #hardcoding a search term for testing
    return ListView.as_view()(request)
    #return render
    #return render(request, 'StatePlan/record_list.html', {'records':records})(request, 'StatePlan/record_list.html',{'records': record})                  #ListView.as_view() 

