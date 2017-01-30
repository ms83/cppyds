#include<iostream>
#include<chrono>
#include<queue>
using namespace std;

const int N = 1<<20;

int main()
{
    auto start = std::chrono::system_clock::now();
    queue<int> q;

    for(int i=0; i<N; ++i) {
        q.push(i);
    }

    for(int i=0; i<N; ++i) {
        q.pop();
    }

    auto end = std::chrono::system_clock::now();
    auto elapsed = end - start;
    std::cout << std::chrono::duration<double>(elapsed).count();
}

// 0.036 secs (-O0 optimization)
// 0.006 secs (-O2 optimization)
