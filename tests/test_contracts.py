"""极限测试样品闭环基础契约测试。"""

import unittest

from extreme_testing import TestSample, unique_by_identity


class ContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.values = {'sample_code': 'sample-code-001', 'batch_code': 'batch-code-001', 'test_plan': 'test-plan-001', 'custody_state': 'draft'}

    def test_fingerprint_is_stable(self) -> None:
        left = TestSample(**self.values)
        right = TestSample(**dict(reversed(list(self.values.items()))))
        self.assertEqual(left.fingerprint(), right.fingerprint())

    def test_evolve_keeps_original(self) -> None:
        original = TestSample(**self.values)
        change_key = next(key for key, value in self.values.items() if isinstance(value, str))
        changed = original.evolve(**{change_key: "revised-value"})
        self.assertNotEqual(original.fingerprint(), changed.fingerprint())
        self.assertEqual(getattr(original, change_key), self.values[change_key])

    def test_conflicting_identity_is_rejected(self) -> None:
        first = TestSample(**self.values)
        changed_values = dict(self.values)
        change_key = next(key for key in self.values if key != "sample_code")
        changed_values[change_key] = 2 if isinstance(changed_values[change_key], int) else "conflict"
        second = TestSample(**changed_values)
        with self.assertRaises(ValueError):
            unique_by_identity([first, second])


if __name__ == "__main__":
    unittest.main()
