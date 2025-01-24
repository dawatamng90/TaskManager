// function markAsCompleted(taskId) {
//   const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;

//   fetch(`/task/${taskId}/mark-completed/`, {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//       "X-CSRFToken": csrfToken,
//     },
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       if (data.status) {
//         // Optionally, you can update the task status and completed date here if needed
//         document.getElementById(`status-${taskId}`).innerText =
//           data.status.replace("_", " ");
//         document.getElementById(`completed-date-${taskId}`).innerText =
//           data.completed_date;
//       }

//       // Refresh the page after marking the task as completed
//       window.location.reload(); // Forces a full page reload
//     })
//     .catch((error) => console.error("Error:", error));
// }

function markCompleted(taskId) {
  fetch(`/task/${taskId}/mark-completed/`, {
    method: "POST",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"), // Include the CSRF token
    },
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.status) {
        alert(`Task marked as: ${data.status}`);
        location.reload(); // Refresh the page or update the UI dynamically
      } else {
        alert(`Error: ${data.error}`);
      }
    })
    .catch((error) => console.error("Error:", error));
}
