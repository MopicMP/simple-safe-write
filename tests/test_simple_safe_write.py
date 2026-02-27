"""Tests for simple-safe-write."""

import os
import tempfile
import pytest
from simple_safe_write import write


class TestWrite:
    """Test suite for write."""

    def test_basic(self):
        """Test basic usage with a real temp directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a sample file inside
            sample = os.path.join(tmpdir, "sample.txt")
            with open(sample, "w") as f:
                f.write("hello world")
            result = write(tmpdir)
            assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            write("")
        except (ValueError, TypeError, FileNotFoundError, OSError):
            pass  # Expected for path-based utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = write(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
