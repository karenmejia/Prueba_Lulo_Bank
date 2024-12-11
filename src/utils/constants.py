from enum import Enum
import os

class constants(Enum):
    year = 2024
    month = 1
    main_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..'))