from typing import List
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def findTheCity1(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # initialize the distance matrix with infinity
        # distance_matrix[i][j] will hold the shortest distance from city i to city j
        distance_matrix = [[float("inf")] * n for _ in range(n)]

        # distance from each city to itself is zero
        for city in range(n):
            distance_matrix[city][city] = 0

        # populate the distance matrix with the given edges
        # for each edge (u, v) with weight wt, set the distance from u to v and v to u
        for u, v, wt in edges:
            distance_matrix[u][v] = wt
            distance_matrix[v][u] = wt

        # Floyd-Warshall algorithm to compute shortest paths between all pairs of cities
        for intermediate in range(n):
            for source in range(n):
                for destination in range(n):
                    # update the shortest distance from source to destination
                    # using intermediate as a possible stopover
                    distance_matrix[source][destination] = min(
                        distance_matrix[source][destination],
                        distance_matrix[source][intermediate] + distance_matrix[intermediate][destination]
                    )

        # variables to determine the best city
        best_city = -1
        # initialize to a value larger than possible to find the minimum
        min_reachable_cities = n + 1

        # evaluate each city to count how many cities are reachable within the distance threshold
        for city in range(n):
            # count the number of cities within the distance threshold from the current city
            reachable_count = sum(
                1 for other_city in range(n)
                if distance_matrix[city][other_city] <= distanceThreshold
            )
            
            # update the best city if the current city has fewer or equal reachable cities
            if reachable_count <= min_reachable_cities:
                min_reachable_cities = reachable_count
                best_city = city

        # return the city with the minimum number of reachable cities within the distance threshold
        return best_city
    
    def findTheCity2(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # variable to store the city with the minimum reachable cities within the threshold
        best_city = -1
        # initialize to a value larger than possible to find the minimum
        min_reachable_cities = n + 1
        # adjacency list to store the graph
        adj_list = defaultdict(list)

        # create adjacency list from the edges
        for u, v, weight in edges:
            # add edge from u to v with the given weight
            adj_list[u].append([v, weight])
            # add edge from v to u with the given weight (since undirected)
            adj_list[v].append([u, weight])

        # iterate through each city to determine the number of reachable cities
        for city in range(n):
            # counter for the number of cities reachable within the distance threshold
            reachable_count = 0
            # distance array initialized to infinity
            distances = [float('inf')] * n
            # distance to itself is 0
            distances[city] = 0
            # priority queue for Dijkstra's algorithm, initialized with the starting city
            priority_queue = [(0, city)]

            # Dijkstra's algorithm to find the shortest paths from the current city
            while priority_queue:
                # det the city with the smallest distance
                current_distance, current_city = heappop(priority_queue)

                # if the distance exceeds the threshold, no need to process further
                if current_distance > distanceThreshold:
                    break

                # explore all neighbors of the current city
                for neighbor_city, weight in adj_list[current_city]:
                    # calculate the distance to the neighbor city
                    if current_distance + weight < distances[neighbor_city]:
                        # update distance if a shorter path is found
                        distances[neighbor_city] = current_distance + weight
                        # push the neighbor into the priority queue
                        heappush(priority_queue, (distances[neighbor_city], neighbor_city))

            # count the number of cities within the distance threshold from the current city
            reachable_count = sum(1 for j in range(n) if distances[j] <= distanceThreshold)
            
            # update the best city if the current city has fewer or equal reachable cities
            if reachable_count <= min_reachable_cities:
                min_reachable_cities = reachable_count
                best_city = city

        # return the city with the minimum reachable cities within the distance threshold
        return best_city

if __name__ == '__main__':
    s = Solution()
    
    print(s.findTheCity1(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))
    print(s.findTheCity1(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2))
    
    print(s.findTheCity2(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))
    print(s.findTheCity2(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2))
