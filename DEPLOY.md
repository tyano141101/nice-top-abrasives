# 独立站部署上线指南

本站为纯静态网站（HTML + CSS + JS），共 72 个页面，可部署到任何静态托管平台，无需服务器。

## 一、目录结构

```
pengyu-site/
├── index.html              首页
├── products/index.html     产品总览
├── category/*.html         7 个产品分类页
├── product/*.html          60 个产品详情页
├── applications.html       应用行业
├── about.html              关于我们
├── contact.html            联系/询盘表单
├── sitemap.xml             站点地图（提交 Google Search Console 用）
└── assets/
    ├── css/style.css
    ├── js/main.js
    └── img/                站点图片
```

## 二、上线前必须改的 4 件事

1. **绑定域名**：`src/build.py` 顶部 `SITE_URL = "https://www.yourdomain.com"` 改为真实域名，重新运行 `python3 src/build.py`，再上传（sitemap.xml 里用得到）。
2. **接询盘表单**：去 [formspree.io](https://formspree.io) 免费注册一个表单，把 `src/build.py` 顶部 `FORMSPREE` 改为你的表单地址，重新生成。备选：改用 `mailto:` 或接到企业微信/WhatsApp。
3. **换品牌信息**：`src/products.json` → `site` 字段（公司名、品牌、电话、邮箱、地址），改完重新运行 `build.py` 全站生效。
4. **换产品实拍图**：`assets/img/` 里 4 张为 AI 占位图，上线前替换为工厂/产品实拍（建议尺寸 1200×800）。60 个产品详情页目前用分类图标占位，可按需补产品图。

重新生成命令：`cd pengyu-site && python3 src/build.py`

## 三、部署方式（三选一，均为免费额度起步）

**A. Cloudflare Pages（推荐，国内访问相对稳）**
1. 把 `pengyu-site` 推到 GitHub 仓库
2. Cloudflare → Pages → 连接 GitHub → 构建设置留空（纯静态）
3. 绑定域名，开启 HTTPS

**B. Netlify**
1. 直接把 `pengyu-site` 文件夹拖进 https://app.netlify.com/drop
2. 得到临时域名，再绑定自有域名

**C. Vercel**
1. `npm i -g vercel && cd pengyu-site && vercel`
2. 按提示绑定域名

## 四、上线后事项

- Google Search Console 提交 `sitemap.xml`，加速收录 60 个产品页（每个产品页都是独立的 SEO 落地页，正好承接 Google Ads 关键词）
- 给全站接入 Google Analytics 4 + Google Ads 转化跟踪（询盘表单提交设为转化目标）
- contact.html 的表单提交后建议跳转感谢页（可在 Formspree 里配置 redirect）

## 五、后续可扩展

- 多语言：当前为英文站；俄语/越南语版本可按同样结构再生成一套（产品数据已有中文对照）
- 博客/News 板块：对 SEO 有帮助，需要的话可以再加
- 在线聊天：接入 Tawk.to / WhatsApp 浮窗按钮
