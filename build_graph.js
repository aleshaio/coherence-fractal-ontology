// Build fractal graph from _meta fields
// Usage: node build_graph.js

const fs = require('fs');
const path = require('path');

function getAllJsonFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  
  files.forEach(file => {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);
    
    if (stat.isDirectory()) {
      getAllJsonFiles(filePath, fileList);
    } else if (file.endsWith('.json') && !file.includes('example')) {
      fileList.push(filePath);
    }
  });
  
  return fileList;
}

function extractMeta(filePath) {
  try {
    const content = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    return content._meta || null;
  } catch (e) {
    return null;
  }
}

function buildGraph() {
  const files = getAllJsonFiles('.');
  const nodes = [];
  const edges = [];
  
  // Extract nodes
  files.forEach(filePath => {
    const meta = extractMeta(filePath);
    if (meta) {
      nodes.push({
        id: meta.id,
        type: meta.type || 'Unknown',
        element: meta.element || null,
        depth: meta.fractal_depth || 0,
        file: filePath
      });
    }
  });
  
  // Extract edges
  files.forEach(filePath => {
    const meta = extractMeta(filePath);
    if (!meta) return;
    
    const sourceId = meta.id;
    
    // Contains relationships
    if (meta.contains) {
      meta.contains.forEach(targetId => {
        edges.push({
          from: sourceId,
          to: targetId,
          type: 'CONTAINS',
          bidirectional: false
        });
      });
    }
    
    // Contained_by relationships
    if (meta.contained_by) {
      meta.contained_by.forEach(targetId => {
        edges.push({
          from: sourceId,
          to: targetId,
          type: 'CONTAINED_BY',
          bidirectional: false
        });
      });
    }
    
    // Related relationships
    if (meta.related) {
      meta.related.forEach(targetId => {
        edges.push({
          from: sourceId,
          to: targetId,
          type: 'RELATED',
          bidirectional: true
        });
      });
    }
    
    // Balance relationships
    if (meta.balances) {
      edges.push({
        from: sourceId,
        to: meta.balances,
        type: 'BALANCES',
        bidirectional: true
      });
    }
    
    // Combines relationships
    if (meta.combines) {
      meta.combines.forEach(targetId => {
        edges.push({
          from: sourceId,
          to: targetId,
          type: 'COMBINES',
          bidirectional: false
        });
      });
    }
  });
  
  return { nodes, edges };
}

function exportD3(graph) {
  return JSON.stringify(graph, null, 2);
}

function exportMermaid(graph) {
  let output = '```mermaid\ngraph TD\n';
  
  // Add nodes with labels
  const nodeLabels = {};
  graph.nodes.forEach(node => {
    const shortId = node.id.split(':').pop();
    nodeLabels[node.id] = shortId;
    
    let shape = '[]';
    if (node.type === 'Seed') shape = '((' + shortId + '))';
    else if (node.type === 'Path') shape = '[' + shortId + ']';
    else shape = '[' + shortId + ']';
    
    output += `    ${shortId}${shape}\n`;
  });
  
  // Add edges
  graph.edges.forEach(edge => {
    const from = edge.from.split(':').pop();
    const to = edge.to.split(':').pop();
    
    if (edge.type === 'CONTAINS') {
      output += `    ${from} -->|contains| ${to}\n`;
    } else if (edge.type === 'CONTAINED_BY') {
      output += `    ${from} -.->|contained by| ${to}\n`;
    } else if (edge.type === 'BALANCES') {
      output += `    ${from} <-->|balances| ${to}\n`;
    } else if (edge.type === 'RELATED') {
      output += `    ${from} --- ${to}\n`;
    }
  });
  
  output += '```';
  return output;
}

function exportCypher(graph) {
  let output = '// Neo4j Cypher import\n\n';
  
  // Create nodes
  output += '// Create nodes\n';
  graph.nodes.forEach(node => {
    const props = JSON.stringify({
      id: node.id,
      type: node.type,
      element: node.element,
      depth: node.depth,
      file: node.file
    });
    output += `CREATE (n:Node ${props});\n`;
  });
  
  output += '\n// Create relationships\n';
  graph.edges.forEach(edge => {
    output += `MATCH (a:Node {id: "${edge.from}"}), (b:Node {id: "${edge.to}"})\n`;
    output += `CREATE (a)-[:${edge.type}]->(b);\n`;
  });
  
  return output;
}

// Main
console.log('Building fractal graph...\n');

const graph = buildGraph();

console.log(`Nodes: ${graph.nodes.length}`);
console.log(`Edges: ${graph.edges.length}\n`);

// Export to multiple formats
fs.writeFileSync('graph.json', exportD3(graph));
console.log('✓ Exported: graph.json (D3.js format)');

fs.writeFileSync('graph.md', exportMermaid(graph));
console.log('✓ Exported: graph.md (Mermaid diagram)');

fs.writeFileSync('graph.cypher', exportCypher(graph));
console.log('✓ Exported: graph.cypher (Neo4j import)');

console.log('\nDone! 🌀');
