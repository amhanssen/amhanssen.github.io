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
