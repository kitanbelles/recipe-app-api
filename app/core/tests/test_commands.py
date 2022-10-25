"""
test custom django management command 
"""

from unittest.mock import patch

from psycopg2 import OperationalError as Pyscopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

class CommandTest (SimpleTestCase):
    """test commands."""

    def test_waitfor_db_ready(self):
        """Test waiting for database if database is ready"""
