import pytest


@pytest.fixture(scope="class")
def clear_resource():
    yield
    import apis
    # apis.case_obj.delete_case()
    pass
