load("@rules_python//python:defs.bzl", "py_test")
load("@my_pip_deps//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

py_test(
  name = "test-lightning",
  main = "test_lightning.py",
 srcs = ["test_lightning.py"],
  deps = [
   "//lightning:example-lightning",
    requirement("pytest"),
  ]
)
