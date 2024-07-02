#!/usr/bin/python3
"""Lockboxes challenge"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists):list of lists representing boxes and their keys.
    
    Returns:
        bool: True if all boxes can be opened, alse otherwise.
    """
    n = len(boxes)
    visited = set() # Set to store visited boxes

    # Recursive function to explore boxes
    def dfs(boxes_index):
        visited.add(boxes_index) # Mark the box as visited
        keys = boxes[boxes_index] # Get keys in the current box
        for key in keys:
            if key not in visited and key < n:
                dfs(key) # Explore the key

        dfs(0) # Start DFS from the first box

        return len(visited) == n # Check if all boxes are visited
