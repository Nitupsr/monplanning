content = open('/var/www/html/planning.html').read()

# Ajouter renderPermut dans switchTab
old = "  if (tab === 'stats') renderStats();\n  if (tab === 'codes') renderCodes();"
new = "  if (tab === 'stats') renderStats();\n  if (tab === 'codes') renderCodes();\n  if (tab === 'permut') renderPermut();"
content = content.replace(old, new)

# Ajouter tab-permut dans switchTab forEach
old2 = "  ['services','stats','codes'].forEach(t => {"
new2 = "  ['services','stats','codes','permut'].forEach(t => {"
content = content.replace(old2, new2)

old3 = "  document.querySelectorAll('.tab').forEach((el,i) => {\n    el.classList.toggle('active', ['services','stats','codes'][i] === tab);"
new3 = "  document.querySelectorAll('.tab').forEach((el,i) => {\n    el.classList.toggle('active', ['services','stats','codes','permut'][i] === tab);"
content = content.replace(old3, new3)

# Marquer auto comme permuté si service modifié dans confirmChange
old4 = "  await saveService(old);\n  document.getElementById('changeModal').classList.remove('open');"
new4 = "  await saveService(old);\n  if (permutStatuses[old.id] && permutStatuses[old.id] !== 'done') {\n    permutStatuses[old.id] = 'done';\n    savePermutData();\n  }\n  document.getElementById('changeModal').classList.remove('open');"
content = content.replace(old4, new4)

open('/var/www/html/planning.html', 'w').write(content)
print('OK')
