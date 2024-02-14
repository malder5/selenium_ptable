from urllib.parse import urlparse, parse_qs

link = 'https://google.ru/?wmid=242&clickid=92c84d0f8c034531ace41792bd8bcc05&Mookid=zoSIq0bZhDXE'

result = parse_qs(urlparse(link).query)

print(result['clickid'])


