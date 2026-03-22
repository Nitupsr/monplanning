content = open('/var/www/html/planning.html').read()

old = """    <button class="tab active" onclick="switchTab('services')">📋 Services</button>
    <button class="tab" onclick="switchTab('stats')">📊 Statistiques</button>
    <button class="tab" onclick="switchTab('codes')">🏷️ Codes</button>
    <button class="tab" onclick="switchTab('permut')">🔄 Permutations</button>"""

new = """    <button class="tab active" onclick="switchTab('services')">📋 Services</button>
    <button class="tab" onclick="switchTab('permut')">🔄 Permutations</button>
    <button class="tab" onclick="switchTab('stats')">📊 Statistiques</button>
    <button class="tab" onclick="switchTab('codes')">🏷️ Codes</button>"""

content = content.replace(old, new)
open('/var/www/html/planning.html', 'w').write(content)
print('OK' if old not in content else 'NOT REPLACED')
