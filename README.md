# Yizhu Wen — Personal Homepage

Source for [yizhu-wen.github.io](https://yizhu-wen.github.io), built with
[Jekyll](https://jekyllrb.com/) on the [academicpages](https://github.com/academicpages/academicpages.github.io)
template and published with GitHub Pages.

## Where things live

| What | File |
| --- | --- |
| Site settings, name, social links | `_config.yml` |
| Home page (bio, news, education, experience) | `_pages/about.md` |
| Publications page (grouping + intro) | `_pages/publications.md` |
| One file per paper | `_publications/YYYY-MM-DD-slug.md` |
| CV page | `_pages/cv.md` |
| CV download | `files/Yizhu_Wen_CV.pdf` |
| Top nav | `_data/navigation.yml` |
| Profile photo | `images/profile.png` |

## Adding a publication

Create `_publications/YYYY-MM-DD-slug.md`. The date controls ordering (newest first)
and `pubtype` decides which section it lands in — use `preprint` for anything under
review, anything else is listed as peer-reviewed.

```yaml
---
title: "Paper Title"
collection: publications
permalink: /publication/YYYY-MM-DD-slug
excerpt: "One sentence about the paper."
date: YYYY-MM-DD
venue: "Full Venue Name (ABBR'YY)"
venueshort: "ABBR'YY"
authors: "**Yizhu Wen**, Co Author"
pubtype: "conference"   # or "journal", or "preprint"
links:
  - label: "arXiv"
    url: "https://arxiv.org/abs/..."
  - label: "Code"
    url: "https://github.com/..."
paperurl: "https://arxiv.org/abs/..."
---
```

## Running locally

```bash
bundle install
bundle exec jekyll serve --config _config.yml,_config.dev.yml
```

Then open <http://localhost:4000>.
