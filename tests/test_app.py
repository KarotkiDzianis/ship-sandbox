"""tests/test_app.py — the only test this sandbox needs: the app actually
starts and answers both routes. Run by scripts/ship/test in CI.
"""
import subprocess
import sys
import time
import unittest
import urllib.request
from pathlib import Path

APP = Path(__file__).resolve().parent.parent / "app" / "main.py"


class TestApp(unittest.TestCase):
    def test_serves_root_and_healthz(self):
        proc = subprocess.Popen([sys.executable, str(APP)])
        try:
            for _ in range(20):
                try:
                    urllib.request.urlopen("http://127.0.0.1:8091/healthz", timeout=0.5)
                    break
                except Exception:
                    time.sleep(0.25)
            else:
                self.fail("app never came up")

            health = urllib.request.urlopen("http://127.0.0.1:8091/healthz")
            self.assertEqual(health.status, 200)

            root = urllib.request.urlopen("http://127.0.0.1:8091/")
            self.assertIn(b"ship-sandbox ok", root.read())
        finally:
            proc.terminate()
            proc.wait(timeout=5)


if __name__ == "__main__":
    unittest.main()
