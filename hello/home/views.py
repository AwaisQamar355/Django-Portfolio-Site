from django.shortcuts import render,HttpResponse,redirect
from home.models import Subscribe
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from home.models import SignUp
# Create your views here.
def home(request):
    HttpResponse("Hello Welcome to your home page")
    # if request.user.is_anonymous:
    #     return redirect('home.html')
    if request.method == "POST":
        email = request.POST.get('email')
        home = Subscribe(email = email , date = datetime.today())
        home.save()
    return render(request,'home.html')
def about(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'about.html')
def contact(request):
    HttpResponse("Hello Welcome to your home page")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        subject = request.POST.get("subject")
        textarea = request.POST.get("textarea")
        contact = Contact(name = name , email = email , phone = phone , password  = password , subject = subject , textarea=textarea , date = datetime.today())
        contact.save()
        messages.success(request, "Thank You!")
    return render(request,'contact.html')
def gear(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'gear.html')
def loginuser(request):
    HttpResponse("Hello Welcome to your home page")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request,user)
            return redirect("home.html")
        else:
            return redirect('signin.html')
            return redirect('login.html')
            
        

    return render(request,'login.html')
def signin(request):
    HttpResponse("Hello Welcome to your home page")
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repeatpassword = request.POST.get("repeatpassword")
        
        sign = SignUp(username=username , email = email , password =  password , repeatpassword = repeatpassword ,date = datetime.today())
        sign.save()

        if User.objects.filter(username = username).exists():
            error_message = 'Username already taken. Please choose a different username.'
            return render(request , 'signin.html' ,{'error_message' : error_message})
        
        if password != repeatpassword:
            return HttpResponse("Your Password and confirm password are not the same!")
        
        else:
            myuser = User.objects.create_user(username,email,password)
            myuser.save()
        return redirect('login.html')
    return render(request,'signin.html')
def logoutuser(request):
    HttpResponse("Hello Welcome to your home page")
    logout(request)
    if request.user.is_anonymous:
        return redirect('login.html')
    return render(request,'logout.html')
def serices(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'serices.html')
def sorcecode(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'sorcecode.html')
def thanku(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'thanku.html')

def html(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'html.html')

def css(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'css.html')

def c(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'c.html')

def clangu(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'clangu.html')

def python(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'python.html')

def js(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'js.html')

def react(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'react.html')
def java(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'java.html')


def htmlworking(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlworking.html')

def htmlinstall(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlinstall.html')

def htmlexecution(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlexecution.html')
def htmltags(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmltags.html')
def htmlelement(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlelement.html')

def htmlatri(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlatri.html')

def htmlcomet(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlcomet.html')
def htmlid(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlid.html')
def skelten(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'skelten.html')

def heading(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'heading.html')

def para(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'para.html')
def horizatal(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'horizatal.html')
def line(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'line.html')

def anchor(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'anchor.html')

def img(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'img.html')
def pre(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'pre.html')
def htmlinline(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlinline.html')

def htmllock(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmllock.html')

def htmllist(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmllist.html')
def htmlorderlist(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlorderlist.html')
def htmlunorder(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlunorder.html')

def htmldefina(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmldefina.html')

def htmltale(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmltale.html')
def htmlmoretale(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlmoretale.html')
def htmlform(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlform.html')

def htmlinput(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlinput.html')

def htmltextarea(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmltextarea.html')
def htmlmoreform(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlmoreform.html')
def htmlmatatag(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlmatatag.html')

def htmllink(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmllink.html')

def htmlvedio(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlvedio.html')
def htmlsvg(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlsvg.html')
def htmliframs(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmliframs.html')

def htmlcodetag(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlcodetag.html')

def htmlsementic(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlsementic.html')
def htmlcanvas(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlcanvas.html')
def htmlgloal(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlgloal.html')

def htmlentites(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlentites.html')

def htmlquotation(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlquotation.html')
def htmlta(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'htmlta.html')

def cssfirst(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssfirst.html')

def csswork(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'csswork.html')
def csssyntex(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'csssyntex.html')

def cssways(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssways.html')

def cssselector(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssselector.html')
def csscoments(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'csscoments.html')
def cssspecific(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssspecific.html')


def csscolor(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'csscolor.html')

def cssbgcolor(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssbgcolor.html')
def cssborder(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssborder.html')
def cssimages(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssimages.html')
def cssvideo(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssvideo.html')

def cssfonts(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssfonts.html')
def csstext(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'csstext.html')
def cssboxmod(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssboxmod.html')
def csspadinbg(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'csspadinbg.html')

def cssmargin(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssmargin.html')
def csshover(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'csshover.html')
def csscurser(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'csscurser.html')
def csslist(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'csslist.html')

def cssblink(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssblink.html')
def csscombina(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'csscombina.html')
def csspesudo(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'csspesudo.html')
def cssbutbtbon(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssbutbtbon.html')

def cssoverfloaw(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssoverfloaw.html')
def cssfloat(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssfloat.html')
def cssimportant(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssimportant.html')
def cssmathfunction(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssmathfunction.html')

def csssize(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'csssize.html')
def csszindex(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'csszindex.html')
def csspbositing(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'csspbositing.html')
def cssform(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssform.html')

def cssnav(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssnav.html')
def cssimportant(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssimportant.html')

def cssdisp(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssdisp.html')
def cssflex(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssflex.html')
def cssgrid(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssgrid.html')
def cssmedia(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssmedia.html')
def cssdtran(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssdtran.html')
def csstran(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'csstran.html')
def cssorderim(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssorderim.html')
def cssgrandan(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssgrandan.html')
def cssinherit(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssinherit.html')
def cssshadow(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssshadow.html')
def csstool(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'csstool.html')
def cssmasking(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssmasking.html')
def csspaginat(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'csspaginat.html')
def cssmediaqu(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssmediaqu.html')

def cssanimation(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'cssanimation.html')

def question(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'question.html')







