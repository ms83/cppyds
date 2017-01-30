#include<iostream>
#include<chrono>
#include<stack>
using namespace std;

const int N = 1<<26;

int main()
{
    auto start = std::chrono::system_clock::now();
    stack<int> s;

    for(int i=0; i<N; ++i) {
        s.push(i);
    }

    for(int i=0; i<N; ++i) {
        s.pop();
    }

    auto end = std::chrono::system_clock::now();
    auto elapsed = end - start;
    std::cout << std::chrono::duration<double>(elapsed).count();
}

// 2.29 secs (-O0 optimization)
// 0.35 secs (-O2 optimization)
