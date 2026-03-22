content = open('/var/www/html/planning.html').read()
old = "const thisMonth = now.toISOString().slice(0,7);"
new = "const pad = n => String(n).padStart(2,'0'); const todayStr = now.getFullYear()+'-'+pad(now.getMonth()+1)+'-'+pad(now.getDate()); const thisMonth = todayStr.slice(0,7);"
content = content.replace(old, new)
old2 = "const todayLocal = `${now.getFullYear()}-${String(now.getMonth()+1).padStart(2,\"0\")}-${String(now.getDate()).padStart(2,\"0\")}`;\n  const ws = getWeekStart(todayLocal);"
new2 = "const ws = getWeekStart(todayStr);"
content = content.replace(old2, new2)
open('/var/www/html/planning.html', 'w').write(content)
print('OK')
