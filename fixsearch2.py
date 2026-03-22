content = open('/var/www/html/planning.html').read()

old = 'function toggleHistory(id) {'
new = '''function handleSearch(val) {
  const clearBtn = document.getElementById('clearSearch');
  const searchResults = document.getElementById('searchResults');
  const weekView = document.getElementById('weekView');
  
  if (!val.trim()) {
    clearSearch();
    return;
  }
  
  clearBtn.style.display = 'block';
  
  // Convertir le wildcard en regex
  const pattern = val.trim().replace(/\*/g, '.*').replace(/\?/g, '.');
  const regex = new RegExp(pattern, 'i');
  
  const results = services.filter(s => 
    regex.test(s.serviceNum || '') || 
    regex.test(s.code) ||
    regex.test(s.note || '')
  ).sort((a,b) => b.date.localeCompare(a.date));
  
  weekView.style.display = 'none';
  searchResults.style.display = 'block';
  
  if (!results.length) {
    searchResults.innerHTML = '<div class="empty"><div class="empty-icon">🔍</div><div class="empty-text">Aucun résultat.</div></div>';
    return;
  }
  
  const today = getLocalToday();
  searchResults.innerHTML = results.map(s => {
    const fd = formatDate(s.date);
    const code = getCode(s.code);
    const type = code ? code.type : 'service';
    const dur = calcDuration(s.start, s.end);
    const isRestDay = isRest(s.code);
    const isPast = s.date < today;
    const isToday = s.date === today;
    const timeClass = isPast ? 'is-past' : isToday ? 'is-today' : '';
    return `<div class="service-item ${timeClass}">
      <div class="service-date">
        ${fd.weekday}<br><span class="day">${fd.day}</span> <span style="font-size:10px">${fd.month}</span>
        <span style="font-size:9px;color:var(--text2)">${s.date.slice(0,4)}</span>
      </div>
      <div class="service-main">
        <div class="service-code">
          ${s.serviceNum ? s.serviceNum : s.code}
          <span class="badge ${getBadgeClass(type)}">${s.code}</span>
          ${s.modified ? '<span class="badge badge-star">⭐</span>' : ''}
        </div>
        <div class="service-hours">${s.start && s.end ? s.start+' → '+s.end : (code ? code.label : s.code)}</div>
        ${s.note ? '<div style="font-size:11px;color:var(--text2);margin-top:2px">📝 '+s.note+'</div>' : ''}
      </div>
      <div class="service-duration">${isRestDay ? '—' : formatDuration(dur)}</div>
    </div>`;
  }).join('');
}

function clearSearch() {
  document.getElementById('searchInput').value = '';
  document.getElementById('clearSearch').style.display = 'none';
  document.getElementById('searchResults').style.display = 'none';
  document.getElementById('weekView').style.display = 'block';
}

function toggleHistory(id) {'''

content = content.replace('function toggleHistory(id) {', new)
open('/var/www/html/planning.html', 'w').write(content)
print('OK')
