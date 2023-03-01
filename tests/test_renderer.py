from pyhina.renderer import SetuptoolsPackage, ProjectInfo


def test_init():
    assert SetuptoolsPackage() is not None


def test_render():
    r = SetuptoolsPackage()
    d = ProjectInfo(
        project_name="test-proj",
        package_name="test_package",
        python_minimum="3.8",
    )

    for path, data in r.render_as_string(d):
        assert len(path) > 0
        assert len(data) > 0
