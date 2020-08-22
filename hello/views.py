from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    num_visit = request.session.get('visitCount', 0) + 1
    request.session['visitCount'] = num_visit
    if num_visit > 4: del(request.session['visitCount'])
    resp = HttpResponse('view count='+str(num_visit))
    resp.set_cookie('dj4e_cookie', '1340ccf2', max_age=1000)
    return resp
