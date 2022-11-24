from enum import Enum
from typing import List


def _decrease_count1(deepths) -> int:
    count = 0
    for i in range(len(deepths)-1):
        if deepths[i] < deepths[i+1]:
            count += 1
    return count


def _decrease_count2(deepths) -> int:
    count = 0
    for i in range(len(deepths)-4):
        first_window = deepths[i] + deepths[i+1] + deepths[i+1]
        second_window = deepths[i+1] + deepths[i+2] + deepths[i+3]
        if first_window < second_window:
            count += 1
    return count


def compute_puzzle1(deepths: List[int]) -> int:
    return _decrease_count1(deepths)


def compute_puzzle2(deepths: List[int]) -> int:
    return _decrease_count2(deepths)
