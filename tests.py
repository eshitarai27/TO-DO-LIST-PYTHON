import unittest
import task_manager

class TestTaskManager(unittest.TestCase):
    def test_add_task(self):
        task_manager.add_task("Test Task")
        self.assertIn({"task": "Test Task", "done": False}, task_manager.list_tasks())

if __name__ == "__main__":
    unittest.main()
