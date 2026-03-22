content = open('/var/www/html/planning.html').read()
old = '''      <div class="service-date">
        <span class="day">${fd.day}</span>
        ${fd.weekday}<br><span style="font-size:10px">${fd.month}</span>
      </div>'''
new = '''      <div class="service-date">
        ${fd.weekday}<br><span class="day">${fd.day}</span><br><span style="font-size:10px">${fd.month}</span>
      </div>'''
content = content.replace(old, new)
open('/var/www/html/planning.html', 'w').write(content)
print('OK' if old not in content else 'NOT REPLACED')
