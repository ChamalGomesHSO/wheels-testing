import zxingcpp

def test_import_and_version():
    """
    Tests that zxingcpp can be imported and has a __version__ attribute.
    """
    print(f"zxing-cpp version: {zxingcpp.__version__}")
    assert hasattr(zxingcpp, '__version__')
    assert isinstance(zxingcpp.__version__, str)
