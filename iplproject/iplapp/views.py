from django.shortcuts import render,redirect

from iplapp.models import Player

# Create your views here.
def home_view(request):
    return render(request,'iplapp/home.html')



def create_view(request):
      if (request.method=="POST"):
         print(request.POST)
         j=request.POST.get("Jno")
         pn=request.POST.get("pn")
         r=request.POST.get("rn")
         w=request.POST.get("wn")
         t=request.POST.get("tn")
         obj = Player(Jno=j,pname=pn,runs=r,wickets=w,tname=t)
         obj.save()
         return redirect("/display/")
       
      return render(request,"iplapp/create.html")
        
   
        
   
def display_view(request):
    ipldb= Player.objects.all()
    context={"ipldb":ipldb}
    return render(request,"iplapp/display.html",context)

def update_view(request,id):
    print("Update in progress",id)
    ipldb=Player.objects.get(Jno =id)
    context={'ipldb':ipldb}
    
    if request.method == "POST":
        print(request.POST)
        ipldb.pname = request.POST.get("pn")
        ipldb.runs = request.POST.get("rn")
        ipldb.wickets = request.POST.get("wn")
        ipldb.tname = request.POST.get("tn")
        ipldb.save()
        return redirect("/display/")
    
    return render(request,"iplapp/update.html",context)

def delete_view(request,id):
    obj=Player.objects.get(Jno =id)
    obj.delete()
    
    print("delete in progress",id)
    return redirect("/display/")
    




