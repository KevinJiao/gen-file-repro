load("//:macros.bzl", "create_genrule")
py_test(
    name = "compare_files",
    srcs = ["compare_files.py"],
    data = [
        "ref.txt",
        ":test.txt",
    ],
)

create_genrule(
    name = "gen_test",
    srcs = [],
    out = ["test.txt"],
    cmd = "$(location gen_test.sh) > \"$@\"",
    exec_tools = [":gen_test.sh"],
)
