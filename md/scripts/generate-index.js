import fs from 'fs'
import path from 'path'

const ROOT = path.resolve('.')

const TARGET_DIRS = [
  'doc',
  'doc-modules',
  'doc-wiki-syntax',
  'faq',
  'scp-cn',
  'history-of-universe',
  'faq-splitted/community-sites',
  'faq-splitted/editing-pages',
  'faq-splitted/private-sites',
  'faq-splitted/site-features',
  'faq-splitted/technical',
  'faq-splitted/upgrades',
  'faq-splitted/user-accounts',
  'faq-splitted/watching',
]

// 读取 Markdown 标题（第一行 #）
function getTitle(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8')
  let line = content.split('\n')[0].trim()
  if (line.includes("```")) {
    line = content.split('\n')[1].trim()
  }
  return line.startsWith("###") ? line.replace(/^###\s*/, '') : line.replace(/^#\s*/, '')
}

// 生成 index.md
function generateIndex(dir) {
  const abs = path.join(ROOT, dir)
  const files = fs.readdirSync(abs)
    .filter(f => f.endsWith('.md') && f !== 'index.md')

  const items = files.map(f => {
    const filePath = path.join(abs, f)
    const title = getTitle(filePath)
    const link = `./${f}`
    return `- [${title}](${link})`
  })

  const content = `# ${dir}\n\n` + items.join('\n') + '\n'

  fs.writeFileSync(path.join(abs, 'index.md'), content)
  console.log(`✔ generated ${dir}/index.md`)
}

// 总入口 index.md
function generateRootIndex() {
  const items = TARGET_DIRS.map(dir => {
    return `- [${dir}](/${dir}/)`
  })

  const content = `# Documentation Hub\n\n${items.join('\n')}\n`

  fs.writeFileSync(path.join(ROOT, 'index.md'), content)
  console.log('✔ generated root index.md')
}

// 执行
TARGET_DIRS.forEach(generateIndex)