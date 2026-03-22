content = open('/var/www/html/planning.html').read()

# Supprimer le console.log de debug
old1 = "console.log('ws=',ws,'weEnd=',(() => { const we = new Date(ws+'T00:00:00'); we.setDate(we.getDate()+6); return we.getFullYear()+'-'+String(we.getMonth()+1).padStart(2,'0')+'-'+String(we.getDate()).padStart(2,'0'); })(),'weekServices=',weekServices.length,'workWeek=',workWeek.length,'total=',totalWeek); document.getElementById('stat-week').textContent = formatDuration(totalWeek);"
new1 = "document.getElementById('stat-week').textContent = formatDuration(totalWeek);"
content = content.replace(old1, new1)

# Supprimer le debug weEndDbg
old2 = "const weEndDbg = (() => { const we = new Date(ws+'T00:00:00'); we.setDate(we.getDate()+6); return we.getFullYear()+'-'+String(we.getMonth()+1).padStart(2,'0')+'-'+String(we.getDate()).padStart(2,'0'); })(); document.getElementById('stat-week-days').textContent = `${workWeek.length} services | ws=${ws} we=${weEndDbg}`;"
new2 = "document.getElementById('stat-week-days').textContent = `${workWeek.length} service(s)`;"
content = content.replace(old2, new2)

open('/var/www/html/planning.html', 'w').write(content)
print('OK')
