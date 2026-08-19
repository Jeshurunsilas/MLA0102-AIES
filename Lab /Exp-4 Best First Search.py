import heapq
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 5,
    'E': 1,
    'F': 3,
    'G': 0
}

def best_first_search(start, goal):
    pq = [(heuristic[start], start)]
    visited = set()

    while pq:
        h, node = heapq.heappop(pq)

        if node in visited:
            continue

        print(node, end=" ")
        visited.add(node)

        if node == goal:
            print("\nGoal Reached")
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

best_first_search('A', 'G')
