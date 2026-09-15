const input = document.querySelector('[data-testid="letra-input"]');
const error = document.querySelector('[data-testid="error-message"]');

input.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    if (input.value.length > 1) {
      error.textContent = "Solo se permite una letra por vez";
    } else {
      error.textContent = "";
    }
  }
});