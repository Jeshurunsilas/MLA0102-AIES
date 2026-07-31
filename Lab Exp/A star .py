import heapq
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 2,
    'E': 1,
    'F': 1,
    'G': 0
}

def a_star(start, goal):
    pq = [(heuristic[start], 0, start)]
    visited = set()

    while pq:
        f, g, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            print("Optimal Cost:", g)
            return

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(pq, (new_f, new_g, neighbor))

a_star('A', 'G')
