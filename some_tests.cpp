
#include "gtest/gtest.h"
#include <thread>
#include <chrono>

using namespace std;

TEST(Various, Fails) {
	EXPECT_TRUE(false) << "Should fail anyway";
}

TEST(Various, Succeeds) {
	EXPECT_TRUE(true) << "Shouldn't fail";
}

TEST(Various, SomeTime) {
	this_thread::sleep_for(chrono::milliseconds(20));
	EXPECT_TRUE(true) << "Shouldn't fail";
}

TEST(Various, Exception) {
	EXPECT_TRUE(true) << "Shouldn't fail";
	throw 456;
	this is definitely not legit C++
}
