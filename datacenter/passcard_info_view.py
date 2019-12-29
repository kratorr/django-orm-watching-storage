from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .models import is_visit_long, format_duration, get_duration

def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)


    this_passcard_visits = []
    for visit in visits:
        this_passcard_visits.append(       
            {
            "entered_at": visit.entered_at,
            "duration": format_duration(get_duration(visit)),
            "is_strange": is_visit_long(visit)
        }
        )

    
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
