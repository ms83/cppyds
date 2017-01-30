#include<iostream>
#include<chrono>
#include<set>
using namespace std;

const int N = 1<<20;

int main()
{
    auto start = std::chrono::system_clock::now();
    set<int> s;

    for(int i=0; i<N; ++i) {
        s.insert(i);
    }

    for(int i=0; i<N; ++i) {
        set<int>::iterator it = s.find(i);
    }

    for(int i=0; i<N; ++i) {
        s.erase(i);
    }

    auto end = std::chrono::system_clock::now();
    auto elapsed = end - start;
    std::cout << std::chrono::duration<double>(elapsed).count();
}

// 2.94 secs (-O0 optimization)
// 0.58 secs (-O2 optimization)
