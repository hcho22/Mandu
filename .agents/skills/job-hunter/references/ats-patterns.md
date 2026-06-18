# ATS URL Patterns

Most company careers pages are powered by an Applicant Tracking System (ATS). When the main careers page doesn't list roles inline (because it's a JS embed), go directly to the ATS.

## Common ATS providers and URL patterns

### Greenhouse
- Public board: `https://boards.greenhouse.io/{company-slug}`
- API (often public): `https://boards-api.greenhouse.io/v1/boards/{company-slug}/jobs`
- The slug is usually the company name lowercased, no spaces

### Lever
- Public board: `https://jobs.lever.co/{company-slug}`
- API: `https://api.lever.co/v0/postings/{company-slug}?mode=json`

### Ashby
- Public board: `https://jobs.ashbyhq.com/{company-slug}`
- API: `https://api.ashbyhq.com/posting-api/job-board/{company-slug}`

### Workable
- Public board: `https://apply.workable.com/{company-slug}/`

### Workday
- Pattern: `https://{company}.wd1.myworkdayjobs.com/...` (varies a lot — search for the company name + "workday careers")
- Workday is the hardest to parse — heavy JS, often requires direct link from the company's own careers page

### SmartRecruiters
- Public board: `https://careers.smartrecruiters.com/{company-slug}`

### Rippling ATS / Recruitee / Personio / Pinpoint
- Less common — usually search `"{company} careers"` and follow the link from the main site

## Finding the slug when it isn't obvious

1. Go to the company's main careers page first.
2. View the page source or follow any "View all roles" / "See open positions" link — that link usually goes to the ATS.
3. The slug in that URL is what you want.

## When all else fails

- Web search: `"{company name}" jobs site:greenhouse.io OR site:lever.co OR site:ashbyhq.com`
- LinkedIn: `https://www.linkedin.com/company/{company}/jobs/` — useful as a backup but the source ATS is preferred because it's more current and shows the apply flow.

## What NOT to do

- Don't apply through aggregators (Indeed, ZipRecruiter, LinkedIn Easy Apply when an ATS link exists). Going through the source ATS gives a cleaner application and avoids referral confusion.
- Don't trust cached Google results for active job listings — fetch the live page.