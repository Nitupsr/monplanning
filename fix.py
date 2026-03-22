content = open('/var/www/html/planning.html').read()
old = "s.date <= ws.replace(/.*/, d => {\n    const dd = new Date(d+'T00:00:00'); dd.setDate(dd.getDate()+6); return dd.toISOString().slice(0,10);\n  })"
new = "s.date <= (() => { const we = new Date(ws+'T00:00:00'); we.setDate(we.getDate()+6); return we.getFullYear()+'-'+String(we.getMonth()+1).padStart(2,'0')+'-'+String(we.getDate()).padStart(2,'0'); })()"
content = content.replace(old, new)
open('/var/www/html/planning.html', 'w').write(content)
print('OK' if old not in content else 'NOT REPLACED')
