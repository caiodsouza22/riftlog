"""Min-heap of pending work. Higher priority pops first."""

from __future__ import annotations

import heapq
from dataclasses import dataclass, field


@dataclass(order=True)
class _Node:
    sort_key: tuple
    seq: int
    payload: object = field(compare=False)


class PriorityQueue:
    def __init__(self) -> None:
        self._heap: list[_Node] = []
        self._seq = 0

    def push(self, payload: object, priority: int = 0) -> None:
        self._seq += 1
        heapq.heappush(self._heap, _Node((-priority, self._seq), self._seq, payload))

    def pop(self) -> object:
        node = heapq.heappop(self._heap)
        return node.payload

    def empty(self) -> bool:
        return not self._heap

    def __len__(self) -> int:
        return len(self._heap)
