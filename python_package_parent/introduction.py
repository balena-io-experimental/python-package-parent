"""Test the capabilities of Python Package Child."""
from python_package_child import Child


def child_greet() -> None:
    """Greeting of a child."""
    child = Child()
    child.greet()
