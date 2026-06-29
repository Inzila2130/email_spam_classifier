const textarea = document.getElementById("message");
const wordCount = document.getElementById("wordCount");
const charCount = document.getElementById("charCount");
const form = document.querySelector("form");
const analyzeButton = document.querySelector(".analyze-btn");

function updateCounter() {
    if (!textarea) return;

    const text = textarea.value.trim();

    const words = text === "" ? 0 : text.split(/\s+/).length;

    wordCount.textContent = `Words : ${words}`;
    charCount.textContent = `Characters : ${textarea.value.length}`;
}

function autoResize() {
    if (!textarea) return;

    textarea.style.height = "auto";
    textarea.style.height = textarea.scrollHeight + "px";
}

if (textarea) {
    updateCounter();
    autoResize();

    textarea.addEventListener("input", () => {
        updateCounter();
        autoResize();
    });
}

if (form) {
    form.addEventListener("submit", () => {
        analyzeButton.disabled = true;
        analyzeButton.innerHTML = "⏳ Analyzing...";
    });
}

const progressBar = document.querySelector(".progress-fill");

if (progressBar) {
    const width = progressBar.dataset.width;

    setTimeout(() => {
        progressBar.style.width = width + "%";
    }, 300);
}

const hamButton = document.getElementById("hamSample");

if (hamButton) {
    hamButton.addEventListener("click", () => {
        textarea.value =
            "Hi! Just checking if we're still meeting tomorrow at 10 AM.";

        updateCounter();
        autoResize();
    });
}

const spamButton = document.getElementById("spamSample");

if (spamButton) {
    spamButton.addEventListener("click", () => {
        textarea.value =
            "Congratulations! You have won a FREE iPhone. Click here to claim now.";

        updateCounter();
        autoResize();
    });
}

const copyButton = document.getElementById("copyResult");

if (copyButton) {
    copyButton.addEventListener("click", () => {

        const result = document.querySelector(".ham,.spam");

        if (!result) return;

        navigator.clipboard.writeText(result.innerText);

        copyButton.innerText = "Copied ✓";

        setTimeout(() => {
            copyButton.innerText = "📋 Copy Result";
        }, 2000);

    });
}

const themeButton = document.getElementById("themeButton");
const logo = document.getElementById("siteLogo");

function updateLogo() {

    if (!logo) return;

    if (document.body.classList.contains("light-theme")) {

        logo.src = "/static/images/mailshield-logo-light.png";
        themeButton.textContent = "☀️";

    } else {

        logo.src = "/static/images/mailshield-logo-dark.png";
        themeButton.textContent = "🌙";

    }

}

const savedTheme = localStorage.getItem("theme");

if (savedTheme === "light") {

    document.body.classList.add("light-theme");

}

updateLogo();

if (themeButton) {

    themeButton.addEventListener("click", () => {

        document.body.classList.toggle("light-theme");

        if (document.body.classList.contains("light-theme")) {

            localStorage.setItem("theme", "light");

        } else {

            localStorage.setItem("theme", "dark");

        }

        updateLogo();

    });

}