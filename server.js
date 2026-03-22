const express = require('express');
const Database = require('better-sqlite3');
const cors = require('cors');
const path = require('path');

const app = express();
const db = new Database(path.join(__dirname, 'planning.db'));

app.use(cors());
app.use(express.json());

// Init tables
db.exec(`
  CREATE TABLE IF NOT EXISTS services (
    id TEXT PRIMARY KEY,
    date TEXT,
    code TEXT,
    start TEXT,
    end TEXT,
    serviceNum TEXT,
    note TEXT,
    modified INTEGER DEFAULT 0,
    history TEXT DEFAULT '[]'
  );
  CREATE TABLE IF NOT EXISTS codes (
    key TEXT PRIMARY KEY,
    label TEXT,
    type TEXT
  );
`);

// Services
app.get('/services', (req, res) => {
  const rows = db.prepare('SELECT * FROM services ORDER BY date DESC').all();
  rows.forEach(r => r.history = JSON.parse(r.history || '[]'));
  res.json(rows);
});

app.post('/services', (req, res) => {
  const s = req.body;
  db.prepare(`INSERT OR REPLACE INTO services VALUES (?,?,?,?,?,?,?,?,?)`).run(
    s.id, s.date, s.code, s.start, s.end, s.serviceNum, s.note,
    s.modified ? 1 : 0, JSON.stringify(s.history || [])
  );
  res.json({ok: true});
});

app.delete('/services/:id', (req, res) => {
  db.prepare('DELETE FROM services WHERE id=?').run(req.params.id);
  res.json({ok: true});
});

// Codes
app.get('/codes', (req, res) => {
  res.json(db.prepare('SELECT * FROM codes').all());
});

app.post('/codes', (req, res) => {
  const c = req.body;
  db.prepare('INSERT OR REPLACE INTO codes VALUES (?,?,?)').run(c.key, c.label, c.type);
  res.json({ok: true});
});

app.delete('/codes/:key', (req, res) => {
  db.prepare('DELETE FROM codes WHERE key=?').run(req.params.key);
  res.json({ok: true});
});

app.listen(3001, () => console.log('Planning backend running on port 3001'));
