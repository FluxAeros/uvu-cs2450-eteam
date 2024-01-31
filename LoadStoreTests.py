import unittest
from LoadStore import LoadStore
from Memory import Memory

class TestMemoryMethods(unittest.TestCase):

    def test_load(self):
        memory = Memory()
        memory.mainMemory[3] = 1024

        LoadStore.Load(3, memory)

        self.assertEqual(memory.accumulator, 1024)
    
    def test_loadIndexError(self):
        memory = Memory()

        with self.assertRaises(IndexError):
            LoadStore.Load(100, memory)

    def test_store(self):
        memory = Memory()
        memory.accumulator = 1024

        LoadStore.Store(3, memory)

        self.assertEqual(memory.mainMemory[3], 1024)
    
    def test_storeIndexError(self):
        memory = Memory()

        with self.assertRaises(IndexError):
            LoadStore.Store(100, memory)

if __name__ == '__main__':
    unittest.main()