load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
    name = "rules_python",
    sha256 = "a644da969b6824cc87f8fe7b18101a8a6c57da5db39caa6566ec6109f37d2141",
    strip_prefix = "rules_python-0.20.0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.20.0/rules_python-0.20.0.tar.gz",
)
load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()
load("@rules_python//python:repositories.bzl", "python_register_toolchains")
python_register_toolchains(
    name = "python3_10",
    python_version = "3.10",
    register_coverage_tool = True,
)
load("@python3_10//:defs.bzl", PYTHON_INTERPRETER_TARGET = "interpreter")
load("@rules_python//python:pip.bzl", "pip_parse")
PIP_EXTRA_ARGS = [
    "--index-url=https://pypi.org/simple",
    "--extra-index-url=https://download.pytorch.org/whl/cu117",
]
pip_parse(
    name = "my_pip_deps",
    extra_pip_args = PIP_EXTRA_ARGS,
    python_interpreter_target = PYTHON_INTERPRETER_TARGET,
    requirements_lock = "//:requirements_lock.txt",
)
load("@my_pip_deps//:requirements.bzl", "install_deps")
install_deps()
