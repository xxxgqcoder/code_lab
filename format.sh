buildifier WORKSPACE

find . -not -path './bazel-*' -name BUILD | xargs buildifier

find . -not -path './bazel-*' -name "*.cc" | xargs clang-format -i --sort-includes

find . -not -path './bazel-*' -name "*.h" | xargs clang-format -i --sort-includes
