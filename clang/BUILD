load("@rules_cc//cc:defs.bzl", "cc_library")

cc_library(
    name = "solve",
    srcs = ["solve.cc"],
    hdrs = ["solve.h"],
    visibility = ["//visibility:public"],
)

cc_test(
    name = "test",
    srcs = ["solve_test.cc"],
    copts = ["-Iexternal/gtest/include"],
    deps = [
        ":solve",
        "@gtest//:gtest_main",
    ],
)
