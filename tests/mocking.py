import pytest

import os
import tempfile

@pytest.fixture
def temp_dir(request):
    temp_dir_path = tempfile.gettempdir()
    pyfile_temp_dir = os.path.join(temp_dir_path, "pyfilehandling")
    os.mkdir(pyfile_temp_dir)
    yield temp_dir_path
    os.rmdir(pyfile_temp_dir)
