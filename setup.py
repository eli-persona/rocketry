import sys

sys.stderr.write(
    """
Unsupported installation method: python setup.py
Please use `python -m pip install .` instead.
"""
)
# sys.exit(1)
from setuptools import setup

setup(
    name="rocketry",
    install_requires=[
        "python-dateutil",
        "redbird @ git+https://github.com/eli-persona/red-bird.git@5e884da61abf1ef01d9a8ef0731ed89ea65964ab",
        "pydantic",
    ],
)
