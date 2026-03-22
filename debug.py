content = open('/var/www/html/planning.html').read()
old = "document.getElementById('stat-week').textContent = formatDuration(totalWeek);"
new = "console.log('ws=',ws,'weEnd=',(() => { const we = new Date(ws+'T00:00:00'); we.setDate(we.getDate()+6); return we.getFullYear()+'-'+String(we.getMonth()+1).padStart(2,'0')+'-'+String(we.getDate()).padStart(2,'0'); })(),'weekServices=',weekServices.length,'workWeek=',workWeek.length,'total=',totalWeek); document.getElementById('stat-week').textContent = formatDuration(totalWeek);"
content = content.replace(old, new)
open('/var/www/html/planning.html', 'w').write(content)
print('OK')
