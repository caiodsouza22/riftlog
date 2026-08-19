"""Builtin step callables. Importing this package registers them on GLOBAL."""

from riftlog.tasks import core as _core  # noqa: F401
from riftlog.tasks import ops_math as _ops_math  # noqa: F401
from riftlog.tasks import ops_seq as _ops_seq  # noqa: F401
from riftlog.tasks import ops_text as _ops_text  # noqa: F401

__all__ = ["core"]
