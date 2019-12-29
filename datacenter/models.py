from django.db import models
from datetime import datetime, timezone

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )


def is_visit_long(visit, minutes=60):
    if visit.leaved_at is not None:
        delta_mintues = ((visit.leaved_at - visit.entered_at).total_seconds() / 60)
    else:
        delta_mintues = datetime.now(timezone.utc) - visit.leaved_at

    if delta_mintues > minutes:
            return True
    return False


def get_duration(visit):
    return  datetime.now(timezone.utc) - visit.entered_at


def format_duration(duration):
    hours, minutes = duration.seconds // 3600, int(duration.seconds % 3600 / 60.0)
    return '{}ч {}мин'.format(hours, minutes)
