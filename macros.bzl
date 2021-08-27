def create_genrule(name, srcs, out, cmd, exec_tools):

  native.genrule(
    name = name,
    srcs = srcs,
    outs = out,
    cmd = cmd,
    exec_tools = exec_tools,
   )

