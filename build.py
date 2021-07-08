from distutils.core import Extension

ext_modules = [
    Extension("factorial", sources=["src/factorial.c"]),
]


def build(setup_kwargs):
    setup_kwargs.update({"ext_modules": ext_modules})
