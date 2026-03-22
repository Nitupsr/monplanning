content = open('/var/www/html/planning.html').read()

# 1. Ajouter l'onglet Permutations dans les tabs
old = '    <button class="tab" onclick="switchTab(\'codes\')">🏷️ Codes</button>'
new = '''    <button class="tab" onclick="switchTab('codes')">🏷️ Codes</button>
    <button class="tab" onclick="switchTab('permut')">🔄 Permutations</button>'''
content = content.replace(old, new)

# 2. Ajouter le div de l'onglet Permutations
old2 = '  <!-- Stats Tab -->'
new2 = '''  <!-- Permutations Tab -->
  <div id="tab-permut" style="display:none">
    <div id="permutList"></div>
  </div>

  <!-- Stats Tab -->'''
content = content.replace(old2, new2)

# 3. Ajouter permutExcludes et statuts dans la config
old3 = 'let changeReasons'
new3 = '''let permutStatuses = JSON.parse(localStorage.getItem('permutStatuses') || '{}');
let permutExcludes = JSON.parse(localStorage.getItem('permutExcludes') || '[]');

function savePermutData() {
  localStorage.setItem('permutStatuses', JSON.stringify(permutStatuses));
  localStorage.setItem('permutExcludes', JSON.stringify(permutExcludes));
}

let changeReasons'''
content = content.replace(old3, new3)

open('/var/www/html/planning.html', 'w').write(content)
print('OK')
