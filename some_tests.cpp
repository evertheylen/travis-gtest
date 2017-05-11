
#include "gtest/gtest.h"
#include <thread>
#include <chrono>
#include <iostream>
#include <vector>

using namespace std;

TEST(Various__ABC, Fails) {
	EXPECT_TRUE(false) << "Should fail anyway";
}

TEST(Various__ABC, Succeeds) {
	EXPECT_TRUE(true) << "Shouldn't fail";
}

TEST(Various__XYZ, SomeTime) {
	this_thread::sleep_for(chrono::milliseconds(20));
	EXPECT_TRUE(true) << "Shouldn't fail";
}

TEST(Various__XYZ, Exception) {
	EXPECT_TRUE(true) << "Shouldn't fail";
	throw 456;
}


vector<int> someStupidFunction() {
	// Some comment
	vector<int> res;
	for (int i=0; i<50; i++) {
		if (i%3 == 0) {
			std::cout << "Divisible by 3";
		} else if ((i+1)%2 == 0) {
			std::cout << "Blabla";
		}
		
		auto f = [&](int& j) {
			i += j;
			static int k = 5;
			k += i*j;
			i -= k;
			return k;
		}
		
		while (i%45 == 13) {
			f(f(i));
			std::cout << "i is currently " << i << endl;
		}
		
		res.push_back(i%2 == 0 ? i : i*2);
	}
	
	return res;
}
