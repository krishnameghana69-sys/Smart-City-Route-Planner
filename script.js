const API_BASE = "http://127.0.0.1:8000";

let cityPositions = {};
let edges = {};

async function loadCities() {
    const response = await fetch(`${API_BASE}/cities`);
    const cities = await response.json();
    const select = document.getElementById("destination");

    select.innerHTML = '<option value="">-- Select Destination --</option>';
    cities.forEach(city => {
        const option = document.createElement("option");
        option.value = city;
        option.textContent = city;
        select.appendChild(option);
    });
}

async function loadPositions() {
    const res = await fetch(`${API_BASE}/positions`);
    cityPositions = await res.json();
}

async function loadEdges() {
    const res = await fetch(`${API_BASE}/edges`);
    edges = await res.json();
}

function drawBaseMap() {
    const svg = document.getElementById("map");
    svg.innerHTML = "";

    // Draw roads
    for (const from in edges) {
        edges[from].forEach(edge => {
            const to = edge[0];
            const traffic = edge[2];

            const [x1, y1] = cityPositions[from];
            const [x2, y2] = cityPositions[to];

            const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
            line.setAttribute("x1", x1);
            line.setAttribute("y1", y1);
            line.setAttribute("x2", x2);
            line.setAttribute("y2", y2);
            line.setAttribute("stroke", traffic === "Green" ? "#7fbf7f" : "#f08080");
            line.setAttribute("stroke-width", "2");
            svg.appendChild(line);
        });
    }

    // Draw nodes
    for (const city in cityPositions) {
        const [x, y] = cityPositions[city];

        const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        circle.setAttribute("cx", x);
        circle.setAttribute("cy", y);
        circle.setAttribute("r", 6);
        circle.setAttribute("fill", "black");
        svg.appendChild(circle);

        const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
        text.setAttribute("x", x + 8);
        text.setAttribute("y", y + 4);
        text.setAttribute("font-size", "11");
        text.textContent = city;
        svg.appendChild(text);
    }
}

function highlightRoute(path, color, width) {
    const svg = document.getElementById("map");

    for (let i = 0; i < path.length - 1; i++) {
        const [x1, y1] = cityPositions[path[i]];
        const [x2, y2] = cityPositions[path[i + 1]];

        const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
        line.setAttribute("x1", x1);
        line.setAttribute("y1", y1);
        line.setAttribute("x2", x2);
        line.setAttribute("y2", y2);
        line.setAttribute("stroke", color);
        line.setAttribute("stroke-width", width);
        svg.appendChild(line);
    }
}

function showRouteInfoOnMap(distance, time) {
    const svg = document.getElementById("map");

    const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
    text.setAttribute("x", 20);
    text.setAttribute("y", 730);   // bottom of the map
    text.setAttribute("font-size", "16");
    text.setAttribute("fill", "#1e88e5");
    text.setAttribute("font-weight", "bold");

    text.textContent = `Distance: ${distance} km   |   Time: ${time} minutes`;

    svg.appendChild(text);
}



async function findRoute() {
    const dest = document.getElementById("destination").value;
    if (!dest) return alert("Select destination");

    const res = await fetch(`${API_BASE}/route/${dest}`);
    const data = await res.json();

    let output = "TOP 3 BEST ROUTES:\n\n";

    data.top_three_routes.forEach((r, i) => {
        output += `Route ${i + 1}: ${r.path.join(" -> ")}\n`;
        output += `Distance: ${r.distance} km\n`;
        output += `Time: ${r.time} min\n\n`;
    });

    output += "DIJKSTRA SHORTEST PATH:\n";
    output += data.dijkstra_route.join(" -> ") + "\n";
    output += `Distance: ${data.dijkstra_distance} km\n`;
    output += `Time: ${data.dijkstra_time} min\n`;

    document.getElementById("output").textContent = output;

    drawBaseMap();
    highlightRoute(data.top_three_routes[0].path, "#1e88e5", 5);   // Blue – Best Route
    highlightRoute(data.dijkstra_route, "#8e24aa", 4);            // Purple – Dijkstra
           // Dijkstra route
    showRouteInfoOnMap(
    data.top_three_routes[0].distance,
    data.top_three_routes[0].time
);


}

window.onload = async () => {
    await loadCities();
    await loadPositions();
    await loadEdges();
    drawBaseMap();
};
