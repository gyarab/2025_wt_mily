import httpx

r = httpx.get('https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt;jsessionid=861D4434867C5AE3FAA91B21976B3B47?date=22.01.2026')
print(r.text)
print(r.status)
lines = r.text.split('\n')
print(lines[0])
