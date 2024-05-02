from django.http import HttpResponse
from django.template import loader
from .models import Members


def helo(request):
    template = loader.get_template('felix.html')
    return HttpResponse(template.render())


def members(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('all_members.html')
    
    context= {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

#tables
def table(request):
    mydata = Members.objects.all()
    template = loader.get_template('table.html')
    context = {
        'mymembers' : mydata,
    }
    return HttpResponse(template.render(context, request))

def firstname(request):
    mydata = Members.objects.filter( firstname= 'Felix')
    mydata = Members.objects.all().order_by("-lastname")
    template = loader.get_template('firstname.html')
    
    context = {
        'firstname' : mydata, 
    }
    
    return HttpResponse(template.render(context, request))
    


#For testing
def testing(request):
   
    mymembers = Members.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
        'firstname' : 'Felix',
        'lastname' : 'Mokaya',
        'mymembers' : mymembers,
        'members' : mymembers,
    }
    return HttpResponse(template.render(context, request))