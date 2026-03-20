/* FediShare from Hugo Theme Meme | 2023 Wladimir Palant | https://github.com/reuixiy/hugo-theme-meme */

function updateState() {
  let hasInstance = document.getElementById("instance").value.trim() != "";
  document.getElementById("submit").disabled = !hasInstance;
}

function getSoftwareName(instance) {
  const SUPPORTED_SCHEMAS = [
    "http://nodeinfo.diaspora.software/ns/schema/2.0",
    "http://nodeinfo.diaspora.software/ns/schema/2.1",
  ];
  return fetch(`https://${instance}/.well-known/nodeinfo`).then(response => response.json()).then(response => {
    if (response && Array.isArray(response.links))
      for (let link of response.links)
        if (SUPPORTED_SCHEMAS.includes(link.rel) && typeof link.href == "string")
          return fetch(link.href);
    throw new Exception(".well-known/nodeinfo file does not contain a nodeinfo link");
  }).then(response => response.json()).then(response => {
    if (response && response.software && typeof response.software.name == "string")
      return response.software.name;
    throw new Exception("_ link does not contain a software name");
  }).catch(error => {
    console.error(error);

    // Download probably failed due to CORS error, assume Mastodon or compatible
    return "mastodon";
  });
}

document.addEventListener("DOMContentLoaded", () => {
  let params = new URLSearchParams(location.hash.slice(1));
  document.getElementById("title").value = params.get("title");
  document.getElementById("description").value = params.get("description");
  document.getElementById("url").value = params.get("url");

  if ("mastodonInstance" in localStorage) {
    document.getElementById("instance").value = localStorage.mastodonInstance;
    document.getElementById("rememberInstance").checked = true;
  }

  const form = document.getElementById("shareForm");

  form.addEventListener("submit", event => {
    if (!form.checkValidity()) {
      event.preventDefault();
      form.reportValidity();
      return;
    };

    event.preventDefault();

    const submitBtn = document.getElementById("submit");
    if (submitBtn.disabled) return;

    let instance = document.getElementById("instance").value.trim();

    // Fix URLs mistakenly entered into the instance field
    instance = instance.replace(/^\w+:[\/\\]*/, "");
    instance = instance.replace(/[\/\\].*/, "");
    document.getElementById("instance").value = instance;

    if (instance == "") {
      form.reportValidity();
      return;
    }

    if (document.getElementById("rememberInstance").checked)
      localStorage.mastodonInstance = instance;
    else
      delete localStorage.mastodonInstance;

    let title = document.getElementById("title").value.trim();
    let description = document.getElementById("description").value.trim();
    let url = document.getElementById("url").value.trim();
    let text = title + "\n" + description + "\n" + url;

    getSoftwareName(instance).then(name => {
      let projects = JSON.parse(document.body.getAttribute("data-projects"));
      let endpoint = projects.hasOwnProperty(name) ? projects[name] : projects.mastodon;
      endpoint = endpoint.replace("{title}", encodeURIComponent(title));
      endpoint = endpoint.replace("{description}", encodeURIComponent(description));
      endpoint = endpoint.replace("{url}", encodeURIComponent(url));
      endpoint = endpoint.replace("{text}", encodeURIComponent(text));
      location.href = `https://${instance}/${endpoint}`;
    });
  });

  document.getElementById("instance").addEventListener("input", updateState);
  updateState();
});