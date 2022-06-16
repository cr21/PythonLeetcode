"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

 

Example 1:


Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
Example 2:


Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 

Constraints:

1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
"""

## Approach 1 backtracking. + greedy 
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        from collections import defaultdict
        self.flightMap = defaultdict(list)
        for ticket in tickets:
            origin = ticket[0]
            dest = ticket[1]
            self.flightMap[origin].append(dest)
        self.flights = len(tickets)
        print(self.flightMap)
        
        self.visited = {}
        for origin, flights in self.flightMap.items():
            flights.sort()
            self.visited[origin] = [False]*self.flights
            
        self.result=[]
        route=["JFK"]
        self.backtrack("JFK", route)
        return self.result
    
    def backtrack(self, origin, route):
        if len(route) == self.flights+1:
            self.result = route
            return True
        
        for index, nextstop in enumerate(self.flightMap[origin]):
            if  not self.visited[origin][index]:
                # mark it
                self.visited[origin][index]  =True
                # recurse
                flag = self.backtrack(nextstop, route+[nextstop])
                if flag:
                    return True
                # unmark it backtrack
                self.visited[origin][index]  =False
                
        return False
        
        
        
        
        
        
        
        
        


## APPROACH 2 Euler cycle AKA Post order dfs

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = collections.defaultdict(list)
        print(sorted(tickets)[::-1])
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route, stack = [], ['JFK']
        while stack:
            while targets[stack[-1]]:
                stack += targets[stack[-1]].pop(),
            route += stack.pop(),
        return route[::-1]
