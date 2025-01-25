# test_todo.py
import unittest
from unittest.mock import patch
from io import StringIO

# Assuming the application code is in a file called 'todo.py'
from todo import display_menu, view_tasks, add_task, remove_task, search_task

class TestToDoApp(unittest.TestCase):

    def setUp(self):
        """Set up the environment before each test."""
        self.tasks = ["Buy groceries", "Clean the house", "Finish homework"]

    def test_display_menu(self):
        """Test that the menu is displayed correctly."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            display_menu()
            output = mock_stdout.getvalue().strip().split('\n')
            self.assertEqual(output[0], "To-Do List")
            self.assertEqual(output[1], "1. View Tasks")
            self.assertEqual(output[2], "2. Add Task")
            self.assertEqual(output[3], "3. Remove Task")
            self.assertEqual(output[4], "4. Search task")
            self.assertEqual(output[5], "5. Exit")

    def test_view_tasks_empty(self):
        """Test the view tasks when no tasks exist."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            view_tasks([])
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "No tasks in the to-do list.")

    def test_view_tasks(self):
        """Test the view tasks when there are tasks."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            view_tasks(self.tasks)
            output = mock_stdout.getvalue().strip().split('\n')
            self.assertIn("1. Buy groceries", output)
            self.assertIn("2. Clean the house", output)
            self.assertIn("3. Finish homework", output)

    @patch('builtins.input', return_value="New task")
    def test_add_task(self, mock_input):
        """Test adding a new task."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            add_task(self.tasks)
            output = mock_stdout.getvalue().strip()
            self.assertIn('Added task: "New task"', output)
            self.assertIn("New task", self.tasks)

    @patch('builtins.input', return_value="2")
    def test_remove_task(self, mock_input):
        """Test removing a task."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            remove_task(self.tasks)
            output = mock_stdout.getvalue().strip()
            self.assertIn("Task 'Clean the house' has been removed from your list.", output)
            self.assertNotIn("Clean the house", self.tasks)

    @patch('builtins.input', return_value="Buy")
    def test_search_task_found(self, mock_input):
        """Test searching for an existing task."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            search_task(self.tasks)
            output = mock_stdout.getvalue().strip().split('\n')
            self.assertIn("Search Results:", output)
            self.assertIn("Buy groceries", output)

    @patch('builtins.input', return_value="Dentis")
    def test_search_task_not_found(self, mock_input):
        """Test searching for a non-existing task."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            search_task(self.tasks)
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "No tasks found matching that keyword.")

if __name__ == "__main__":
    unittest.main()
