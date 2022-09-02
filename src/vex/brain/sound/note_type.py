"""Musical Note Types."""


from collections.abc import Sequence
from enum import IntEnum

from ...util.doc import robotmesh_doc


__all__: Sequence[str] = ('NoteType',)


@robotmesh_doc("""
    Musical note to play.

    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_note_type.html
""")
class NoteType(IntEnum):
    """Musical Note."""

    silence: int = 0   # Stop playing/play a silence.
    C: int = 1
    D: int = 2
    E: int = 3
    F: int = 4
    G: int = 5
    A: int = 6
    B: int = 7