from distutils.dist import Distribution
from pathlib import Path

from build import ext_modules

FACTORIALS = [
    1,
    1,
    2,
    6,
    24,
    120,
    720,
    5040,
    40320,
    362880,
    3628800,
    39916800,
    479001600,
    6227020800,
    87178291200,
    1307674368000,
    20922789888000,
]


def pytest_sessionstart(session):
    dist = Distribution(attrs={"ext_modules": ext_modules})
    build_ext_cmd = dist.get_command_obj("build_ext")
    build_ext_cmd.ensure_finalized()
    build_ext_cmd.inplace = 1
    build_ext_cmd.run()
    session.factorial_obj = Path(build_ext_cmd.get_ext_fullpath("factorial"))


def pytest_sessionfinish(session):
    session.factorial_obj.unlink()
