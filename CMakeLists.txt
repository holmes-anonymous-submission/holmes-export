cmake_minimum_required (VERSION 3.0)
project (ucb-holmes-export)

find_path(CMAKE_FOLDER NAMES cmake/emp-tool-config.cmake)
include(${CMAKE_FOLDER}/cmake/emp-base.cmake)

find_package(emp-ot REQUIRED)
include_directories(${EMP-OT_INCLUDE_DIRS})

find_package(emp-zk-holmes REQUIRED)
include_directories(${EMP-ZK-HOLMES_INCLUDE_DIRS})

find_package(GMP REQUIRED)
include_directories(${GMP_INCLUDE_DIR})
find_package(FLINT REQUIRED)
include_directories(${FLINT_INCLUDE_DIR}/flint)
find_package(MPFR REQUIRED)
include_directories(${MPFR_INCLUDE_DIR})

find_package(OpenMP)

if (${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
   set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS} -ggdb -Wno-ignored-attributes -Xpreprocessor -fopenmp")
   set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS} -Wno-ignored-attributes -Xpreprocessor -fopenmp")
else()
   set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS} -ggdb -Wno-ignored-attributes -fopenmp")
   set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS} -Wno-ignored-attributes -fopenmp")
endif()

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin/)

set(binaries_export export_range_check export_histogram_numeric export_histogram_nominal export_mean_check export_trimmed_mean export_variance_check export_dataset_1 export_dataset_2 export_dataset_3)
foreach(bin ${binaries_export})
   add_executable("${bin}" "export/${bin}.cpp")
   target_link_libraries("${bin}" ${EMP-OT_LIBRARIES} ${EMP-ZK-HOLMES_LIBRARIES} ${GMP_LIBRARIES} ${MPFR_LIBRARIES} ${FLINT_LIBRARIES} OpenMP::OpenMP_CXX)
endforeach()