import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "MerulaBook",
  description: "AI-friendly Wikidot Documentation",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Examples', link: '/markdown-examples' }
    ],

    sidebar: [
      {
        text: 'Wikidot',
        items: [
          { text: 'General Doc', link: '/doc/' },
          { text: 'Modules Doc', link: '/doc-modules/' },
          { text: 'Wiki Syntax Doc', link: '/doc-wiki-syntax/' },
          { text: 'FAQ', link: '/faq/' },
          { text: 'FAQ - Community Sites', link: '/faq-splitted/community-sites' },
          { text: 'FAQ - Editing Pages', link: '/faq-splitted/editing-pages' },
          { text: 'FAQ - Private Sites', link: '/faq-splitted/private-sites' },
          { text: 'FAQ - Site Features', link: '/faq-splitted/site-features' },
          { text: 'FAQ - Technical', link: '/faq-splitted/technical' },
          { text: 'FAQ - Upgrades', link: '/faq-splitted/upgrades' },
          { text: 'FAQ - User Accounts', link: '/faq-splitted/user-accounts' },
          { text: 'FAQ - Watching', link: '/faq-splitted/watching' },

        ]
      },
      {
        text: 'Media',
        items: [
          { text: 'Wikidot AJAX 接口逆向文档', link: '/wikidot-ajax.md' },
        ]
      },
      {
        text: 'Community',
        items: [
          { text: 'SCP Wiki CN', link: '/scp-cn/' },
          { text: 'SCP Wiki CN - 宇宙史', link: '/history-of-universe/' },
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/rHanbowChic/wd-rag' }
    ],
    footer: {
      message: 'The river is moving. The blackbird must be flying.',
      copyright: 'Copyright © 2026 Ect07, Licensed under the MIT License.'
    },
    search: {
      provider: 'local'
    }
  },
  markdown: {
    config(md) {
      md.options.html = false

      const defaultRender =
        md.renderer.rules.link_open ||
        ((tokens, idx, options, env, self) =>
          self.renderToken(tokens, idx, options))

      md.renderer.rules.link_open = (tokens, idx, options, env, self) => {
        const href = tokens[idx].attrGet('href')

        if (!href) {
          return defaultRender(tokens, idx, options, env, self)
        }

        // Wikidot 内部死链
        if (
          href.startsWith('/doc:') ||
          href.startsWith('/doc-') ||
          href.startsWith('/system:') ||
          href.startsWith('/community-sites') ||
          href.startsWith('/page-unix-name') ||
          href.startsWith('/plans') ||
          href.startsWith('/education') ||
          href.startsWith('/start') ||
          href == "/doc"
        ) {
          // 去掉 href，保留文本
          tokens[idx].attrSet('href', '#')
        }

        return defaultRender(tokens, idx, options, env, self)
      }
    }
  },
  sitemap: {
    hostname: 'https://merula.ect.fyi'
  },
  head: [
    // 1. 注入 Dify Chatbot 配置
    ['script', {}, `
      window.difyChatbotConfig = {
        token: 'Fnbc7TuopmaZx6RQ',
        baseUrl: 'https://dify.ect.fyi',
        inputs: {},
        systemVariables: {},
        userVariables: {},
      }
    `],

    // 2. 引入 embed 脚本
    ['script', {
      src: 'https://dify.ect.fyi/embed.min.js',
      id: 'Fnbc7TuopmaZx6RQ',
      defer: ''
    }],

    // 3. 注入样式
    ['style', {}, `
      #dify-chatbot-bubble-button {
        background-color: #1C64F2 !important;
      }

      #dify-chatbot-bubble-window {
        width: 24rem !important;
        height: 40rem !important;
      }
    `]
  ]
})
