const puppeteer = require('puppeteer');

const LOGIN = 'TON_LOGIN';
const PASSWORD = 'TON_MOT_DE_PASSE';

async function scrapePlanning() {
const browser = await puppeteer.launch({
    headless: 'new',
    executablePath: '/usr/bin/chromium',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  
  // Intercepter les requêtes API
  const apiCalls = [];
  page.on('response', async response => {
    const url = response.url();
    const ct = response.headers()['content-type'] || '';
    if (ct.includes('json') && url.includes('keolis')) {
      try {
        const data = await response.json();
        apiCalls.push({ url, data });
      } catch(e) {}
    }
  });

  console.log('Ouverture my.keolis.com...');
  await page.goto('https://my.keolis.com', { waitUntil: 'networkidle2', timeout: 30000 });
  
  console.log('Page chargée, titre:', await page.title());
  console.log('URL actuelle:', page.url());
  
  // Screenshot pour voir où on en est
  await page.screenshot({ path: '/tmp/keolis1.png' });
  console.log('Screenshot sauvegardé dans /tmp/keolis1.png');
  
  console.log('APIs détectées:', apiCalls.length);
  apiCalls.forEach(a => console.log(' -', a.url));

  await browser.close();
}

scrapePlanning().catch(console.error);
