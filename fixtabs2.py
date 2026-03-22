content = open('/var/www/html/planning.html').read()

old = "  document.querySelectorAll('.tab').forEach((el,i) => {\n    el.classList.toggle('active', ['services','stats','codes','permut'][i] === tab);"
new = "  document.querySelectorAll('.tab').forEach((el,i) => {\n    el.classList.toggle('active', ['services','permut','stats','codes'][i] === tab);"
content = content.replace(old, new)

old2 = "  ['services','stats','codes','permut'].forEach(t => {"
new2 = "  ['services','permut','stats','codes'].forEach(t => {"
content = content.replace(old2, new2)

open('/var/www/html/planning.html', 'w').write(content)
print('OK')
