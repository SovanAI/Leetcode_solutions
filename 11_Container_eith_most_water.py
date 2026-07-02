class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate width
            width = right - left

            # Calculate height
            h = min(height[left], height[right])

            # Calculate area
            area = width * h

            # Update maximum area
            if area > max_area:
                max_area = area

            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
    


#     You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1