#include<iostream>
#include<chrono>
#include<deque>
using namespace std;

const int N = 1<<26;

int main()
{
    auto start = std::chrono::system_clock::now();
    deque<int> dq;

    for(int i=0; i<N; ++i) {
        dq.push_back(i);
        dq.push_front(i);
    }

    for(int i=0; i<N; ++i) {
        dq.pop_back();
        dq.pop_front();
    }

    auto end = std::chrono::system_clock::now();
    auto elapsed = end - start;
    std::cout << std::chrono::duration<double>(elapsed).count();
}

// 3.62 secs (-O0 optimization)
// 0.60 secs (-O2 optimization)
