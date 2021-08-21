#include "solve.h"
#include "gtest/gtest.h"

TEST(test_test, content) {
    EXPECT_EQ(1, 2);
}
int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}