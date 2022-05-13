from unittest import mock

from employee.crud.Employee import Employee
import unittest


class TestEmployee(unittest.TestCase):

    @mock
    # UPDATE
    def test_update_emp_details(self):
        Ram = Employee(1987, 'Ram Kumar', 8000)
        emp_sal = Ram.update_emp_details()
        self.assertEquals(emp_sal, 34500, "Sal Hike is Wrong")


if __name__ == '__main__':
    unittest.main()
