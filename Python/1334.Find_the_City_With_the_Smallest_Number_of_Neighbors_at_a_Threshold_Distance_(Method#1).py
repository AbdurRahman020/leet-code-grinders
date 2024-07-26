from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
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

if __name__ == '__main__':
    s = Solution()
    print(s.findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))
    print(s.findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2))