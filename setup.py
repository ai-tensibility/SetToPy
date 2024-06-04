from setuptools import setup, Extension
import pybind11
import os

ext_modules = [
    Extension(
        "settopy_bindings",
        ["settopy_bindings.cpp", "settopy.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++",
        extra_compile_args=[
            "-O3", "-funroll-loops", "-std=c++11",
            "-I/opt/homebrew/include",
            "-target", "arm64-apple-macos11",  # Ensure we target only arm64 architecture
            "-mmacosx-version-min=11.0"  # Ensure compatibility with macOS 11.0 or later
        ],
        extra_link_args=[
            "-L/opt/homebrew/opt/libomp/lib",
            "-lomp"
        ],
    ),
]

# Set environment variables to use LLVM clang/clang++
os.environ["CC"] = "/opt/homebrew/opt/llvm/bin/clang"
os.environ["CXX"] = "/opt/homebrew/opt/llvm/bin/clang++"

setup(
    name="settopy",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python library for set theory operations using C++ backend",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    ext_modules=ext_modules,
    zip_safe=False,
    install_requires=["pybind11"],
    setup_requires=["pybind11"],  # Ensure pybind11 is available during setup
)
