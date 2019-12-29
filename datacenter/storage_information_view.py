from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datetime import datetime, timezone
from .models import is_visit_long, format_duration, get_duration


def storage_information_view(request):
    # Программируем здесь
    non_closed_visits = []
    x_non_closed_visits = Visit.objects.filter(leaved_at=None)
    for visit in x_non_closed_visits:
        is_visit_long(visit)
        non_closed_visits.append(
            {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit))
        }
    ) 
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }


    return render(request, 'storage_information.html', context)



