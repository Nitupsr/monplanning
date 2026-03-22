import sys, json
from datetime import date, timedelta
import urllib.request

data = urllib.request.urlopen('http://135.125.53.206:3001/services').read()
services = json.loads(data)
today = date(2026, 3, 22)
day = today.weekday()
ws = today - timedelta(days=day)
we = ws + timedelta(days=6)
print('Semaine:', ws, 'au', we)
week = [s for s in services if ws.isoformat() <= s['date'] <= we.isoformat() and s['code'] not in ['RH','RTT','JRTT','CP','CPR','MAL']]
print('Services semaine:', [(s['date'], s['code'], s['start'], s['end']) for s in week])
total = sum((int(s['end'][:2])*60+int(s['end'][3:])) - (int(s['start'][:2])*60+int(s['start'][3:])) for s in week if s['start'] and s['end'])
print('Total:', total//60, 'h', total%60, 'min')
