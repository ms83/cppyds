#include<iostream>
#include<chrono>
#include<vector>
using namespace std;

const int N = 1<<26;

int main()
{
    auto start = std::chrono::system_clock::now();
    vector<int> v;

    for(int i=0; i<N; ++i) {
        v.push_back(i);
    }

    while(!v.empty()) {
        v.pop_back();
    }

    auto end = std::chrono::system_clock::now();
    auto elapsed = end - start;
    std::cout << std::chrono::duration<double>(elapsed).count();
}

// 3.46 secs (-O0 optimization)
// 0.24 secs (-O2 optimization)
