#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.db.models import Max, Min, Avg, Count
from kaori_record.models import Record, Member, Competition, Event, AllBestRecord, FormalBestRecord, EventForRank

def pockemon_result(request):

    name = request.POST['name']
    year = request.POST['year']
    result_member = Member.objects.get(member_name=request.POST['name'], member_year=request.POST['year'])
    best_records_all = AllBestRecord.objects.select_related().filter(member=result_member.member_id).order_by('best_record')
    records_gender_all = AllBestRecord.objects.filter(member__member_gender=result_member.member_gender).order_by('best_record')
    target_events = best_records_all.values_list('event__event_name', 'event__event_distance')

    free_50 = best_records_all.filter(event__event_name='자유형', event__event_distance='50')
    free_100 = best_records_all.filter(event__event_name='자유형', event__event_distance='100')
    free_200 = best_records_all.filter(event__event_name='자유형', event__event_distance='200')
    fly_50 = best_records_all.filter(event__event_name='접영', event__event_distance='50')
    fly_100 = best_records_all.filter(event__event_name='접영', event__event_distance='100')
    breast_50 = best_records_all.filter(event__event_name='평영', event__event_distance='50')
    breast_100 = best_records_all.filter(event__event_name='평영', event__event_distance='100')
    back_50 = best_records_all.filter(event__event_name='배영', event__event_distance='50')
    back_100 = best_records_all.filter(event__event_name='배영', event__event_distance='100')
    im_100 = best_records_all.filter(event__event_name='개인혼영', event__event_distance='100')
    im_200 = best_records_all.filter(event__event_name='개인혼영', event__event_distance='200')
    kick_50 = best_records_all.filter(event__event_name='발차기', event__event_distance='50')
    dolphine_50 = best_records_all.filter(event__event_name='돌핀킥', event__event_distance='50')
    bifin_50 = best_records_all.filter(event__event_name='바이핀', event__event_distance='50')
    bifin_100 = best_records_all.filter(event__event_name='바이핀', event__event_distance='100')
    bifin_200 = best_records_all.filter(event__event_name='바이핀', event__event_distance='200')
    open_water_3km = best_records_all.filter(event__event_name='바다수영', event__event_distance='3000')

    free_50_m = ["0\'26\"50", "0\'29\"00", "0\'32\"00", "0\'35\"00"]
    free_100_m = ["0\'59\"00", "1\'03\"00", "1\'08\"00", "1\'13\"00"]
    free_200_m = ["2\'07\"00", "2\'22\"00", "2\'34\"00"]
    fly_50_m = ["0\'27\"50", "0\'29\"50", "0\'32\"00", "0\'35\"00"]
    fly_100_m = ["1\'03\"00", "1\'07\"00", "1\'12\"00", "1\'20\"00"]
    breast_50_m = ["0\'33\"00", "0\'35\"50", "0\'39\"00", "0\'44\"00"]
    breast_100_m = ["1\'15\"00", "1\'20\"00", "1\'27\"00", "1\'35\"00"]
    back_50_m = ["0\'31\"50", "0\'34\"00", "0\'37\"00", "0\'41\"00"]
    back_100_m = ["1\'08\"00", "1\'12\"00", "1\'14\"00", "1\'24\"00"]
    im_100_m = ["1\'05\"00", "1\'09\"00", "1\'14\"00"]
    im_200_m = ["2\'25\"00", "2\'45\"00", "3\'10\"00"]
    kick_50_m = ["0\'35\"00", "0\'40\"00", "0\'45\"00"]
    dolphine_50_m = ["0\'35\"00", "0\'40\"00", "0\'45\"00"]
    bifin_50_m = ["0\'20\"00", "0\'24\"00", "0\'27\"00"]
    bifin_100_m = ["0\'40\"00", "0\'43\"00", "0\'54\"00"]
    bifin_200_m = ["1\'25\"00", "1\'31\"00", "1\'57\"00"]
    open_water_3km_m = ["1\'25\"00", "1\'31\"00", "1\'57\"00"]

    free_50_f = ["0\'31\"50", "0\'34\"00", "0\'37\"00", "0\'42\"00"]
    free_100_f = ["1\'10\"00", "1\'14\"00", "1\'19\"00", "1\'24\"00"]
    free_200_f = ["2\'30\"00", "2\'45\"00", "2\'57\"00"]
    fly_50_f = ["0\'32\"50", "0\'34\"50", "0\'37\"00", "0\'40\"00"]
    fly_100_f = ["1\'14\"00", "1\'18\"00", "1\'23\"00", "1\'34\"00"]
    breast_50_f = ["0\'38\"00", "0\'40\"50", "0\'44\"00", "0\'49\"00"]
    breast_100_f = ["1\'26\"00", "1\'31\"00", "1\'38\"00", "1\'46\"00"]
    back_50_f = ["0\'36\"50", "0\'39\"00", "0\'42\"00", "0\'46\"00"]
    back_100_f = ["1\'19\"00", "1\'23\"00", "1\'25\"00", "1\'35\"00"]
    im_100_f = ["1\'16\"00", "1\'20\"00", "1\'25\"00"]
    im_200_f = ["2\'48\"00", "3\'08\"00", "3\'33\"00"]
    kick_50_f = ["0\'35\"00", "0\'40\"00", "0\'45\"00"]
    dolphine_50_f = ["0\'35\"00", "0\'40\"00", "0\'45\"00"]
    bifin_50_f = ["0\'22\"00", "0\'26\"00", "0\'29\"00"]
    bifin_100_f = ["0\'44\"00", "0\'47\"00", "0\'58\"00"]
    bifin_200_f = ["1\'33\"00", "1\'39\"00", "2\'05\"00"]
    open_water_3km_f = ["1\'25\"00", "1\'31\"00", "1\'57\"00"]

    free_50_r = records_gender_all.filter(event__event_name="자유형", event__event_distance="50").order_by('best_record')
    free_100_r = records_gender_all.filter(event__event_name="자유형", event__event_distance="100").order_by('best_record')
    free_200_r = records_gender_all.filter(event__event_name="자유형", event__event_distance="200").order_by('best_record')
    fly_50_r = records_gender_all.filter(event__event_name="접영", event__event_distance="50").order_by('best_record')
    fly_100_r = records_gender_all.filter(event__event_name="접영", event__event_distance="100").order_by('best_record')
    breast_50_r = records_gender_all.filter(event__event_name="평영", event__event_distance="50").order_by('best_record')
    breast_100_r = records_gender_all.filter(event__event_name="평영", event__event_distance="100").order_by('best_record')
    back_50_r = records_gender_all.filter(event__event_name="배영", event__event_distance="50").order_by('best_record')
    back_100_r = records_gender_all.filter(event__event_name="배영", event__event_distance="100").order_by('best_record')
    im_100_r = records_gender_all.filter(event__event_name="개인혼영", event__event_distance="100").order_by('best_record')
    im_200_r = records_gender_all.filter(event__event_name="개인혼영", event__event_distance="200").order_by('best_record')
    bifin_100_r = records_gender_all.filter(event__event_name="바이핀", event__event_distance="100").order_by('best_record')

    free_50_rank = 1
    found = 0
    if len(free_50_r) == 0 :
        free_50_rank = 1000
    for r in free_50_r :
        if request.POST['name'] == r.member.member_name :
            found = 1
            break
        else :
            free_50_rank = free_50_rank + 1
    if found == 0 :
        free_50_rank = 1000

    free_100_rank = 1
    found = 0
    if len(free_100_r) == 0 :
        free_100_rank = 1000
    for r in free_100_r :
        if request.POST['name'] == r.member.member_name :
            found = 1
            break
        else :
            free_100_rank = free_100_rank + 1
    if found == 0 :
        free_100_rank = 1000

    free_200_rank = 1
    found = 0
    if len(free_200_r) == 0 :
        free_200_rank = 1000
    for r in free_200_r :
        if request.POST['name'] == r.member.member_name :
            found = 1
            break
        else :
            free_200_rank = free_200_rank + 1
    if found == 0 :
        free_200_rank = 1000

    fly_50_rank = 1
    found = 0
    if len(fly_50_r) == 0 :
        fly_50_rank = 1000
    for r in fly_50_r :
        if request.POST['name'] == r.member.member_name :
            found = 1
            break
        else :
            fly_50_rank = fly_50_rank + 1
    if found == 0 :
        fly_50_rank = 1000

    fly_100_rank = 1
    found = 0
    if len(fly_100_r) == 0 :
        fly_100_rank = 1000
    for r in fly_100_r :
        if request.POST['name'] == r.member.member_name :
            found = 1
            break
        else :
            fly_100_rank = fly_100_rank + 1
    if found == 0 :
        fly_100_rank = 1000

    breast_50_rank = 1
    found = 0
    if len(breast_50_r) == 0 :
        breast_50_rank = 1000
    for r in breast_50_r :
        if request.POST['name'] == r.member.member_name :
            found = 1
            break
        else :
            breast_50_rank = breast_50_rank + 1
    if found == 0 :
        breast_50_rank = 1000

    breast_100_rank = 1
    found = 0
    if len(breast_100_r) == 0 :
        breast_100_rank = 1000
    for r in breast_100_r :
        if request.POST['name'] == r.member.member_name :
            found = 1
            break
        else :
            breast_100_rank = breast_100_rank + 1
    if found == 0 :
        breast_100_rank = 1000

    back_50_rank = 1
    found = 0
    if len(back_50_r) == 0 :
        back_50_rank = 1000
    for r in back_50_r :
        if request.POST['name'] == r.member.member_name :
            found = 1
            break
        else :
            back_50_rank = back_50_rank + 1
    if found == 0 :
        back_50_rank = 1000

    back_100_rank = 1
    found = 0
    if len(back_100_r) == 0 :
        back_100_rank = 1000
    for r in back_100_r :
        if request.POST['name'] == r.member.member_name :
            found = 1
            break
        else :
            back_100_rank = back_100_rank + 1
    if found == 0 :
        back_100_rank = 1000

    # On working
    bifin_100_rank = 10
    for r in bifin_100_r :
        if request.POST['name'] == r.member.member_name :
            break
        else :
            bifin_100_rank = bifin_100_rank + 1

    im_100_rank = 1
    found = 0
    if len(im_100_r) == 0 :
        im_100_rank = 1000
    for r in im_100_r :
        if request.POST['name'] == r.member.member_name :
            found = 1
            break
        else :
            im_100_rank = im_100_rank + 1
    if found == 0 :
        im_100_rank = 1000

    im_200_rank = 1
    found = 0
    if len(im_200_r) == 0 :
        im_200_rank = 1000
    for r in im_200_r :
        if request.POST['name'] == r.member.member_name :
            found = 1
            break
        else :
            im_200_rank = im_200_rank + 1
    if found == 0 :
        im_200_rank = 1000

    context = {
        'name':name,
        'year':year,
        'gender':result_member.member_gender,
        'year_2':year[-2:],
        'free_50':free_50,
        'free_100':free_100,
        'free_200':free_200,
        'fly_50':fly_50,
        'fly_100':fly_100,
        'breast_50':breast_50,
        'breast_100':breast_100,
        'back_50':back_50,
        'back_100':back_100,
        'im_100':im_100,
        'im_200':im_200,
        'dolphine_50':dolphine_50,
        'kick_50':kick_50,
        'bifin_50':bifin_50,
        'bifin_100':bifin_100,
        'bifin_200':bifin_200,
        'open_water_3km':open_water_3km,
        'free_50_m':free_50_m,
        'free_100_m':free_100_m,
        'free_200_m':free_200_m,
        'fly_50_m':fly_50_m,
        'fly_100_m':fly_100_m,
        'breast_50_m':breast_50_m,
        'breast_100_m':breast_100_m,
        'back_50_m':back_50_m,
        'back_100_m':back_100_m,
        'im_100_m':im_100_m,
        'im_200_m':im_200_m,
        'dolphine_50_m':dolphine_50_m,
        'kick_50_m':kick_50_m,
        'bifin_50_m':bifin_50_m,
        'bifin_100_m':bifin_100_m,
        'bifin_200_m':bifin_200_m,
        'open_water_3km_m':open_water_3km_m,
        'free_50_f':free_50_f,
        'free_100_f':free_100_f,
        'free_200_f':free_200_f,
        'fly_50_f':fly_50_f,
        'fly_100_f':fly_100_f,
        'breast_50_f':breast_50_f,
        'breast_100_f':breast_100_f,
        'back_50_f':back_50_f,
        'back_100_f':back_100_f,
        'im_100_f':im_100_f,
        'im_200_f':im_200_f,
        'dolphine_50_f':dolphine_50_f,
        'kick_50_f':kick_50_f,
        'bifin_50_f':bifin_50_f,
        'bifin_100_f':bifin_100_f,
        'bifin_200_f':bifin_200_f,
        'open_water_3km_f':open_water_3km_f,
        'free_50_rank':free_50_rank,
        'free_100_rank':free_100_rank,
        'free_200_rank':free_200_rank,
        'fly_50_rank':fly_50_rank,
        'fly_100_rank':fly_100_rank,
        'breast_50_rank':breast_50_rank,
        'breast_100_rank':breast_100_rank,
        'back_50_rank':back_50_rank,
        'back_100_rank':back_100_rank,
        'im_100_rank':im_100_rank,
        'im_200_rank':im_200_rank,
        'bifin_100_rank':bifin_100_rank
    }
    return render(request, 'kaori_record/pockemon_result.html', context)

def pockemon(request):
    context = {}
    return render(request, 'kaori_record/pockemon.html', context)

def index(request):
    context = {}
    return render(request, 'kaori_record/index.html', context)

def individual_record(request):
    context = {}
    return render(request, 'kaori_record/individual_record.html', context)

def individual_record_result(request):

    result_member = Member.objects.get(member_name=request.POST['name'], member_year=request.POST['year'])
    records = Record.objects.select_related().filter(member=result_member.member_id).order_by('event__event_name', 'event__event_distance','record')
    records_formal = Record.objects.select_related().filter(member=result_member.member_id, competition__competition_formality=1).order_by('event__event_name', 'event__event_distance','record')

    best_records_all = AllBestRecord.objects.select_related().filter(member=result_member.member_id).order_by('best_record')
    best_records_formal = FormalBestRecord.objects.select_related().filter(member=result_member.member_id).order_by('best_record')

    records_gender_all = AllBestRecord.objects.filter(member__member_gender=result_member.member_gender).order_by('best_record')
    records_gender_formal = FormalBestRecord.objects.filter(member__member_gender=result_member.member_gender).order_by('best_record')

    target_events = best_records_all.values_list('event__event_name', 'event__event_distance')
    target_events_formal = best_records_formal.values_list('event__event_name', 'event__event_distance')

    competition_id = records.order_by('competition_id').values('competition_id').distinct()
    competition = Competition.objects.filter(kirokhoe=0, competition_id__in=competition_id).order_by('-competition_year')

    all_rank = []
    for target_event in target_events :
        count = 1
        temp_record = records_gender_all.filter(event__event_name=target_event[0], event__event_distance=target_event[1]).order_by('best_record')

        for r in temp_record :
            if request.POST['name'] == r.member.member_name :
                break
            else :
                count = count + 1

        all_rank.append(count)

    formal_rank = []
    for target_event in target_events_formal :
        count = 1
        temp_record2 = records_gender_formal.filter(event__event_name=target_event[0], event__event_distance=target_event[1]).order_by('best_record')

        for r in temp_record2 :
            if request.POST['name'] == r.member.member_name :
                break
            else :
                count = count + 1

        formal_rank.append(count)

    context = {'name':request.POST['name'],
               'year':request.POST['year'],
               'formality':request.POST.get('formality', False),
               'year_short':str(request.POST['year'])[-2:],
               'best_records_all':best_records_all,
               'best_records_formal':best_records_formal,
               'records':records,
               'records_formal':records_formal,
               'records_gender_all':records_gender_all,
               'records_gender_formal':records_gender_formal,
               'all_rank':all_rank,
               'formal_rank':formal_rank,
               'competition':competition
               }

    return render(request, 'kaori_record/individual_record_result.html', context)

def competition(request):

    competition_years = Competition.objects.filter(kirokhoe=0).order_by('-competition_year').values('competition_year').distinct()

    context = {
        'competition_years':competition_years
    }
    return render(request, 'kaori_record/competition.html', context)

def competition_result(request):

    year = request.POST['year'][:4]
    competitions = Competition.objects.filter(competition_year=year, kirokhoe=0).order_by('competition_id')
    kirokhoe = Competition.objects.filter(competition_year=year, kirokhoe=1).order_by('competition_id')

    competitions_id = Competition.objects.filter(competition_year=year, kirokhoe=0).order_by('competition_id').values_list('competition_id')
    relevant_records = Record.objects.filter(competition_id__in=competitions_id).order_by('competition_id', 'rank', 'member__member_name', 'event__event_name')

    kirokhoe_id = Competition.objects.filter(competition_year=year, kirokhoe=1).order_by('competition_id').values_list('competition_id')
    kirokhoe_relevant_records = Record.objects.filter(competition_id__in=kirokhoe_id).order_by('competition_id','member__member_name', 'event__event_name')


    competition_years = Competition.objects.filter(kirokhoe=0).order_by('-competition_year').values('competition_year').distinct()

    context = {
        'year':year,
        'competition_years':competition_years,
        'competitions_id':competitions_id,
        'competitions':competitions,
        'relevant_records':relevant_records,
        'kirokhoe':kirokhoe,
        'kirokhoe_id':kirokhoe_id,
        'kirokhoe_relevant_records':kirokhoe_relevant_records
    }
    return render(request, 'kaori_record/competition_result.html', context)

def ranking(request):
    context = {}
    return render(request, 'kaori_record/ranking.html', context)

def ranking_result(request):

    event_name = request.POST.get('event_name','')
    event_distance = int(request.POST.get('event_distance', 0)[:-1])
    event_gender = request.POST.get('event_gender','')
    formality = request.POST.get('formality', False)

    result_event = Event.objects.get(event_name=event_name, event_distance=event_distance)

    event_name_list = Event.objects.values('event_name').order_by('event_name').distinct()
    event_distance_list = Event.objects.values('event_distance').order_by('event_distance').distinct()
    gender_list = Member.objects.values('member_gender').order_by('member_gender').distinct()

    records_gender_all = AllBestRecord.objects.filter(event=result_event, member__member_gender=event_gender ).order_by('best_record')
    records_no_gender_all = AllBestRecord.objects.filter(event=result_event).order_by('best_record')
    records_gender_formal = FormalBestRecord.objects.filter(event=result_event, member__member_gender=event_gender ).order_by('best_record')
    records_no_gender_formal = FormalBestRecord.objects.filter(event=result_event).order_by('best_record')


    context = { 'event_name':event_name,
                'event_distance':event_distance,
                'event_gender':event_gender,
                'formality':formality,
                'records_gender_all':records_gender_all,
                'records_no_gender_all':records_no_gender_all,
                'records_gender_formal':records_gender_formal,
                'records_no_gender_formal':records_no_gender_formal,
                'event_name_list':event_name_list,
                'event_distance_list':event_distance_list,
                'gender_list':gender_list
                }

    return render(request, 'kaori_record/ranking_result.html', context)

def manage(request):
    context = {}
    return render(request, 'kaori_record/manage.html', context)