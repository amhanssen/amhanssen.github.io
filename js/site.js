// Opens and closes the phone menu.
document.addEventListener("DOMContentLoaded", () => {
  const nav = document.querySelector(".nav");
  const btn = document.querySelector(".menu-btn");
  if (!nav || !btn) return;
  btn.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    btn.setAttribute("aria-expanded", open);
    btn.textContent = open ? "Close" : "Menu";
  });
});

// Click a case-study image to see it larger. Escape or click closes it.
document.addEventListener("DOMContentLoaded", () => {
  if (!location.pathname.includes("/work/")) return;
  const imgs = document.querySelectorAll("figure img");
  let box = null;
  const close = () => { if (box) { box.remove(); box = null; document.body.style.overflow = ""; } };
  imgs.forEach((img) => {
    img.classList.add("zoomable");
    img.addEventListener("click", () => {
      box = document.createElement("div");
      box.className = "lightbox";
      box.setAttribute("role", "dialog");
      box.setAttribute("aria-label", img.alt || "Image");
      const big = document.createElement("img");
      big.src = img.currentSrc || img.src;
      big.alt = img.alt;
      const btn = document.createElement("button");
      btn.textContent = "Close";
      box.append(big, btn);
      box.addEventListener("click", close);
      document.body.append(box);
      document.body.style.overflow = "hidden";
      btn.focus();
    });
  });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") close(); });
});
