from python_tsp.heuristics import solve_tsp_lin_kernighan
import numpy as np

from tqdm import trange
import platform

def self_organising_maps(points: np.ndarray) -> np.ndarray:
    # use known solver
    points = np.unique(points)
    distance_matrix = np.abs(points[:,None] - points[None,:])

    optimal_solution, _ = solve_tsp_lin_kernighan(distance_matrix)

    route = points[optimal_solution]
    return route


def greedy_shortest_path(points: np.ndarray) -> np.ndarray:
    # keep points only once
    points = np.unique(points)

    # initialise empty path
    path = np.ndarray(len(points), dtype=complex)
    points *= 1j
    path[-1] = min(points[points.imag == min(points.imag)]) / 1j
    points /= 1j

    for i in trange(len(points), desc="Optimising shape", ascii=True if platform.system() == "Windows" else None, leave=False):
        # find the nearest point
        nearest = np.abs(points - path[i-1]).argmin()
        # set the next element in the path to this value
        path[i] = points[nearest]
        # delete that point
        points = np.delete(points, nearest)

    return path


def optimised_shortest_path(points: np.ndarray, iterations : int = 2) -> np.ndarray:
    # precompute greedy path
    points = greedy_shortest_path(points)

    for _ in range(iterations):
        # start with points that are already in place
        order = np.argsort(abs(points - np.roll(points, 1)) + abs(points - np.roll(points, -1)))
        for i in order:
            point = points[i]
            # remove the point
            points = np.delete(points, i)
            # find the best place to insert
            distances = abs(points - point)
            heuristic = distances + np.roll(distances, 1) - abs(points - np.roll(points, 1))
            nearest = heuristic.argmin()
            # insert back in the shortest place
            points = np.insert(points, nearest, point)        

    return points