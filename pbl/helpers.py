import socket

def _textarea_to_listr(text, check_ip=False):
    text = list(set(filter(lambda x:x!='', map(lambda x:str(x).strip(), text.split('\r\n')))))
    if check_ip:
        IP = []
        for item in text:
            try:
                socket.inet_aton(item)
                IP.append(item)
            except:
                pass
        return '|'.join(sorted(IP))
    return '|'.join(sorted(text))

def build_survey(survey, IP, domain, operator, URL):

    if IP:
        IP = _textarea_to_listr(IP, check_ip=True)
        if survey.IP != IP:
            survey.IP = IP
            survey.save()
        return 'IP'

    if domain:
        domain = _textarea_to_listr(domain)
        if survey.domain != domain:
            survey.domain = domain
        if survey.operator != operator:
            survey.operator = operator
        survey.save()
        return 'domain'

    if URL:
        URL = _textarea_to_listr(URL)
        if survey.URL != URL:
            survey.URL = URL
            survey.save()
        return 'URL'


def listr_to_textarea(survey):
    IP = survey.IP.replace('|', '\r\n')
    domain = survey.domain.replace('|', '\r\n')
    operator = survey.operator
    URL = survey.URL.replace('|', '\r\n')

    return {'IP':IP, 'domain':domain, 'operator':operator, 'URL':URL}

