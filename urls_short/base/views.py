from django.shortcuts import render,redirect
from .models import Urls
import shortuuid

# Create your views here.
def urlshort(request):
    newurl = Urls.objects.all()
    if request.method=='POST':
        newurl = Urls.objects.create(
            id = shortuuid.ShortUUID().random(length=5),
            orgurl = request.POST.get('orgurl'),
        )
        newurl.save()
        return redirect(newurl.orgurl)
    
    context = {"orgurl":newurl,"currectUrl":request}
    return render(request,'index.html',context)

def red_url(request,pk):
    url_object  = Urls.objects.get(id=pk)
    url_object.no_clicks = url_object.no_clicks + 1
    url_object.save()
    
    return redirect(url_object.orgurl)