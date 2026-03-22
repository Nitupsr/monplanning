content = open('/var/www/html/planning.html').read()

# Corriger le label dans le select - format complet avec mois
old = "const label = `${ws.slice(8)}/${ws.slice(5,7)} - ${we.slice(8)}/${we.slice(5,7)}`;"
new = "const mois = ['Jan','Fév','Mar','Avr','Mai','Jun','Jul','Aoû','Sep','Oct','Nov','Déc']; const label = `Sem. du ${parseInt(ws.slice(8))} ${mois[parseInt(ws.slice(5,7))-1]} au ${parseInt(we.slice(8))} ${mois[parseInt(we.slice(5,7))-1]}`;"
content = content.replace(old, new)

open('/var/www/html/planning.html', 'w').write(content)
print('OK')
