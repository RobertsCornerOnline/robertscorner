/* ==========================================================================
   Robert's Corner — shared script (theme toggle, back-to-top, copy email)
   Loaded with `defer` at the end of every page.
   ========================================================================== */

/* THEME TOGGLE ------------------------------------------------------------
   Works out the theme currently shown, flips it, and saves the choice.
   The icon swaps through CSS, so no icon logic is needed here. */
document.getElementById("theme")?.addEventListener("click", () => {
  const root = document.documentElement;
  const isDark = root.dataset.theme
    ? root.dataset.theme === "dark"
    : matchMedia("(prefers-color-scheme:dark)").matches;
  root.dataset.theme = isDark ? "light" : "dark";
  try { localStorage.setItem("theme", root.dataset.theme); } catch (e) { /* storage blocked: ignore */ }
});

/* BACK TO TOP -------------------------------------------------------------
   Button appears after scrolling 600px. */
const totop = document.getElementById("totop");
if (totop) {
  addEventListener("scroll", () => totop.classList.toggle("show", scrollY > 600), { passive: true });
  totop.addEventListener("click", () => scrollTo({ top: 0 }));
}

/* COPY EMAIL --------------------------------------------------------------
   Any element with data-copy copies that text to the clipboard. */
document.querySelectorAll("[data-copy]").forEach(btn =>
  btn.addEventListener("click", async () => {
    const label = btn.textContent;
    try { await navigator.clipboard.writeText(btn.dataset.copy); btn.textContent = "Copied"; }
    catch (e) { btn.textContent = "Copy failed"; }
    setTimeout(() => (btn.textContent = label), 1500);
  })
);
