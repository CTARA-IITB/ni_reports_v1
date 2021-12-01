from django.http import response
from django.shortcuts import render,redirect
from categories.models import UtAreaEn
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models import Q

def articles(request):
    return render(request,'articles.html')

def dataUsersWorkshop(request):
    return render(request,'dataUsersWorkshop.html')

def referenceDocuments(request):
    return render(request,'referenceDocuments.html')

def questionnaire(request):
    return render(request,'questionnaire.html')

def factsheets(request):
    india=UtAreaEn.objects.values('area_id','area_name').filter(area_parent_nid=-1)
    states=UtAreaEn.objects.values('area_id','area_name').filter(area_parent_nid=1).filter(~Q(area_name="Andaman & Nicobar Islands")).filter(~Q(area_name="Chandigarh")).filter(~Q(area_name="Dadra and Nagar Haveli")).filter(~Q(area_name="Daman and Diu")).filter(~Q(area_name="Lakshadweep")).filter(~Q(area_name="Puducherry")).order_by('area_name')
    for i in range(len(states)):
        individual_name=states[i]['area_name'].split()
        str=''
        flag=True
        if len(individual_name)>1:
            for s in individual_name:
                if flag:
                    str+=s +'-'
                    flag=False
                else:
                    str+=s
                    flag=True
        else :
            str=individual_name[0]
        states[i]['area_id'] = '/static_files/factsheets/CNNS-v6-factsheet-' + str + '.pdf'
    for i in range(len(india)):
        india[i]['area_id']=  '/static_files/factsheets/CNNS-v6-factsheet-' + india[i]['area_name'] + '.pdf'
    return render(request,'factsheets.html',{'states':states,'india':india})

def index(request):
    return render(request,'index.html')

def keyFindings(request):
    return render(request,'keyFindings.html')

def presentations(request):

    states=UtAreaEn.objects.values('area_id','area_name').filter(area_parent_nid=1).filter(~Q(area_name="Andaman & Nicobar Islands")).filter(~Q(area_name="Chandigarh")).filter(~Q(area_name="Dadra and Nagar Haveli")).filter(~Q(area_name="Daman and Diu")).filter(~Q(area_name="Lakshadweep")).filter(~Q(area_name="Puducherry")).order_by('area_name')

    for i in range(len(states)):
        individual_name=states[i]['area_name'].split()
        str=''
        flag=True
        if len(individual_name)==2:
            for s in individual_name:
                if flag:
                    str+=s +'_'
                    flag=False
                else:
                    str+=s
        elif len(individual_name)==3:
            temp=2
            for s in individual_name:
                if temp:
                    str+=s +'_'
                    temp-=1
                    continue
                else:
                    str+=s
        else :
            str=individual_name[0]
        states[i]['area_id'] = '/static_files/presentations/CNNS_Presentations_' + str + '.pdf'
    return render(request,'presentations.html',{'states':states})

def report(request):
    return render(request,'report.html')

def stateAndDistrict (request):

    selected_state_value='India'
    india=UtAreaEn.objects.values('area_id','area_name').filter(area_parent_nid=-1)
    states=UtAreaEn.objects.values('area_id','area_name','area_nid').filter(area_parent_nid=1).order_by('area_name')

    for i in range(len(states)):
        states[i]['area_id'] = '/static_files/stateAndDistrict/NutritionInfo_' + states[i]['area_id']+ '_' + states[i]['area_name'] + '.pdf'
    for i in range(len(india)):
        india[i]['area_id']= '/static_files/stateAndDistrict/NutritionInfo_' + india[i]['area_id']+ '_' + india[i]['area_name'] + '.pdf'

    if request.method == 'POST':

        try:
            selected_state_value=request.POST['selected_state']
        except MultiValueDictKeyError:
           selected_state_value = ''

        if selected_state_value!='India':
            areaId=UtAreaEn.objects.values('area_nid').filter(area_name=selected_state_value).first()
            id=areaId['area_nid']
            district=UtAreaEn.objects.values('area_id','area_name').filter(area_parent_nid=id).order_by('area_name')
            for i in range(len(district)):
                district[i]['area_id']= '/static_files/stateAndDistrict/NutritionInfo_' + district[i]['area_id']+ '_' + district[i]['area_name'] + '.pdf'
            return render(request,'stateAndDistrict.html',{'states':states,'india':india,'district':district,'selected_state_value':selected_state_value})
        else :
            return render(request,'stateAndDistrict.html',{'states':states,'india':india,'selected_state_value':selected_state_value})
    else :
        return render(request,'stateAndDistrict.html',{'states':states,'india':india,'selected_state_value':selected_state_value})


def thematicReport(request):
    return render(request,'thematicReport.html')

def nfhsfactsheets(request):
    # states=UtAreaEn.objects.values('area_id','area_name').filter(area_parent_nid=1).filter(~Q(area_name="Arunachal Pradesh")).filter(~Q(area_name="Chandigarh")).filter(~Q(area_name="Chhattisgarh")).filter(~Q(area_name="Delhi")).filter(~Q(area_name="Haryana")).filter(~Q(area_name="Jharkhand")).filter(~Q(area_name="Lakshadweep")).filter(~Q(area_name="Madhya Pradesh")).filter(~Q(area_name="Orissa")).filter(~Q(area_name="Puducherry")).filter(~Q(area_name="Punjab")).filter(~Q(area_name="Rajasthan")).filter(~Q(area_name="Tamil Nadu")).filter(~Q(area_name="Uttar Pradesh")).filter(~Q(area_name="Uttarakhand")).order_by('area_name')
    # factsheets = ["NFHS-5_AN.csv","NFHS-5_AP.csv","NFHS-5_AS.csv","NFHS-5_BR.csv","NFHS-5_DD.csv","NFHS-5_DD.csv","NFHS-5_GA.csv","NFHS-5_GJ.csv","NFHS-5_HP.csv","NFHS-5_JK.csv","NFHS-5_KA.csv","NFHS-5_KL.csv","NFHS-5_MH.csv","NFHS-5_MN.csv","NFHS-5_ML.csv","NFHS-5_MZ.csv","NFHS-5_NL.csv","NFHS-5_SK.csv","NFHS-5_TG.csv","NFHS-5_TR.csv","NFHS-5_WB.csv"]
    # state_factsheet = zip(states,factsheets)
    states = {"AP" : "Andhra Pradesh","AR" : "Arunachal Pradesh", "AS" : "Assam","BR" : "Bihar","CT" : "Chhattisgarh","GA" : "Goa","GJ" : "Gujarat","HR" : "Haryana","HP" : "Himachal Pradesh","JH" : "Jharkhand", "KA" : "Karnataka","KL" : "Kerala", "MP" : "Madhya Pradesh","MH" : "Maharashtra","MN" : "Manipur", "ML" : "Meghalaya","MZ" : "Mizoram", "NL" : "Nagaland","OR" : "Odisha", "PB" : "Punjab", "RJ" : "Rajasthan","SK" : "Sikkim","TN" : "Tamil Nadu", "TL" : "Telangana","TR" : "Tripura","UP" : "Uttar Pradesh", "UT" : "Uttarakhand", "WB" : "West Bengal","AN" : "Andaman Nicobar Islands","DD" : "Dadra Nagar Haveli Daman Diu","DL" : "NCT Delhi","JK" : "Jammu Kashmir", "LH" : "Ladakh", "PY" : "Puducherry"}
    context = {'states': states}
    return render(request,'nfhsfactsheets.html',context)
