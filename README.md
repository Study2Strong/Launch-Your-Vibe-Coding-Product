# Launch Your Vibe Coding Product

📖 **[網頁好讀版](https://study2strong.github.io/Launch-Your-Vibe-Coding-Product/)** — 內容與本 README 呼應，建議直接看網頁版

## 這是什麼

市面上很多教學在教「怎麼用 AI 做出一個產品」，但很少有人教「產品做出來後，怎麼讓它真正上線、隨時可用」。這個 repo 示範的就是這一段：一個真實跑起來的 CI/CD 流程，把內容從本機變成一個任何人隨時打得開的網址——而且你現在看到的好讀版網頁，就是照著這套流程自動部署出來的。

## 部署流程

完整流程圖與逐步說明在[好讀版網頁](https://study2strong.github.io/Launch-Your-Vibe-Coding-Product/)裡，這裡只列重點：

1. 開分支、改內容、本機自我檢查（AI 輔助：`/simplify`、`/security-review`）
2. 發 PR，觸發 **CI job**：連結檢查（＋視情況加入 UI 自動化測試），與自動／人工 Code Review 並行，全部通過才解鎖 Merge
3. Merge 到 `main`，觸發 **CD job**：`vitepress build` 打包 → 部署到 GitHub Pages

CI（測試/驗證）與 CD（打包/部署）刻意拆成兩個獨立階段，測試沒過，部署就完全不會被觸發。

## 前置條件

實際照做這套流程之前，需要先準備好：

- GitHub 帳號（免費方案即可）
- 這個 repo 必須設為 **public**——GitHub 免費方案的 Pages 只能從 public repo 發布；private repo 要 GitHub Pro（個人）或 Team（組織）付費方案才能搭配 Pages（[來源](https://docs.github.com/get-started/learning-about-github/githubs-products)）
- 完成 `gh auth login`，讓 GitHub CLI 取得授權
- 本機安裝 Git、Node.js + npm（VitePress 建置需要）
- 若要加入 UI 自動化測試：本機/CI 需要 Python 3。Selenium 4.6+ 內建 Selenium Manager，會自動偵測並下載對應版本的瀏覽器驅動，不需要額外手動安裝（[來源](https://www.selenium.dev/documentation/selenium_manager/)）
- 若要額外部署到 Cloudflare Pages：需要一組免費 Cloudflare 帳號與 API Token

## 限制條件

這套流程用 GitHub Pages 部署，代表也繼承了它的限制（[來源](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)）：

- **僅支援純靜態內容**：不能在 Pages 上執行伺服器端程式（PHP/Node.js/Python 執行環境）、不能直接連資料庫。這也是為什麼這個 MVP 定位是「靜態教學網站」——動態服務、後端、資料庫規劃寫在網頁的 Roadmap 段落，誠實標示為「還沒做」
- 網站大小軟上限 1GB，來源 repo 也建議不超過 1GB
- 頻寬軟上限 100GB/月（軟限制，超過會先收到通知而非直接關站）
- build 頻率軟上限每小時 10 次，但**使用自訂 GitHub Actions workflow 部署不受此限**——這正是這個 repo 採用的方式
- 單次部署逾時上限 10 分鐘
- 部署內容全部公開可見，不能放任何密鑰或敏感資訊
- 不可作為商業交易／電商／SaaS 的主要用途（GitHub 服務條款限制）

## 本機開發

```bash
npm install
npm run docs:dev      # 本機預覽，預設 http://localhost:5173
npm run docs:build    # 打包成靜態檔案
```
