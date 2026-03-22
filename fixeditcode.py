content = open('/var/www/html/planning.html').read()

old = 'async function addCode() {'
new = '''function editCode(i) {
  const c = codes[i];
  const newLabel = prompt('Libellé :', c.label);
  if (newLabel === null) return;
  const newType = prompt('Type (repos/conge/maladie/dispo/service) :', c.type);
  if (newType === null) return;
  codes[i].label = newLabel.trim() || c.label;
  codes[i].type = newType.trim() || c.type;
  saveCode(codes[i]);
  renderCodes();
  toast('Code modifié');
}

async function addCode() {'''

old2 = '<button class="icon-btn" onclick="deleteCode(${i})" title="Supprimer">×</button>'
new2 = '<button class="icon-btn edit" onclick="editCode(${i})" title="Modifier">✏️</button><button class="icon-btn" onclick="deleteCode(${i})" title="Supprimer">×</button>'

content = content.replace(old, new)
content = content.replace(old2, new2)
open('/var/www/html/planning.html', 'w').write(content)
print('OK')
