from django.urls import path,include
from . import views

urlpatterns=[

    # path('',views.index,name='index'),
    path('',views.report,name='report'),
    path('articles',views.articles,name="articles"),
    path('dataUsersWorkshop',views.dataUsersWorkshop,name='dataUsersWorkshop'),
    path('factsheets',views.factsheets,name='factsheets'),
    path('keyFindings',views.keyFindings,name='keyFindings'),
    path('presentations',views.presentations,name='presentations'),
    path('stateAndDistrict',views.stateAndDistrict,name='stateAndDistrict'),
    path('thematicReport',views.thematicReport,name='thematicReport'),
    path('referenceDocuments',views.referenceDocuments,name='referenceDocuments'),
    path('questionnaire',views.questionnaire,name='questionnaire'),
    path('nfhsfactsheets',views.nfhsfactsheets,name='nfhsfactsheets'),

]
