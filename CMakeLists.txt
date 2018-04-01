cmake_minimum_required(VERSION 3.0)
find_package(install_py)


project(python_scripter VERSION 1.0.0)


message("\nProject Name           : ${PROJECT_NAME}")
message("Project Source Dir     : ${PROJECT_SOURCE_DIR}")
message("Project Version        : ${PROJECT_VERSION}\n")


add_subdirectory(src)

add_subdirectory(src/_widgets/ui)

add_subdirectory(scripts)