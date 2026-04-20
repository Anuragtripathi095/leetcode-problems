class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_gas = 0
        total_cost = 0
        tank = 0
        start = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            
            tank += gas[i] - cost[i]
            
            # If tank is negative, reset starting point
            if tank < 0:
                start = i + 1
                tank = 0
        
        # Check overall feasibility
        if total_gas < total_cost:
            return -1
        
        return start