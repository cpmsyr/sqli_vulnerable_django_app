from django.shortcuts import render
from vulnerable_app.models import Part


def searchparts(request):
    return render(request, "partsearch.html")

# SQL Injection Vulnerable


def parts(request):
    if request.POST:
        searchtext = request.POST['searchText']
        sql = ("""select * from part p where p.name='%s';""" %(searchtext))
        dsparts = Part.objects.raw(sql)
    else:
        sql = ("""select * from part;""" )
        dsparts = Part.objects.raw(sql)
    return render(request, "partsearch.html", {'data': dsparts})


# Using ORM Model for Security


#def parts(request):
    #searchtext = request.POST['searchText']
    #dsparts = Part.objects.all().filter(name=searchtext)
    #return render(request, "partsearch.html", {'data': dsparts})

