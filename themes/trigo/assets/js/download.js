/*
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/

const RELEASES_API = 'https://api.github.com/repos/FreeCAD/FreeCAD/releases?per_page=100';
const WEEKLY_TAG = /^weekly-\d{4}\.\d{2}\.\d{2}$/;

const releaseDownloads = document.querySelectorAll('[data-release-download]');

if (releaseDownloads.length) {
  const donatePage = releaseDownloads[0].dataset.donatePage;

  document.querySelectorAll('.download-link').forEach(link => {
    link.addEventListener('click', () => {
      setTimeout(() => {
        window.location.assign(donatePage);
      }, 1500);
    });
  });

  fetch(RELEASES_API)
    .then(response => {
      if (!response.ok) {
        throw new Error(`GitHub API: ${response.status}`);
      }

      return response.json();
    })
    .then(releases => {
      if (!Array.isArray(releases)) {
        throw new Error('GitHub API: expected a release list');
      }

      releaseDownloads.forEach(download => {
        const channel = download.dataset.releaseChannel;
        const latest = channel === 'weekly'
          ? releases
            .filter(release =>
              !release.draft &&
              release.prerelease &&
              WEEKLY_TAG.test(release.tag_name)
            )
            .sort((a, b) => b.tag_name.localeCompare(a.tag_name))[0]
          : releases
            .filter(release => !release.draft && !release.prerelease)
            .sort((a, b) => Date.parse(b.published_at) - Date.parse(a.published_at))[0];

        if (!latest) {
          return;
        }

        const releaseLink = download.querySelector('[data-release-link]');
        if (latest.html_url && releaseLink) {
          releaseLink.href = latest.html_url;
        }

        const assets = Array.isArray(latest.assets) ? latest.assets : [];
        download.querySelectorAll('[data-release-asset-pattern]').forEach(link => {
          const assetPattern = new RegExp(link.dataset.releaseAssetPattern);
          const asset = assets.find(candidate =>
            assetPattern.test(candidate.name) && candidate.browser_download_url
          );

          if (!asset) {
            return;
          }

          link.href = asset.browser_download_url;
          link.hidden = false;
          link.removeAttribute('aria-hidden');
        });
      });
    })
    .catch(error => {
      console.warn('Unable to load FreeCAD release data.', error);
    });
}
