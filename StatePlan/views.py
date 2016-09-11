from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import Http404
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SearchForm
from StatePlan.models import TMACSP_record
from django.views.generic.list import ListView


def TMACSP(request):
    query_list = TMACSP_record.objects.all()
    subpopquery = request.GET.get("subpop")
    procatquery = request.GET.get("procat")
    srvreqquery = request.GET.get("srvreq")
    
    if subpopquery and procatquery:
        query_list = query_list.filter(
            Q(Subject_Population__iexact=subpopquery)
            )
        query_list= query_list.filter(
            Q(Program_Category__iexact=procatquery)
            )

    if subpopquery and srvreqquery:
        query_list = query_list.filter(
            Q(Subject_Population__iexact=subpopquery)
            )
        query_list= query_list.filter(
            Q(Services_Requirements__iexact=srvreqquery)
            )
    if procatquery and srvreqquery:
        query_list = query_list.filter(
            Q(Program_Category__iexact=procatquery)
            )
        query_list= query_list.filter(
            Q(Services_Requirements__iexact=srvreqquery)
            )

    if subpopquery and procatquery and srvreqquery:
        query_list = query_list.filter(
            Q(Subject_Population__iexact=subpopquery)
            )
        query_list= query_list.filter(
            Q(Program_Category__iexact=procatquery)
            ) 
        query_list=query_list.filter(
            Q(Services_Requirements__iexact=srvreqquery)
            )   

    if subpopquery or procatquery or srvreqquery:
        query_list = query_list.filter(
            Q(Subject_Population__iexact=subpopquery) |
            Q(Program_Category__iexact=procatquery) |
            Q(Services_Requirements__iexact=srvreqquery)
            ).distinct()
    return render(request,'TMACSP/TMACSP.html',{
        'query_list': query_list,
        })

def index(request):
   return render(request,'StatePlan/index.html')

def TMACSP_record_detail(request, id):
    try:
        record = TMACSP_record.objects.get(id=id)
    except TMACSP_record.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'TMACSP/TMACPS_record_detail.html', {
            'record': record,
        })



def record_list(request):
    records = Record.objects.all()
    return ListView.as_view()(request)
