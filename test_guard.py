import unittest
from guard import check


class GuardTests(unittest.TestCase):
    def test_allows_added_optional_field(self):
        self.assertTrue(check({"properties": {"id": {"type": "string"}}}, {"properties": {"id": {"type": "string"}, "note": {"type": "string"}}})["compatible"])

    def test_rejects_removed_field(self):
        report = check({"properties": {"id": {"type": "string"}}}, {"properties": {}})
        self.assertEqual(report["issues"][0]["kind"], "field-removed")

    def test_rejects_new_required_field(self):
        report = check({"properties": {}}, {"properties": {"region": {"type": "string"}}, "required": ["region"]})
        self.assertEqual(report["issues"][0]["kind"], "required-added")


if __name__ == "__main__":
    unittest.main()
