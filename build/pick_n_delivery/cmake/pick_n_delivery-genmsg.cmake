# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "pick_n_delivery: 1 messages, 0 services")

set(MSG_I_FLAGS "-Ipick_n_delivery:/home/mik/labiagi_2020_21/pick_n_delivery/src/pick_n_delivery/msg;-Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(pick_n_delivery_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/mik/labiagi_2020_21/pick_n_delivery/src/pick_n_delivery/msg/NewGoal.msg" NAME_WE)
add_custom_target(_pick_n_delivery_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pick_n_delivery" "/home/mik/labiagi_2020_21/pick_n_delivery/src/pick_n_delivery/msg/NewGoal.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(pick_n_delivery
  "/home/mik/labiagi_2020_21/pick_n_delivery/src/pick_n_delivery/msg/NewGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pick_n_delivery
)

### Generating Services

### Generating Module File
_generate_module_cpp(pick_n_delivery
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pick_n_delivery
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(pick_n_delivery_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(pick_n_delivery_generate_messages pick_n_delivery_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/mik/labiagi_2020_21/pick_n_delivery/src/pick_n_delivery/msg/NewGoal.msg" NAME_WE)
add_dependencies(pick_n_delivery_generate_messages_cpp _pick_n_delivery_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pick_n_delivery_gencpp)
add_dependencies(pick_n_delivery_gencpp pick_n_delivery_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pick_n_delivery_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(pick_n_delivery
  "/home/mik/labiagi_2020_21/pick_n_delivery/src/pick_n_delivery/msg/NewGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pick_n_delivery
)

### Generating Services

### Generating Module File
_generate_module_eus(pick_n_delivery
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pick_n_delivery
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(pick_n_delivery_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(pick_n_delivery_generate_messages pick_n_delivery_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/mik/labiagi_2020_21/pick_n_delivery/src/pick_n_delivery/msg/NewGoal.msg" NAME_WE)
add_dependencies(pick_n_delivery_generate_messages_eus _pick_n_delivery_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pick_n_delivery_geneus)
add_dependencies(pick_n_delivery_geneus pick_n_delivery_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pick_n_delivery_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(pick_n_delivery
  "/home/mik/labiagi_2020_21/pick_n_delivery/src/pick_n_delivery/msg/NewGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pick_n_delivery
)

### Generating Services

### Generating Module File
_generate_module_lisp(pick_n_delivery
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pick_n_delivery
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(pick_n_delivery_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(pick_n_delivery_generate_messages pick_n_delivery_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/mik/labiagi_2020_21/pick_n_delivery/src/pick_n_delivery/msg/NewGoal.msg" NAME_WE)
add_dependencies(pick_n_delivery_generate_messages_lisp _pick_n_delivery_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pick_n_delivery_genlisp)
add_dependencies(pick_n_delivery_genlisp pick_n_delivery_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pick_n_delivery_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(pick_n_delivery
  "/home/mik/labiagi_2020_21/pick_n_delivery/src/pick_n_delivery/msg/NewGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pick_n_delivery
)

### Generating Services

### Generating Module File
_generate_module_nodejs(pick_n_delivery
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pick_n_delivery
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(pick_n_delivery_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(pick_n_delivery_generate_messages pick_n_delivery_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/mik/labiagi_2020_21/pick_n_delivery/src/pick_n_delivery/msg/NewGoal.msg" NAME_WE)
add_dependencies(pick_n_delivery_generate_messages_nodejs _pick_n_delivery_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pick_n_delivery_gennodejs)
add_dependencies(pick_n_delivery_gennodejs pick_n_delivery_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pick_n_delivery_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(pick_n_delivery
  "/home/mik/labiagi_2020_21/pick_n_delivery/src/pick_n_delivery/msg/NewGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pick_n_delivery
)

### Generating Services

### Generating Module File
_generate_module_py(pick_n_delivery
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pick_n_delivery
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(pick_n_delivery_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(pick_n_delivery_generate_messages pick_n_delivery_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/mik/labiagi_2020_21/pick_n_delivery/src/pick_n_delivery/msg/NewGoal.msg" NAME_WE)
add_dependencies(pick_n_delivery_generate_messages_py _pick_n_delivery_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pick_n_delivery_genpy)
add_dependencies(pick_n_delivery_genpy pick_n_delivery_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pick_n_delivery_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pick_n_delivery)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pick_n_delivery
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(pick_n_delivery_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(pick_n_delivery_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pick_n_delivery)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pick_n_delivery
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(pick_n_delivery_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(pick_n_delivery_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pick_n_delivery)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pick_n_delivery
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(pick_n_delivery_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(pick_n_delivery_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pick_n_delivery)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pick_n_delivery
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(pick_n_delivery_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(pick_n_delivery_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pick_n_delivery)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pick_n_delivery\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pick_n_delivery
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(pick_n_delivery_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(pick_n_delivery_generate_messages_py std_msgs_generate_messages_py)
endif()
