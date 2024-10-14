import re
import json
import typing
import requests
import subprocess
from wb_base_data import wbBaseData

@typing.overload
def cf_clearance_reverse(domain, siteKey, useragent: typing.Optional[str]) -> tuple[str, str]:
    ...

def cf_clearance_reverse(domain, siteKey, client_request=None, *args, **kwargs) -> tuple[str, str]:
    #print(domain, siteKey, client_request, args, kwargs)
    base_data = wbBaseData(domain.replace('https://', ''), *args, **kwargs)

    str_data = json.dumps(base_data, separators=(',', ':'))
    result = subprocess.run(
        ['node', 'wb_encrypter.js', str_data, siteKey], 
        capture_output=True, 
        text=True
    )
    wb = result.stdout.strip()
    #https://www.support.kogama.com/cdn-cgi/challenge-platform/h/b/scripts/jsd/62ec4f065604/main.js?
    r = client_request.get(f'https://www.support.kogama.com/cdn-cgi/challenge-platform/h/b/scripts/jsd/62ec4f065604/main.js?')
    html_site = r.text
    cf_ray = r.headers['CF-RAY'].split('-')[0]

    for i,v in enumerate(html_site.split(',/')):
        if v.startswith('0.'):
            s_param = v.split('/,')[0]
            break

    return wb, s_param, cf_ray

def get_cf_cookie(domain, siteKey, client_request=None, *args, **kwargs):
    wb, s_param, cf_ray = cf_clearance_reverse(domain, siteKey, client_request, *args, **kwargs)

    payload = {
        'wb': wb,
        's': s_param
    }
    jsd = client_request.post(
        f'https://www.support.kogama.com/cdn-cgi/challenge-platform/h/b/jsd/r/{cf_ray}',
        #headers={
        #    'content-type': 'application/json'
        #},
        json=payload
    )
    return jsd.cookies['cf_clearance'], cf_ray
