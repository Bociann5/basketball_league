import os, django

def set_up_django():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basketball_league.settings")
    django.setup()