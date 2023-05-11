function handleSubmit(event) {
  event.preventDefault();
  const messageInput = document.getElementById("message");
  const message = messageInput.value;
  const loading = document.getElementById("loading");
  loading.classList.remove("hidden");
  fetch("/results", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  })
    .then((response) => response.text())
    .then((data) => {
      loading.classList.add("hidden");
      const responseDiv = document.createElement("div");
      responseDiv.innerText = data;
      document.body.appendChild(responseDiv);
    });
}
