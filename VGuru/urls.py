"""VGuru URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("webapp.urls")),
    path('kin',index.webpage1,name='webpage1'),
    path('sub',index.webpage2,name='webpage2'),
    path('11',index.webpage3,name='webpage3'),
    path('12',index.webpage3,name='webpage3'),
    path('rhymes',index.rhy,name='rhy'),
    path('numbers',index.no,name='no'),
    path('about',index.webpage4,name='webpage4'),
    path('english',index.eng1,name='eng1'),
    path('english',index.eng2,name='eng2'),
    path('english',index.eng3,name='eng3'),
    path('english',index.eng4,name='eng4'),
    path('english',index.eng5,name='eng5'),
    path('english',index.eng6,name='eng6'),
    path('english',index.eng7,name='eng7'),
    path('english',index.eng8,name='eng8'),
    path('english',index.eng9,name='eng9'),
    path('english',index.eng10,name='eng10'),
    path('maths',index.math1,name='math1'),
    path('maths',index.math2,name='math2'),
    path('maths',index.math3,name='math3'),
    path('maths',index.math4,name='math4'),
    path('maths',index.math5,name='math5'),
    path('maths',index.math6,name='math6'),
    path('maths',index.math7,name='math7'),
    path('maths',index.math8,name='math8'),
    path('maths',index.math9,name='math9'),
    path('maths',index.math10,name='math10'),
    path('science',index.sci1,name='sci1'),
    path('science',index.sci2,name='sci2'),
    path('science',index.sci3,name='sci3'),
    path('science',index.sci4,name='sci4'),
    path('science',index.sci5,name='sci5'),
    path('science',index.sci6,name='sci6'),
    path('science',index.sci7,name='sci7'),
    path('science',index.sci8,name='sci8'),
    path('science',index.sci9,name='sci9'),
    path('science',index.sci10,name='sci10'),
    path('socialscience',index.soci1,name='soci1'),
    path('socialscience',index.soci2,name='soci2'),
    path('socialscience',index.soci3,name='soci3'),
    path('socialscience',index.soci4,name='soci4'),
    path('socialscience',index.soci5,name='soci5'),
    path('socialscience',index.soci6,name='soci6'),
    path('socialscience',index.soci7,name='soci7'),
    path('socialscience',index.soci8,name='soci8'),
    path('socialscience',index.soci9,name='soci9'),
    path('socialscience',index.soci10,name='soci10'),
    path('computerscience',index.cs11,name='cs11'),
    path('computerscience',index.cs12,name='cs12'),
    path('Biology',index.bio11,name='bio11'),
    path('Biology',index.bio12,name='bio12'),
    path('Physics',index.phy11,name='phy11'),
    path('Physics',index.phy12,name='phy12'),
    path('Chemistry',index.chem11,name='chem12'),
    path('Chemistry',index.chem12,name='chem12'),
    path('Maths',index.math11,name='math11'),
    path('Maths',index.math12,name='math12'),
    path('Businessmaths',index.bus11,name='bus12'),
    path('Businessmaths',index.bus11,name='bus11'),
    path('Accountancy',index.acc11,name='acc11'),
    path('Accountancy',index.acc12,name='acc12'),
    path('ebook',index.ebk,name='ebk'),
    path('questionpapers',index.qb,name='qb'),


]
