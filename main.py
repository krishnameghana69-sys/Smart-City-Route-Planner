from fastapi import FastAPI
from algorithms import get_all_cities, dijkstra, get_path, find_all_paths, path_metrics
from positions import positions
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from graph_data import graph

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend
#app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")


@app.get("/cities")
def cities():
    return get_all_cities()

@app.get("/route/{destination}")
def get_route(destination: str):
    all_routes = find_all_paths("Majestic", destination)

    routes_info = []
    for r in all_routes:
        dist, time = path_metrics(r)
        routes_info.append({
            "path": r,
            "distance": dist,
            "time": round(time, 2)
        })

    # Sort by (time, distance)
    routes_info.sort(key=lambda x: (x["time"], x["distance"]))

    # Take best 3 routes
    top_three = routes_info[:3]

    # Dijkstra
    time_d, dist_d, parent_d = dijkstra()
    dijkstra_path = get_path(parent_d, destination)

    return {
        "source": "Majestic",
        "destination": destination,
        "top_three_routes": top_three,
        "dijkstra_route": dijkstra_path,
        "dijkstra_time": round(time_d[destination], 2),
        "dijkstra_distance": dist_d[destination]
    }



@app.get("/edges")
def get_edges():
    return graph


@app.get("/positions")
def get_positions():
    return positions
