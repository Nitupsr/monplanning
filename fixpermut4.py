content = open('/var/www/html/planning.html').read()

old = '    <div id="permutList"></div>\n  </div>'
new = '''    <div style="text-align:right;margin-bottom:8px">
      <button class="btn" style="font-size:11px;padding:5px 12px;color:var(--text2)" onclick="resetPermut()">↺ Réinitialiser la liste</button>
    </div>
    <div id="permutList"></div>
  </div>'''
content = content.replace(old, new)

old2 = 'function excludePermut(id) {'
new2 = '''function resetPermut() {
  if (!confirm('Réinitialiser tous les statuts et exclusions ?')) return;
  permutStatuses = {};
  permutExcludes = [];
  savePermutData();
  renderPermut();
  toast('Liste réinitialisée');
}

function excludePermut(id) {'''
content = content.replace(old2, new2)

open('/var/www/html/planning.html', 'w').write(content)
print('OK')
