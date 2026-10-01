from halloween.arts import get_art

def test_get_pumpkin():
    art = get_art("pumpkin")
    assert "() ()" in art

def test_unknown_art():
    try:
        get_art("dragon")
        assert False, "Should have raised KeyError"
    except KeyError:
        pass