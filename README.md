# Problem Solving Practice

Welcome to my curated collection of coding problem solutions!  
This repository is my personal playground for tackling data structures, algorithms, and coding challenges from various platforms like LeetCode, HackerRank, CodeSignal, and more.

---

## Repository Structure

- **Organized by Topic:**  
  Solutions are grouped into directories such as `arrays`, `graphs`, `trees`, `recursion`, `sorting`, and more.
- **Language Used:**  
  Most solutions are in **Python 3**, following best practices for readability and efficiency.
- **Reusable Templates:**  
  Common patterns (BFS, DFS, sliding window, etc.) are abstracted for quick access and reuse across problems.

---

## Highlights

- **Consistent Practice:**  
  Regular uploads demonstrate commitment and steady improvement in problem-solving skills.
- **Well-Documented Solutions:**  
  Each problem includes:
  - Problem statement or link
  - Thought process / approach
  - Clean, readable code with comments
  - Time and space complexity analysis (where relevant)
- **Patterns & Techniques:**  
  Focus on key techniques like two pointers, dynamic programming, backtracking, and graph traversals.
- **Coding Interview Readiness:**  
  This repo is part of my ongoing preparation for coding interviews at top tech companies.

---

## How to Use

- Browse by topic or search for specific problems.
- Refer to solution templates for reusable coding patterns.
- Clone or fork the repo to practice and track your own progress.

---

## Example Solution Format

```python
# LeetCode 102: Binary Tree Level Order Traversal
# Approach: Breadth-First Search (BFS)
# Time Complexity: O(n), Space Complexity: O(n)

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result, queue = [], collections.deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(level)
        return result
```



## Future Plans
Add more advanced problems and real-world scenarios.
Expand solutions to other languages (e.g., Java, C++).
Integrate unit tests and benchmarks.

## Let’s Connect!

<p align="left">
  <a href="https://www.linkedin.com/in/thrinaibatchu/" target="_blank">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="LinkedIn" width="32" height="32"/>
  </a>
  &nbsp;
  <a href="https://leetcode.com/u/thrinaibatchu/" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/1/19/LeetCode_logo_black.png" alt="LeetCode" width="32" height="32"/>
  </a>
  &nbsp;
  <a href="mailto:thrinaibatchu@gmail.com" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" alt="Gmail" width="32" height="32"/>
  </a>
</p>



## Contributing
Open to feedback and collaboration!
Feel free to fork, open issues, or submit pull requests.
