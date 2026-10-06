"""Tests the lesson notebook calls with check(...). You never need to open this."""

from check import eq


def _tree():
    #       3
    #      / \
    #     9   20
    #        /  \
    #       15   7
    return TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))


def test_build_and_to_pylist():
    eq(to_pylist(build_list([1, 2, 3])), [1, 2, 3])
    eq(build_list([]), None)
    eq(to_pylist(None), [])


def test_reverse_list():
    eq(to_pylist(Solution().reverseList(build_list([1, 2, 3, 4]))), [4, 3, 2, 1])
    eq(Solution().reverseList(None), None)


def test_remove_elements():
    eq(to_pylist(Solution().removeElements(build_list([7, 1, 7, 2, 7]), 7)), [1, 2])
    eq(to_pylist(Solution().removeElements(build_list([7, 7]), 7)), [])


def test_max_depth():
    eq(Solution().maxDepth(_tree()), 3)
    eq(Solution().maxDepth(None), 0)


def test_count_leaves():
    eq(Solution().countLeaves(_tree()), 3)
    eq(Solution().countLeaves(None), 0)


def test_climb_stairs():
    eq(Solution().climbStairs(2), 2)
    eq(Solution().climbStairs(5), 8)
    eq(Solution().climbStairs(80), 37889062373143906)


def test_combine():
    eq(Solution().combine(4, 2), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
    eq(Solution().combine(1, 1), [[1]])


def test_min_stack():
    s = MinStack()
    s.push(-2); s.push(0); s.push(-3)
    eq(s.getMin(), -3)
    s.pop()
    eq(s.top(), 0)
    eq(s.getMin(), -2)
    s.push(-2)
    s.pop()
    eq(s.getMin(), -2, "duplicate minimums")


def test_trie():
    t = Trie()
    t.insert("apple")
    eq(t.search("apple"), True)
    eq(t.search("app"), False)
    eq(t.startsWith("app"), True)
    t.insert("app")
    eq(t.search("app"), True)
    eq(t.startsWith("b"), False)


def test_lru_cache():
    c = LRUCache(2)
    c.put(1, 1); c.put(2, 2)
    eq(c.get(1), 1)
    c.put(3, 3)                    # evicts 2 (1 was used more recently)
    eq(c.get(2), -1)
    c.put(4, 4)                    # evicts 1
    eq([c.get(1), c.get(3), c.get(4)], [-1, 3, 4])
    c.put(3, 30)                   # update counts as a use
    c.put(5, 5)                    # evicts 4
    eq([c.get(4), c.get(3)], [-1, 30])
