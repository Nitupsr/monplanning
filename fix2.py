content = open('/var/www/html/planning.html').read()
old = "  const weekServices = services.filter(s => s.date >= ws && s.date <= ws.replace(/.*/, d => {\n    const dd = new Date(d+'T00:00:00'); dd.setDate(dd.getDate()+6); return dd.toISOString().slice(0,10);\n  }));"
new = "  const pad2 = n => String(n).padStart(2,'0'); const weD = new Date(ws+'T00:00:00'); weD.setDate(weD.getDate()+6); const weEnd = weD.getFullYear()+'-'+pad2(weD.getMonth()+1)+'-'+pad2(weD.getDate());\n  const weekServices = services.filter(s => s.date >= ws && s.date <= weEnd);"
content = content.replace(old, new)
open('/var/www/html/planning.html', 'w').write(content)
print('OK' if old not in content else 'NOT REPLACED')
