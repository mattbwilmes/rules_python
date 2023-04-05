load("@rules_python//python:defs.bzl", "py_library")
load("@my_pip_deps//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

py_library(
  name = "example-lightning",
  srcs = [
    "example_lightning.py",
  ],
  deps = [
    requirement("lightning"),
  ],
)
