import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from backend.src.models.bd_model import Language
# Popule a linguagem

Language.create_language('Python')
Language.create_language('Javascript')
Language.create_language('Java')
Language.create_language('Rust')