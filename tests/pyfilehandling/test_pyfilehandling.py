import pyfilehandling

def test_read_is_present_at_package_level():
    assert pyfilehandling.read != None

def test_write_is_present_at_package_level():
    assert pyfilehandling.write != None
