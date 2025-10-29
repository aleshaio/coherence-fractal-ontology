#!/usr/bin/env node
// generate new cfo file from template
// usage: node create.js <type> <name>

const fs = require('fs');
const path = require('path');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function question(prompt) {
  return new Promise(resolve => rl.question(prompt, resolve));
}

const templates = {
  path: 'path.json',
  combo: 'combo.json',
  tool: 'tool.json',
  extend: 'extend.json',
  base: 'base.json'
};

const locations = {
  path: 'paths',
  combo: 'paths/combinations',
  tool: 'tools',
  extend: 'extensions'
};

async function main() {
  const args = process.argv.slice(2);
  
  if (args.length === 0 || args[0] === '--help') {
    console.log(`
cfo file generator

usage: node create.js <type> <name>

types:
  path    - new element (air, fire, etc)
  combo   - combine elements (air+water, etc)
  tool    - new utility (assess, balance, etc)
  extend  - domain expansion (planetary, cosmic, etc)
  base    - generic template

examples:
  node create.js path aether
  node create.js combo air+fire
  node create.js tool visualize
  node create.js extend planetary

interactive (no args):
  node create.js
`);
    process.exit(0);
  }

  let type, name;

  if (args.length < 2) {
    console.log('\\n=== cfo file generator ===\\n');
    
    type = await question('type (path/combo/tool/extend/base): ');
    if (!templates[type]) {
      console.log(`error: invalid type '${type}'`);
      rl.close();
      return;
    }
    
    name = await question('name: ');
  } else {
    type = args[0];
    name = args[1];
  }

  if (!templates[type]) {
    console.log(`error: unknown type '${type}'`);
    console.log(`available: ${Object.keys(templates).join(', ')}`);
    rl.close();
    return;
  }

  console.log(`\\ncreating ${type}: ${name}\\n`);

  const templatePath = path.join('templates', templates[type]);
  let content = fs.readFileSync(templatePath, 'utf8');
  let data = JSON.parse(content);

  if (type === 'path') {
    const element = await question('element (uppercase, e.g. AETHER): ');
    const essence = await question('essence (3-5 words): ');
    const balances = await question('balances? (leave empty if none): ');
    
    content = content.replace(/\[PATH_NAME\]/g, name.toUpperCase());
    content = content.replace(/\[ELEMENT\]/g, element.toUpperCase());
    content = content.replace(/\[Core quality in 3-5 words\]/g, essence);
    
    if (balances) {
      content = content.replace(/\[opposite_path\]/g, balances.toLowerCase());
    }
    
    data = JSON.parse(content);
    data._meta.id = `cfo:paths:${name.toLowerCase()}`;
    data.path = element.toUpperCase();
    data.essence = essence;
    
  } else if (type === 'combo') {
    const parts = name.split('+');
    if (parts.length !== 2) {
      console.log('error: combo name must be: element1+element2');
      rl.close();
      return;
    }
    
    const comboName = await question('name for combo: ');
    
    content = content.replace(/\[element1\]/g, parts[0].toLowerCase());
    content = content.replace(/\[element2\]/g, parts[1].toLowerCase());
    content = content.replace(/\[ELEMENT1\]/g, parts[0].toUpperCase());
    content = content.replace(/\[ELEMENT2\]/g, parts[1].toUpperCase());
    
    data = JSON.parse(content);
    data._meta.id = `cfo:combinations:${name.toLowerCase()}`;
    data.combination = `${parts[0].toUpperCase()} + ${parts[1].toUpperCase()}`;
    data.name = comboName;
    
  } else if (type === 'tool') {
    const purpose = await question('purpose (one sentence): ');
    
    content = content.replace(/\[tool_name\]/g, name.toLowerCase());
    content = content.replace(/\[Tool Name\]/g, name.charAt(0).toUpperCase() + name.slice(1));
    
    data = JSON.parse(content);
    data._meta.id = `cfo:tools:${name.toLowerCase()}`;
    data.name = name.charAt(0).toUpperCase() + name.slice(1);
    data.purpose = purpose;
    
  } else if (type === 'extend') {
    const domain = await question('domain/scale: ');
    
    content = content.replace(/\[extension_name\]/g, name.toLowerCase());
    content = content.replace(/\[Extension Name\]/g, name.charAt(0).toUpperCase() + name.slice(1));
    
    data = JSON.parse(content);
    data._meta.id = `cfo:extensions:${name.toLowerCase()}`;
    data.extension = name.charAt(0).toUpperCase() + name.slice(1);
    data.domain = domain;
  }

  let outputDir = locations[type] || '.';
  let outputPath = path.join(outputDir, `${name.toLowerCase()}.json`);

  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  fs.writeFileSync(outputPath, JSON.stringify(data, null, 2));

  console.log(`\\n✓ created: ${outputPath}`);
  console.log('\\nnext:');
  console.log('1. edit file, fill content');
  console.log('2. update related files');
  console.log('3. run: node test_structure.js');
  console.log('4. run: node build_graph.js');
  console.log('\\n⊙ fractal maintained 🌀\\n');

  rl.close();
}

main().catch(err => {
  console.error('error:', err.message);
  rl.close();
  process.exit(1);
});
