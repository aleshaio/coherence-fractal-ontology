// Test that _meta is present in all files
const fs = require('fs');
const path = require('path');

const files = [
  'absolute.json',
  'paths/air.json',
  'paths/fire.json',
  'paths/water.json',
  'paths/earth.json',
  'growth/positions.json',
  'growth/fibonacci.json',
  'tools/assess.json',
  'tools/balance.json',
  'ai/awakening.json'
];

console.log('Checking fractal structure...\n');

files.forEach(file => {
  try {
    const content = JSON.parse(fs.readFileSync(file, 'utf8'));
    const hasMeta = !!content._meta;
    const hasSeed = !!content._holographic_seed;
    const hasLinks = !!content._links;
    
    console.log(`${file}:`);
    console.log(`  _meta: ${hasMeta ? '✓' : '✗'}`);
    console.log(`  _holographic_seed: ${hasSeed ? '✓' : '✗'}`);
    console.log(`  _links: ${hasLinks ? '✓' : '✗'}`);
    console.log('');
  } catch (e) {
    console.log(`${file}: ERROR - ${e.message}\n`);
  }
});

console.log('Structure check complete! 🌀');
