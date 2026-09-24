(() => {
  const el = document.getElementById("last-updated");
  if (!el) return;

  const modified = new Date(document.lastModified);
  const formatted = new Intl.DateTimeFormat("en-GB", {
    day: "2-digit",
    month: "short",
    year: "numeric"
  }).format(modified);

  el.textContent = formatted;
})();
