import socket

def _textarea_to_listr(text, check_ip=False):
    text = list(set(filter(lambda x:x!='', map(lambda x:str(x).strip(), text.split('\r\n')))))
    if check_ip:
        IP = []
        for item in text:
            if _is_valid_ipv4_address(item): IP.append(item)
        return '|'.join(sorted(IP))
    return '|'.join(sorted(text))

def _is_valid_ipv4_address(address):
    try:
        addr= socket.inet_pton(socket.AF_INET, address)
    except AttributeError:
        try:
            addr= socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:
        return False 
    return True

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

MINUTE = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
'15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
'28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
'41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53',
'54', '55', '56', '57', '58', '59']

HOUR = ['*', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']

