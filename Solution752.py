from collections import deque

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        # Convert deadends to a set for faster lookup
        deadends_set = set(deadends)
        # If the initial state is a dead end, return -1
        if "0000" in deadends_set:
            return -1
        # Initialize visited set to keep track of visited states
        visited = set()
        # Initialize the queue for BFS
        queue = deque([("0000", 0)])  # (state, steps)
        
        # BFS loop
        while queue:
            state, steps = queue.popleft()
            # If the target state is reached, return the number of steps
            if state == target:
                return steps
            # If the current state is a dead end or already visited, skip it
            if state in deadends_set or state in visited:
                continue
            # Mark the current state as visited
            visited.add(state)
            # Generate all possible next states
            for i in range(4):
                # Rotate the wheel up and down
                for d in (-1, 1):
                    new_digit = (int(state[i]) + d) % 10
                    new_state = state[:i] + str(new_digit) + state[i+1:]
                    # Add the new state to the queue if not visited and not a dead end
                    if new_state not in visited and new_state not in deadends_set:
                        queue.append((new_state, steps + 1))
        
        # If the target state cannot be reached
        return -1
