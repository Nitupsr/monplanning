content = open('/var/www/html/planning.html').read()

old = '  <div id="tab-services">\n    <div class="week-nav">'
new = '''  <div id="tab-services">
    <div style="position:relative;margin-bottom:10px">
      <input type="text" id="searchInput" placeholder="Rechercher... (ex: W191*, *18*)" oninput="handleSearch(this.value)" style="width:100%;background:var(--bg2);border:1px solid var(--border);color:var(--text);padding:10px 36px 10px 14px;border-radius:10px;font-size:14px;">
      <button onclick="clearSearch()" id="clearSearch" style="display:none;position:absolute;right:10px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--text2);font-size:16px;cursor:pointer;">✕</button>
    </div>
    <div id="searchResults" style="display:none"></div>
    <div id="weekView">
    <div class="week-nav">'''

old2 = '    <div id="servicesList"></div>\n  </div>\n\n  <!-- Stats Tab -->'
new2 = '    <div id="servicesList"></div>\n    </div>\n  </div>\n\n  <!-- Stats Tab -->'

content = content.replace(old, new)
content = content.replace(old2, new2)
open('/var/www/html/planning.html', 'w').write(content)
print('OK')
