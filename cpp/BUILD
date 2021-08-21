load("@rules_cc//cc:defs.bzl", "cc_binary", "cc_library", "cc_test")

cc_library(
    name = "solve_lib",
    srcs = ["solve.cc"],
    hdrs = ["solve.h"],
    visibility = ["//visibility:public"],
)

cc_test(
    name = "solve_test",
    srcs = ["solve_test.cc"],
    copts = ["-Iexternal/gtest/include"],
    deps = [
        ":solve_lib",
        "@gtest//:gtest_main",
    ],
)

cc_binary(
    name = "run_solve",
    srcs = ["solve.cc"],
    deps = [
        ":solve_lib",
    ],
)
