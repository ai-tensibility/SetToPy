from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import sys
import setuptools


class BuildExt(build_ext):
    def build_extensions(self):
        compiler_type = self.compiler.compiler_type
        for ext in self.extensions:
            if compiler_type == "msvc":
                ext.extra_compile_args = ["/std:c++14"]
            else:
                ext.extra_compile_args = ["-std=c++14"]
        build_ext.build_extensions(self)


ext_modules = [
    Extension(
        "settopy",
        sources=["settopy/settopy_bindings.cpp", "settopy/settopy.cpp"],
        include_dirs=[],
        language="c++",
    ),
]

setup(
    name="SetToPy",
    version="0.1.0",
    author="Kan Yuenyong",
    author_email="kan.yuenyong@siamintelligenceunit.com",
    description="A Python library for efficient set operations using C++",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sikkha/SetToPy",
    license="Apache-2.0",
    packages=["settopy"],
    ext_modules=ext_modules,
    cmdclass={"build_ext": BuildExt},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C++",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["numpy", "pybind11",],
)
