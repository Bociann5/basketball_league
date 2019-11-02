def set_up_django():
    import django, os, sys

    root_path = '/'.join(os.getcwd().split('/')[:-1])
    path_for_settigns = f'{root_path}/basketball_league'
    print(os.getcwd())

    sys.path.insert(0, path_for_settigns)
    sys.path.insert(0, root_path)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    django.setup()
