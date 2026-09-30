# Publishing with GitHub Pages

The intended web address is https://aleverrier.github.io/bosonic-hardware/.

## First publication

1. Open https://github.com/aleverrier/bosonic-hardware/settings.
2. In **Danger Zone**, choose **Change repository visibility**, then **Make public**, and complete GitHub's confirmation. This makes repository contents public.
3. Open https://github.com/aleverrier/bosonic-hardware/settings/pages.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Select **main** and **/ (root)**, then **Save**.
6. Wait for GitHub to finish deployment. The Pages settings page reports the published address.

The repository already contains the entry point `index.html` and `.nojekyll`; no custom domain or local server is needed.

GitHub Pages can also use a private repository on a compatible paid GitHub plan. The website itself is normally publicly accessible. Official instructions: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## Subsequent updates

Edit `src/circuit-lab.html`, rebuild using `python3 tools/build.py`, and commit the source and regenerated `index.html` to `main`. Once Pages is configured, GitHub republishes changes from that branch.

## When the page does not appear

- Opening `index.html` in the GitHub file viewer shows source; use the hosted address.
- A 404 at the hosted address means publication is not yet available; check Pages settings and the deployment in the repository's Actions tab.
- An old page may be cached; reload after a successful deployment.
- The lab loads D3 from a pinned CDN URL; blocking that dependency can prevent plots from initializing.

## Current setup status

The files and browser link are committed. Repository visibility and Pages activation require completion through GitHub settings; they were not changed by the file upload.
