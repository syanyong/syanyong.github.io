document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.getElementById("contact-toggle");
  const card = document.getElementById("contact-card");

  if (!toggle || !card) return;

  toggle.addEventListener("click", () => {
    const isExpanded = toggle.getAttribute("aria-expanded") === "true";
    toggle.setAttribute("aria-expanded", String(!isExpanded));
    toggle.setAttribute("title", isExpanded ? "Show contact QR code" : "Hide contact QR code");
    card.hidden = isExpanded;
  });
});
