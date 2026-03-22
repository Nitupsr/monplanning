content = open('/var/www/html/planning.html').read()
old = "document.getElementById('stat-week-days').textContent = `${workWeek.length} service(s)`;"
new = "const weEndDbg = (() => { const we = new Date(ws+'T00:00:00'); we.setDate(we.getDate()+6); return we.getFullYear()+'-'+String(we.getMonth()+1).padStart(2,'0')+'-'+String(we.getDate()).padStart(2,'0'); })(); document.getElementById('stat-week-days').textContent = `${workWeek.length} services | ws=${ws} we=${weEndDbg}`;"
content = content.replace(old, new)
open('/var/www/html/planning.html', 'w').write(content)
print('OK')
