import unittest
from LoadStore import LoadStore
from Memory import Memory

class TestLoadStoreMethods(unittest.TestCase):

    def test_load(self):
        memory = Memory()
        memory.setMainMemory(3, 1024)

        LoadStore.Load(memory, 3)

        self.assertEqual(memory.getAccumulator(), 1024)
    
    def test_loadIndexError(self):
        memory = Memory()

        with self.assertRaises(IndexError):
            LoadStore.Load(memory, 100)

    def test_store(self):
        memory = Memory()
        memory.setAccumulator(1024)

        LoadStore.Store(memory, 3)

        self.assertEqual(memory.getMainMemory(3), 1024)
    
    def test_storeIndexError(self):
        memory = Memory()

        with self.assertRaises(IndexError):
            LoadStore.Store(memory, 100)

if __name__ == '__main__':
    unittest.main()