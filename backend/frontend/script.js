// 3D Background
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('bg') });
renderer.setSize(window.innerWidth, window.innerHeight);
camera.position.z = 5;

const geometry = new THREE.TorusGeometry(1, 0.4, 16, 100);
const material = new THREE.MeshStandardMaterial({ color: 0x38bdf8 });
const torus = new THREE.Mesh(geometry, material);
scene.add(torus);

const light = new THREE.PointLight(0xffffff);
light.position.set(5, 5, 5);
scene.add(light);

function animate() {
  requestAnimationFrame(animate);
  torus.rotation.x += 0.01;
  torus.rotation.y += 0.005;
  renderer.render(scene, camera);
}
animate();

// Toggle chatbot
document.getElementById("chatbot-toggle").addEventListener("click", () => {
  const chatbot = document.getElementById("chatbot-box");
  chatbot.style.display = chatbot.style.display === "flex" ? "none" : "flex";
});

// Handle chat
document.getElementById("send-btn").addEventListener("click", async () => {
  const input = document.getElementById("chat-input");
  const message = input.value.trim();
  const chatBox = document.getElementById("chat-messages");

  if (message) {
    chatBox.innerHTML += `<div class="chat-msg user">${message}</div>`;
    input.value = "";

    const res = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });

    const data = await res.json();
    chatBox.innerHTML += `<div class="chat-msg bot">${data.response}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
  }
});

// Task logic
let editId = null;

document.getElementById("taskForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const title = document.getElementById("title").value;
  const description = document.getElementById("description").value;
  const status = document.getElementById("status").value;

  const method = editId ? "PUT" : "POST";
  const url = editId
    ? `http://127.0.0.1:8000/tasks/${editId}`
    : `http://127.0.0.1:8000/tasks`;

  await fetch(url, {
    method,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, description, status }),
  });

  document.getElementById("taskForm").reset();
  editId = null;
  fetchTasks();
});

async function fetchTasks() {
  const res = await fetch("http://127.0.0.1:8000/tasks");
  const tasks = await res.json();
  const container = document.getElementById("tasks");
  container.innerHTML = "";

  tasks.forEach((task) => {
    const div = document.createElement("div");
    div.className = "task";
    div.innerHTML = `
      <h3>${task.title}</h3>
      <p>${task.description}</p>
      <p class="status">${task.status}</p>
      <div class="actions">
        <button class="edit" onclick="editTask(${task.id})">Edit</button>
        <button class="delete" onclick="deleteTask(${task.id})">Delete</button>
      </div>`;
    container.appendChild(div);
  });
}
fetchTasks();

async function deleteTask(id) {
  await fetch(`http://127.0.0.1:8000/tasks/${id}`, { method: "DELETE" });
  fetchTasks();
}

function editTask(id) {
  fetch(`http://127.0.0.1:8000/tasks/${id}`)
    .then(res => res.json())
    .then(task => {
      document.getElementById("title").value = task.title;
      document.getElementById("description").value = task.description;
      document.getElementById("status").value = task.status;
      editId = id;
    });
}
