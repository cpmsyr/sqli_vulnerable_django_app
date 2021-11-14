from django.shortcuts import render
from vulnerable_app.models import Part


def searchparts(request):
    return render(request, "partsearch.html")

# SQL Injection Vulnerable
def parts(request):
    #searchtext = "%" + request.POST['searchText'] + "%"
    #sql = "Select * FROM part p where p.name like %s"
    searchtext = request.POST['searchText']
    sql = ("""select * from part p where p.name='%s';""" %(searchtext))
    dsparts = Part.objects.raw(sql)
    #dsparts = Part.objects.raw(sql, [searchtext])
    #dsparts = Part.objects.all()
    return render(request, "partsearch.html", {'data': dsparts})

# Using ORM Model for Security


"""
def parts(request):
    searchtext = request.POST['searchText']
    #searchtext = '%Prop%'
    dsparts = Part.objects.all()
    return render(request, "partsearch.html", {'data': dsparts})
    """