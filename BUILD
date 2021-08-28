py_test(
    name = "compare_files",
    srcs = ["compare_files.py"],
    data = [
        "ref.txt",
        ":aaa_test.txt",
    ],
)

genrule(
    name = "gen_test",
    srcs = [],
    outs = ["aaa_test.txt"],
    cmd = "$(location gen_test.sh) > \"$@\"",
    exec_tools = [":gen_test.sh"],
)
