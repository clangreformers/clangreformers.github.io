---
name: clangreformers knowledge map
description: Comprehensive knowledge map of the clangreformers Jekyll site — trilingual historical documentation project on Chinese language standardization
type: project
---

## Project: clangreformers

A trilingual (English / Simplified Chinese / Traditional Chinese) Jekyll-based historical documentation site preserving the history of Chinese language standardization and modernization (1912–1960s).

**URL**: https://clangreformers.github.io/
**Non-profit**: TaxId 83-2358327, established August 2019
**Maintainers**: Yun Wang & Yingxian Wang (granddaughter of Wang Shuda, a key historical figure)

**Why:** Preserve the personal histories and institutional records of the Chinese National Language Movement — a pivotal cultural project largely undocumented in English.

**How to apply:** All content is trilingual; edits/additions should always consider all three language variants. The site is scholarly but personal (family heritage).

## Architecture

- **Framework**: Jekyll 4.0.0 + Minima 2.5 theme
- **Hosting**: GitHub Pages
- **Plugins**: jekyll-sitemap, jekyll-feed, jekyll-seo-tag

### Trilingual routing
- English: default paths (`/about/`, `/people/`)
- Simplified Chinese: `-cn` suffix (`/about-cn/`)
- Traditional Chinese: `-tw` suffix (`/about-tw/`)
- Front matter uses `lang:` and `ref:` fields for language linking
- Separate navigation YAML files per language in `_data/`
- Separate search JSON files per language

### Directory map
| Directory | Purpose | File count |
|---|---|---|
| `_posts/` | Blog articles (trilingual) | ~130 files (43 unique × 3 langs) |
| `people/` | Biographical profiles | ~72 files (24 detailed × 3 langs) + index with 400+ names |
| `glossary/` | Historical terms & organizations | ~36 files (12 topics × 3 langs) |
| `dictionaries/` | Dictionary reference pages | 3 files |
| `teaching/` | Language teaching resources | 3 files |
| `standardization/` | Standardization timeline & overview | 6 files |
| `who/` | About the organization | 3 files |
| `_layouts/` | default, post, page templates | 3 files |
| `_includes/` | Headers, footers, widgets | ~28 components |
| `assets/css/` | Bootstrap + custom styles | 4 files |
| `assets/js/` | Carousel, search, banner scripts | 4 files |
| `assets/imgs/` | Historical photos, documents | 250+ files |
| `scripts/` | Python utilities (TTS audio, PDF extraction) | 5 files |

### Special features
- Homepage dual-carousel with timeline/chronological toggle
- Client-side search (simple-jekyll-search)
- Daily random character feature (Shuowen 600 characters)
- Pinyin/Zhuyin learning table
- Audio pronunciation recordings for 600 characters
- PayPal donation integration
- Interactive timeline widget
