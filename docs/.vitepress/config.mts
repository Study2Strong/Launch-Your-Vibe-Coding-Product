import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'

export default withMermaid(defineConfig({
  lang: 'zh-Hant',
  title: 'Launch Your Vibe Coding Product',
  description: 'AI 幫你把產品做出來之後，你要怎麼讓它真正上線、隨時可用？',
  base: '/Launch-Your-Vibe-Coding-Product/',
  cleanUrls: true,
  themeConfig: {
    outline: {
      level: [2, 3],
      label: '本頁目錄'
    },
    nav: [
      { text: '首頁', link: '/' }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/Study2Strong/Launch-Your-Vibe-Coding-Product' }
    ],
    footer: {
      message: '本網頁由本 repo 的 GitHub Actions 自動建置與部署',
      copyright: 'Study2Strong'
    }
  }
}))
