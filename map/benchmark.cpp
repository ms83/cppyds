#include<iostream>
#include<chrono>
#include<map>
using namespace std;

const int N = 1<<20;

int main()
{
    int total = 0;
    auto start = std::chrono::system_clock::now();
    map<int, int> m;

    for(int i=0; i<N; ++i) {
        m[i] = i;
    }

    for(int i=0; i<N; ++i) {
        total += m[i];
    }

    for(int i=0; i<N; ++i) {
        m.erase(i);
    }

    auto end = std::chrono::system_clock::now();
    auto elapsed = end - start;
    std::cout << std::chrono::duration<double>(elapsed).count();

    std::cout << total;
}

// 3.03 secs (-O0 optimization)
// 0.58 secs (-O2 optimization)
