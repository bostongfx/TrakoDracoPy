cmake_minimum_required(VERSION 3.18.2)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

project(TrakoDracoPy)

find_package(PythonExtensions REQUIRED)
find_package(Cython REQUIRED)

# Note: To ensure includes of the form "draco/draco_header.h" work
#       as expected from a build directory, specify "draco" subdirectory.
add_subdirectory(
  draco
  ${CMAKE_CURRENT_BINARY_DIR}/draco
  )

add_subdirectory(TrakoDracoPy)
