buildifier WORKSPACE

find . -not -path "./bazel-*" -name BUILD | xargs buildifier

find . -not -path "./bazel-*" -type f \( -iname "*.cc" -o -iname "*.c" -o -iname "*.cpp" -o -iname "*.h" -o -iname "*.hpp" \) | \
    xargs clang-format -i --sort-includes
