import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("installer", ROOT / "scripts" / "install.py")
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def test_fresh_install_preserves_every_file(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder) / "skills"
            installer.install(destination, installer.SKILLS)
            for source in installer.SOURCE.rglob("*"):
                if source.is_file():
                    self.assertEqual(source.read_bytes(), (destination / source.relative_to(installer.SOURCE)).read_bytes())

    def test_conflict_does_not_modify_any_requested_skill(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder)
            protected = destination / "pnas-figure"
            protected.mkdir()
            sentinel = protected / "custom.txt"
            sentinel.write_text("keep my customization", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                installer.install(destination, installer.SKILLS)
            self.assertFalse((destination / "pnas-writing").exists())
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "keep my customization")

    def test_dry_run_creates_nothing(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder) / "not-created"
            installer.install(destination, installer.SKILLS, dry_run=True)
            self.assertFalse(destination.exists())

    def test_single_selection(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder)
            installer.install(destination, ["pnas-polishing"])
            self.assertEqual([p.name for p in destination.iterdir()], ["pnas-polishing"])
            self.assertTrue((destination / "pnas-polishing" / "references" / "style-guardrails.md").is_file())

    def test_invalid_name_cannot_escape_destination(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(ValueError):
                installer.install(Path(folder) / "skills", ["../outside"])
            self.assertEqual(list(Path(folder).iterdir()), [])


if __name__ == "__main__":
    unittest.main()
