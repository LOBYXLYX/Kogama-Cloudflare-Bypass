import httpx
from cf_reverse import get_cf_cookie

client = httpx.Client()
client.headers = {
    'authority': 'www.support.kogama.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'es-US,es-419;q=0.9,es;q=0.8',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="129", "Google Chrome";v="129"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"iOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/129.0.6668.46 Mobile/15E148 Safari/604.1'
}


red_sk = client.get('https://www.support.kogama.com/')
client.cookies = red_sk.cookies


cf_cookie, ray = get_cf_cookie(
    'https://www.support.kogama.com/',
    'x3MU-7nK0tLQlyRoIXNDZOiPF+c26s$gdJAVzEv9qmapSuh5bwfjHYTk18eWBG4rC',
    client,
    useragent=client.headers['user-agent']
)


print(client.cookies)
print('\nBYPASSED KOGAMA CLOUDFLARE')

