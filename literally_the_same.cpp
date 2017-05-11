
// Haha not literally, just mostly the same

vector<int> otherStupidFunction2() {
	// Some comment
	vector<int> res;
	for (int i=0; i<50; i++) {
		if (i%3 == 0) {
			std::cout << "Divisible by 3";
		} else if ((i+1)%2 == 0) {
			std::cout << "Blablabla";
		}
		
		auto f = [&](int& j) {
			i += j;
			static int k = 6;
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
}
