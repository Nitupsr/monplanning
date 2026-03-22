content = open('/var/www/html/planning.html').read()

old = 'function toggleHistory(id) {'
new = '''function isPermutable(s) {
  const today = getLocalToday();
  if (s.date <= today) return false;
  if (permutExcludes.includes(s.id)) return false;
  const startHour = s.start ? parseInt(s.start.split(':')[0]) : 99;
  const isW190 = s.serviceNum && s.serviceNum.match(/W190\d\d/i);
  return startHour < 6 || isW190;
}

function renderPermut() {
  const list = document.getElementById('permutList');
  const permutables = services.filter(isPermutable)
    .sort((a,b) => a.date.localeCompare(b.date));

  if (!permutables.length) {
    list.innerHTML = '<div class="empty"><div class="empty-icon">✅</div><div class="empty-text">Aucun service à permuter pour le moment.</div></div>';
    return;
  }

  const months = ['Jan','Fév','Mar','Avr','Mai','Jun','Jul','Aoû','Sep','Oct','Nov','Déc'];
  list.innerHTML = permutables.map(s => {
    const fd = formatDate(s.date);
    const status = permutStatuses[s.id] || 'todo';
    const statusLabel = { todo: '🔄 À permuter', waiting: '⏳ En attente', done: '✅ Permuté' };
    const statusColor = { todo: 'var(--accent2)', waiting: 'var(--yellow)', done: 'var(--green)' };
    return `<div class="service-item" style="border-left:3px solid ${statusColor[status]}">
      <div class="service-date">
        ${fd.weekday}<br><span class="day">${fd.day}</span> <span style="font-size:10px">${months[parseInt(s.date.slice(5,7))-1]}</span>
      </div>
      <div class="service-main">
        <div class="service-code">
          ${s.serviceNum || s.code}
          <span class="badge badge-service">${s.code}</span>
        </div>
        <div class="service-hours">${s.start && s.end ? s.start+' → '+s.end : ''}</div>
        <div style="margin-top:6px;font-size:12px;font-weight:600;color:${statusColor[status]}">${statusLabel[status]}</div>
        <div style="display:flex;gap:6px;margin-top:8px;flex-wrap:wrap">
          ${status !== 'waiting' ? `<button class="btn" style="font-size:11px;padding:4px 10px" onclick="setPermutStatus('${s.id}','waiting')">⏳ En attente</button>` : ''}
          ${status !== 'done' ? `<button class="btn primary" style="font-size:11px;padding:4px 10px" onclick="setPermutStatus('${s.id}','done')">✅ Permuté</button>` : ''}
          <button class="btn" style="font-size:11px;padding:4px 10px;border-color:var(--red);color:var(--red)" onclick="excludePermut('${s.id}')">✕ Retirer</button>
        </div>
      </div>
    </div>`;
  }).join('');
}

function setPermutStatus(id, status) {
  permutStatuses[id] = status;
  savePermutData();
  renderPermut();
}

function excludePermut(id) {
  permutExcludes.push(id);
  savePermutData();
  renderPermut();
}

function toggleHistory(id) {'''

content = content.replace('function toggleHistory(id) {', new)
open('/var/www/html/planning.html', 'w').write(content)
print('OK')
