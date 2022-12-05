
from pathlib import Path

print(max([sum(map(int, c.strip().split('\n'))) for c in [i for i in Path("input.txt").read_text().split('\n\n')]]))