from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import Http404
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SearchForm
from StatePlan.models import Record, AttachmentPages_record
from django.views.generic.list import ListView



def StatePlan(request):
    query_list = Record.objects.all()
    subjectquery = request.GET.get("sq")
    programquery = request.GET.get("pq")
    
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
    return render(request,'StatePlan/StatePlan.html',{
        'query_list': query_list,
        })

def AttachmentPages(request):
    query_list = AttachmentPages_record.objects.all()
    subjectquery = request.GET.get("subq")
    servicesquery = request.GET.get("svcsq")
    
    if subjectquery and servicesquery:
        query_list = query_list.filter(
            Q(Subject__iexact=subjectquery)
            )
        query_list= query_list.filter(
            Q(Services__iexact=servicesquery)
            )
    if subjectquery or servicesquery:
        query_list = query_list.filter(
            Q(Subject__iexact=subjectquery) |
            Q(Services__iexact=servicesquery) 
            ).distinct()
    return render(request,'AttachmentPages/AttachmentPages.html',{
        'query_list': query_list,
        })



def index(request):
   return render(request,'StatePlan/index.html')

def record_detail(request, id):
    try:
        record = Record.objects.get(id=id)
    except Record.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'StatePlan/record_detail.html', {
            'record': record,
        })

def attPages_record_detail(request, id):
    try:
        record = AttachmentPages_record.objects.get(id=id)
    except AttachmentPages_record.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'AttachmentPages/attPages_record_detail.html', {
            'record': record,
        })


def record_list(request):
    records = Record.objects.all()
    return ListView.as_view()(request)
