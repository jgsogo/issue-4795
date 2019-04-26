
cmake_minimum_required(VERSION 2.8.12)
project(lightfoot)

find_package(zlib)

add_executable(iprc main.cpp)
target_link_libraries(iprc zlib::zlib)
