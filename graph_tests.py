import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())

    # my tests
    # test helper to create test file
    def generate_test_file(self, vertices):
        with open('my_test.txt', 'w') as f:
            for i in range(0, len(vertices), 2):
                f.write('{} {}\n'.format(vertices[i], vertices[i+1]))

    # simple test
    def test_03(self):
        test_graph = ['v1', 'v2']
        self.generate_test_file(test_graph)
        g = Graph('my_test.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2']])
        self.assertTrue(g.is_bipartite())

    # test1.txt backwards to test our sorting
    def test_04(self):
        test_graph = ['v8', 'v6', 'v9', 'v8', 'v7', 'v9', 'v6', 'v7', 'v1', 'v5', 'v1', 'v4', 'v1', 'v3', 'v1', 'v2']
        self.generate_test_file(test_graph)
        g = Graph('my_test.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())

    # star
    def test_05(self):
        test_graph = ['v1', 'v3', 'v1', 'v4', 'v2', 'v5', 'v2', 'v4', 'v3', 'v5']
        self.generate_test_file(test_graph)
        g = Graph('my_test.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5']])
        self.assertFalse(g.is_bipartite())

    # 3 triangles out of order?
    def test_06(self):
        test_graph = ['v4', 'v5', 'v5', 'v6', 'v6', 'v4', 'v1', 'v2', 'v1', 'v3', 'v3', 'v2', 'v7', 'v8', 'v9', 'v7', 'v9', 'v8']
        self.generate_test_file(test_graph)
        g = Graph('my_test.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v5', 'v6'], ['v7', 'v8', 'v9']])
#        self.assertFalse(g.is_bipartite())

    # circle with a tail
    def test_07(self):
        test_graph = ['v1', 'v2', 'v2', 'v3', 'v3', 'v4', 'v4', 'v5', 'v6', 'v1', 'v6', 'v7', 'v7', 'v8']
        self.generate_test_file(test_graph)
        g = Graph('my_test.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8']])
        self.assertTrue(g.is_bipartite())

    # square and pair
    def test_08(self):
        test_graph = ['v3', 'v4', 'v4', 'v5', 'v5', 'v6', 'v6', 'v3', 'v1', 'v2']
        self.generate_test_file(test_graph)
        g = Graph('my_test.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2'], ['v3', 'v4', 'v5', 'v6']])
        self.assertTrue(g.is_bipartite())

    # FileNotFound
    def test_09(self):
        with self.assertRaises(SystemExit) as context:
            Graph('fake_file.txt')

    # test get_vertex None
    def test_10(self):
        g = Graph('test1.txt')
        self.assertEqual(g.get_vertex('fake_vertex'), None)

    # stack tests
    def test_stack_empty_pop(self):
        stack = Stack(5)
        with self.assertRaises(IndexError):
           stack.pop()

    def test_stack_push_full(self):
        stack = Stack(5)
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertEqual(stack.size(), 5)
        with self.assertRaises(IndexError):
           stack.push(2)

    def test_stack_peek(self):
        stack = Stack(5)
        stack.push(5)
        self.assertEqual(stack.peek(), 5)
        stack.pop()
        with self.assertRaises(IndexError):
           stack.peek()
 
    #queue tests
    def test_empty_dequeue(self):
        queue = Queue(5)
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_enqueue_full(self):
        queue = Queue(5)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        self.assertEqual(queue.size(), 5)
        with self.assertRaises(IndexError):
            queue.enqueue(2)
 
    def test_queue_peek(self):
        queue = Queue(5)
        queue.enqueue(5)
        self.assertEqual(queue.peek(), 5)
        queue.dequeue()
        with self.assertRaises(IndexError):
            queue.peek()

if __name__ == '__main__':
   unittest.main()
