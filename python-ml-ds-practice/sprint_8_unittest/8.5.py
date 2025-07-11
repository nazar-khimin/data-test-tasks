import unittest


class Worker:
    def __init__(self, name, salary=0):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.name = name
        self.salary = salary

    def get_tax_value(self):
        tax_brackets = [
            (1000, 0),  # 0-1000: 0%
            (3000, 0.10),  # 1001-3000: 10%
            (5000, 0.15),  # 3001-5000: 15%
            (10000, 0.21),  # 5001-10000: 21%
            (20000, 0.30),  # 10001-20000: 30%
            (50000, 0.40),  # 20001-50000: 40%
            (float('inf'), 0.47)  # 50001+: 47%
        ]

        total_tax = 0
        previous_limit = 0
        remaining_salary = self.salary

        for limit, rate in tax_brackets:
            if remaining_salary <= 0:
                break

            taxable_amount = min(remaining_salary, limit - previous_limit)
            tax = taxable_amount * rate
            total_tax += tax

            remaining_salary -= taxable_amount
            previous_limit = limit

        return round(total_tax, 2)


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ("w1", 1000, 0.0),  # No tax below 1000
            ("w2", 1001, 0.1),  # 1 * 10% = 0.1
            ("w3", 3000, 200.0),  # 2000 * 10% = 200
            ("w4", 3001, 200.15),  # 2000 * 10% + 1 * 15% = 200.15
            ("w5", 5000, 500.0),  # 2000 * 10% + 2000 * 15% = 500
            ("w6", 10000, 1550.0),  # 2000 * 10% + 2000 * 15% + 5000 * 21% = 1550
            ("w7", 20000, 4550.0),  # 2000 * 10% + 2000 * 15% + 5000 * 21% + 10000 * 30% = 4550
            ("w8", 50000, 16550.0),  # 2000 * 10% + 2000 * 15% + 5000 * 21% + 10000 * 30% + 30000 * 40% = 16550
            ("w9", 100000, 40050.0) # 2000 * 10% + 2000 * 15% + 5000 * 21% + 10000 * 30% + 30000 * 40% + 50000 * 47% = 40050
        ]
        self.workers = {name: Worker(name, salary) for name, salary, _ in self.test_cases}

    def tearDown(self):
        self.workers = {}

    def test_get_tax_value(self):
        for name, salary, expected_tax in self.test_cases:
            with self.subTest(worker=name, salary=salary):
                self.assertEqual(self.workers[name].get_tax_value(), expected_tax)

    @unittest.expectedFailure
    def test_negative_salary(self):
            worker = Worker("Invalid", -500)

    def test_salary_zero(self):
        worker = Worker("Zero", 0)
        self.assertEqual(worker.get_tax_value(), 0.0)

worker = Worker("Vika", 100000)
print(worker.get_tax_value())