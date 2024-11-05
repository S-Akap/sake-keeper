const sampleLoginElm = document.querySelector("#sample-login");
const targetUrl = sampleLoginElm.getAttribute("href");

sampleLoginElm.addEventListener("click", (e) => {
    e.preventDefault();
    document.querySelector("#sample-login-modal").classList.add("open");
});

document.querySelector("#confirm-button").addEventListener("click", () => {
    window.location.href = targetUrl;
});

document.querySelector("#cancel-button").addEventListener("click", function() {
    document.querySelector("#sample-login-modal").classList.remove("open");
});
