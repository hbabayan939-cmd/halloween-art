from halloween.arts.pumpkin import PUMPKIN
from halloween.arts.ghost import GHOST
from halloween.arts.skeleton import SKELETON

ARTS = {
    "pumpkin": PUMPKIN,
    "ghost": GHOST,
    "skeleton": SKELETON,
}

def get_art(name: str) -> str:
    if name == "all":
        return "\n".join(ARTS.values())
    if name not in ARTS:
        raise KeyError(f"Unknown art: {name}")
    return ARTS[name]