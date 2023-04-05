load("@rules_python//python:defs.bzl", "py_library")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")
package(default_visibility = ["//visibility:public"])

compile_pip_requirements(
    name = "my_pip_deps",
    extra_args = [
        "--allow-unsafe",
        "--index-url=https://pypi.org/simple",
        "--extra-index-url=https://download.pytorch.org/whl/cu117",
        "--resolver=backtracking",
    ],
    requirements_in = "requirements.txt",
    requirements_txt = "requirements_lock.txt",
)
