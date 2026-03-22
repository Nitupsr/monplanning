content = open('/var/www/html/planning.html').read()

old = '  <!-- Services Tab -->\n  <div id="tab-services">\n    <div id="weekView">\n    <div class="week-nav">'
new = '''  <!-- Services Tab -->
  <div id="tab-services">
    <div style="position:relative;margin-bottom:10px">
      <input type="text" id="searchInput" placeholder="🔍 Rechercher... (ex: W191*, *18*)" oninput="handleSearch(this.value)" style="width:100%;background:var(--bg2);border:1px solid var(--border);color:var(--text);padding:10px 36px 10px 14px;border-radius:10px;font-size:14px;font-family:'DM Sans',sans-serif;">
      <button onclick="clearSearch()" id="clearSearch" style="display:none;position:absolute;right:10px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--text2);font-size:16px;cursor:pointer;">✕</button>
    </div>
    <div id="searchResults" style="display:none"></div>
    <div id="weekView">
    <div class="week-nav">'''

content = content.replace(old, new)
open('/var/www/html/planning.html', 'w').write(content)
print('OK' if 'searchInput' in content and content.count('searchInput') > 2 else 'NOT REPLACED - checking...')
