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
    if subjectquery or programquery:
        query_list = query_list.filter(
            Q(Subject=subjectquery) |
            Q(Program=programquery) |
            Q(Section=subjectquery)
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

    # record = get_object_or_404(Record.objects.all())
    # return render(request, 'StatePlan/record_detail.html', {'record': record})(request, 'StatePlan/record_list.html', {'records': records})




def get_search(request):
    #if request.method == 'SearchForm':
    form = SearchForm(request.POST)
    #if form.is_valid():
     #   return HttpResponseRedirect('/search/')
    #else:
     #   search  = SearchForm()
    return render(request, 'StatePlan/search.html', {'form': form})


def record_list(request):
    records = Record.objects.all() #hardcoding a search term for testing
    return ListView.as_view()(request)
    #return render
    #return render(request, 'StatePlan/record_list.html', {'records':records})(request, 'StatePlan/record_list.html',{'records': record})                  #ListView.as_view() 

