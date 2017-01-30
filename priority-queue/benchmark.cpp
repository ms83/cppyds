#include<iostream>
#include<chrono>
#include<queue>
using namespace std;

const int N = 1<<20;

int main()
{
    auto start = std::chrono::system_clock::now();
    vector<int> v{2,1,1,5,4};
    priority_queue<int> h(v.begin(), v.end());

    for(int i=0; i<N; ++i) {
        h.push(i);
    }

    for(int i=0; i<N; ++i) {
        h.pop();
    }

    auto end = std::chrono::system_clock::now();
    auto elapsed = end - start;
    std::cout << std::chrono::duration<double>(elapsed).count();
}

// 1.90 secs (-O0 optimization)
// 0.10 secs (-O2 optimization)
