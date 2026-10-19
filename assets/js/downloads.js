// Fills every .dl-count on the page; see _includes/downloads.html.
(function () {
  if (window.__mcDl) return; window.__mcDl = true;
  var archived = fetch(document.currentScript ? new URL("../downloads.json", document.currentScript.src).href : "/mobicut-public/assets/downloads.json", { cache: "no-store" })
    .then(function (r) { return r.ok ? r.json() : { archived: 0 }; })
    .then(function (j) { return j.archived || 0; })
    .catch(function () { return 0; });
  var live = fetch("https://api.github.com/repos/bme327/mobicut-public/releases?per_page=100")
    .then(function (r) { if (!r.ok) throw r; return r.json(); })
    .then(function (rs) {
      return rs.reduce(function (sum, rel) {
        return sum + rel.assets.filter(function (a) { return a.name === "mobicut.apk"; })
          .reduce(function (s, a) { return s + a.download_count; }, 0);
      }, 0);
    });
  Promise.all([archived, live]).then(function (v) {
    var n = (v[0] + v[1]).toLocaleString("en");
    document.querySelectorAll(".dl-count").forEach(function (el) {
      el.querySelector(".dl-n").textContent = n;
      el.hidden = false;
    });
  }).catch(function () {});
})();
