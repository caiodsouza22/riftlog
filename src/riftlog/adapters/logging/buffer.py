"""Plain log lines stored on each step result."""

from __future__ import annotations

from datetime import datetime


def format_line(instant: datetime, level: str, message: str) -> str:
    stamp = instant.strftime("%Y-%m-%dT%H:%M:%SZ")
    return f"{stamp} {level.upper()} {message}"


class LogBuf:
    def __init__(self) -> None:
        self.lines: list[str] = []

    def write(self, instant: datetime, level: str, message: str) -> str:
        line = format_line(instant, level, message)
        self.lines.append(line)
        return line

    def clear(self) -> None:
        self.lines.clear()
