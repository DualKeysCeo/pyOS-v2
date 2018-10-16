import sys
import os

def termCols():
    try:
        columns, rows = os.get_terminal_size(0)
        return columns
    except OSError:
        columns, rows = os.get_terminal_size(1)
        return columns