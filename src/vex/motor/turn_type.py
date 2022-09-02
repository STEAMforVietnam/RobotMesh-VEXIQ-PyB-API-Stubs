"""Movement Turn Types."""


from collections.abc import Sequence
from enum import IntEnum

from ..util.doc import robotmesh_doc


__all__: Sequence[str] = ('TurnType',)


@robotmesh_doc("""
    Left or right turn.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_turn_type.html
""")
class TurnType(IntEnum):
    """Movement Turn Types."""

    LEFT: int = 0
    RIGHT: int = 1