cmake_minimum_required(VERSION 3.0)
project(SetTopy)

set(CMAKE_CXX_STANDARD 11)

# Define the SetTopy library
add_library(SetTopy SHARED settopy.cpp)

# Include directories for Python bindings
include_directories(${PYTHON_INCLUDE_DIRS})

# Link libraries for Python bindings
target_link_libraries(SetTopy ${PYTHON_LIBRARIES})
