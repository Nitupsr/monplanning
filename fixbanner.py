content = open('/var/www/html/planning.html').read()

# Ajouter la bannière après les stats-grid
old = '  <!-- Upload zone -->'
new = '''  <!-- Bannière prochain service -->
  <div id="nextServiceBanner" style="display:none;margin-bottom:12px"></div>

  <!-- Upload zone -->'''
content = content.replace(old, new)

# Ajouter la fonction JS
old2 = 'function getLocalToday() {'
new2 = '''function updateNextServiceBanner() {
  const banner = document.getElementById('nextServiceBanner');
  if (!banner) return;
  const today = getLocalToday();
  const now = new Date();
  const pad = n => String(n).padStart(2,'0');

  const upcoming = services
    .filter(s => s.date >= today && !isRest(s.code) && s.start)
    .sort((a,b) => a.date.localeCompare(b.date) || a.start.localeCompare(b.start));

  if (!upcoming.length) { banner.style.display = 'none'; return; }

  const next = upcoming[0];
  const isToday = next.date === today;
  const tomorrow = addDays(today, 1);
  const isTomorrow = next.date === tomorrow;
  const afterTomorrow = addDays(today, 2);
  const isAfterTomorrow = next.date === afterTomorrow;

  const diffDays = Math.round((new Date(next.date+'T00:00:00') - new Date(today+'T00:00:00')) / 86400000);

  let countdown = '';
  if (isToday) {
    const [sh, sm] = next.start.split(':').map(Number);
    const startMins = sh * 60 + sm;
    const nowMins = now.getHours() * 60 + now.getMinutes();
    const diff = startMins - nowMins;
    if (diff <= 0) {
      const [eh, em] = (next.end || '00:00').split(':').map(Number);
      const endMins = eh * 60 + em;
      if (nowMins < endMins) countdown = 'En cours';
      else countdown = 'Terminé';
    } else if (sh < 12) countdown = 'Ce matin';
    else if (sh < 14) countdown = 'Ce midi';
    else if (sh < 18) countdown = 'Cet après-midi';
    else countdown = 'Ce soir';
  } else if (isTomorrow) {
    countdown = 'Demain';
  } else if (isAfterTomorrow) {
    countdown = 'Après-demain';
  } else {
    countdown = `Dans ${diffDays} jours`;
  }

  const color = isToday ? 'var(--green)' : 'var(--accent)';
  const borderColor = isToday ? 'rgba(79,209,160,0.4)' : 'rgba(79,156,249,0.4)';
  const bgColor = isToday ? 'rgba(79,209,160,0.08)' : 'rgba(79,156,249,0.08)';
  const label = isToday ? 'En service aujourd\'hui' : 'Prochain service';

  banner.style.display = 'block';
  banner.innerHTML = `<div style="background:${bgColor};border:1px solid ${borderColor};border-radius:14px;padding:14px 16px;display:flex;align-items:center;gap:12px;">
    <div style="font-size:26px;flex-shrink:0">🚃</div>
    <div style="flex:1">
      <div style="font-size:11px;font-weight:600;color:${color};text-transform:uppercase;letter-spacing:0.8px;margin-bottom:3px">${label}</div>
      <div style="font-size:16px;font-weight:700;color:${color}">${next.serviceNum || next.code}</div>
      <div style="font-size:12px;color:var(--text2);margin-top:2px">${next.start} → ${next.end || '?'}</div>
    </div>
    <div style="font-family:'Courier New',monospace;font-size:13px;font-weight:700;color:${color};background:${bgColor};border:1px solid ${borderColor};border-radius:8px;padding:8px 12px;text-align:center;flex-shrink:0">${countdown}</div>
  </div>`;
}

function getLocalToday() {'''

content = content.replace('function getLocalToday() {', new2)

# Appeler updateNextServiceBanner dans render
old3 = '  updateStats();\n}'
new3 = '  updateStats();\n  updateNextServiceBanner();\n}'
content = content.replace(old3, new3, 1)

open('/var/www/html/planning.html', 'w').write(content)
print('OK')
