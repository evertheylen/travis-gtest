cmake_minimum_required(VERSION 3.2.2)

set(PROJECT_NAME travis-gtest)
project(${PROJECT_NAME} CXX)

# Colors
if(NOT WIN32)
  string(ASCII 27 Esc)
  set(ColorReset  "${Esc}[m")
  set(ColorBold   "${Esc}[1m")
  set(Red         "${Esc}[31m")
  set(Green       "${Esc}[32m")
  set(Yellow      "${Esc}[33m")
  set(Blue        "${Esc}[34m")
  set(Magenta     "${Esc}[35m")
  set(Cyan        "${Esc}[36m")
  set(White       "${Esc}[37m")
  set(BoldRed     "${Esc}[1;31m")
  set(BoldGreen   "${Esc}[1;32m")
  set(BoldYellow  "${Esc}[1;33m")
  set(BoldBlue    "${Esc}[1;34m")
  set(BoldMagenta "${Esc}[1;35m")
  set(BoldCyan    "${Esc}[1;36m")
  set(BoldWhite   "${Esc}[1;37m")
endif()


message("\n${BoldCyan}>>> Settings${ColorReset}")
get_filename_component(TEST_ROOT . ABSOLUTE)
get_filename_component(WORKSPACE_ROOT ${TEST_ROOT}/.. ABSOLUTE)

message("CMAKE_BUILD_TYPE: ${CMAKE_BUILD_TYPE}")
message("PROJECT_BINARY_DIR: ${PROJECT_BINARY_DIR}")

message("TEST_ROOT: ${TEST_ROOT}")
message("WORKSPACE_ROOT: ${WORKSPACE_ROOT}")

# Includes
set(INCLUDES

)

message("INCLUDES: ${INCLUDES}")
include_directories(${INCLUDES})

# Sources
set(SOURCES
    
)

message("SOURCES: ${SOURCES}")

enable_testing()

#set(BUILD_GTEST ON CACHE BOOL "Build Google Test library")
#set(BUILD_GMOCK OFF CACHE BOOL "Build Google Mock library")
add_subdirectory(gtest)

set(LIBS
    gtest
    gtest_main
)

message("LIBS: ${LIBS}")

message("\n${BoldCyan}>>> Tests${ColorReset}")

# add/delete tests here
set(TEST_LIST
    some_tests
)

foreach(TEST_NAME ${TEST_LIST})
    message("add executable: ${TEST_NAME}")
    set(EXEC_NAME ${TEST_NAME})

    # todo: add/delete sources
    add_executable(${EXEC_NAME}
        ${TEST_NAME}.cpp
        ${SOURCES}
    )
    set_property(TARGET ${EXEC_NAME} PROPERTY CXX_STANDARD 11)
    set_property(TARGET ${EXEC_NAME} PROPERTY CXX_STANDARD_REQUIRED ON)

    target_link_libraries(${EXEC_NAME} ${LIBS})
    add_test(
        NAME ${EXEC_NAME}
        COMMAND $<TARGET_FILE:${EXEC_NAME}>
    )
endforeach(TEST_NAME)
