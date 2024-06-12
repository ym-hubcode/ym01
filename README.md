
# OSPF Simulation

This project simulates the OSPF (Open Shortest Path First) protocol using Python. The simulation includes a graphical representation of the network topology and the routing process.

## Features
- Graphical network topology using Pygame
- Simulated routers using multiprocessing
- LSA generation and broadcasting
- Shortest path calculation using Dijkstra's algorithm

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Modules

- `main.py`: The main entry point of the application.
- `router.py`: Defines the Router class and its functionalities.
- `network.py`: Manages the network topology.
- `dijkstra.py`: Implements Dijkstra's algorithm.
- `utils/visualization.py`: Contains functions for graphical visualization.
