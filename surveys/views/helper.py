def get_ip(request):
    # grab ip address of person
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = None

    if forwarded_for:
        ip = forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip
