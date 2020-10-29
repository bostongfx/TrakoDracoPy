
include_directories(
  "${CMAKE_CURRENT_SOURCE_DIR}"
  "${CMAKE_CURRENT_BINARY_DIR}"
  "${draco_SOURCE_DIR}/src"
  "${draco_BINARY_DIR}" # Remove this
  )

add_cython_target(_TrakoDracoPy CXX)
add_library(_TrakoDracoPy MODULE ${_TrakoDracoPy})
python_extension_module(_TrakoDracoPy)

target_link_libraries(_TrakoDracoPy
  draco
  dracodec
  dracoenc
  )

install(TARGETS _TrakoDracoPy LIBRARY DESTINATION TrakoDracoPy)