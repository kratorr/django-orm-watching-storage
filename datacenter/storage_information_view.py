from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datetime import datetime, timezone
from .models import format_duration, get_duration, is_visit_long


def storage_information_view(request):
    non_closed_visits = []
    non_closed_visits_objects = Visit.objects.filter(leaved_at=None)
    for visit in non_closed_visits_objects:
        non_closed_visits.append(
            {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit)
        }
    ) 
    context = {
        "non_closed_visits": non_closed_visits,
    }


    return render(request, 'storage_information.html', context)



