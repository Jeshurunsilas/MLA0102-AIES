import heapq

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 7), ('E', 3)],
    'C': [('F', 1)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 5)],
    'G': []
}

def uniform_cost_search(start, goal):
    pq = [(0, start)]
    visited = set()

    while pq:
        cost, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            print("Minimum Cost:", cost)
            return

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor))

uniform_cost_search('A', 'G')
