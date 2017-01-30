
# C++ vs. Python data structures

[Deque](#deque) &nbsp; [Dynamic Array](#dynamic-array) &nbsp; [Map](#map) &nbsp; [Priority Queue](#priority-queue) &nbsp; [Queue](#queue) &nbsp; [Set](#set) &nbsp; [Stack](#stack)



## Deque

[declaration and definition](#deque-declaration-and-definition)

[initialize with values](#deque-initialize-with-values)

[access](#deque-access)

[insert](#deque-insert)

[remove](#deque-remove)

[benchmark](#deque-benchmark)

### deque: declaration and definition
```python
from collections import deque
dq = deque()
```
```cpp
#include<deque>
deque<int> dq;
```

### deque: initialize with values
```python
dq = deque([0, 1 ,2, 3, 4])
```
```cpp
deque<int> dq {0,1,2,3,4};
```

### deque: access
```python
dq[0]
dq[-1]
dq[2] # raise IndexError if index of of range
```
```cpp
dq.front();
dq.back();
dq[2];    // undefined behaviour if index out of range
dq.at(2); // throw std::out_of_range if index out of range
```

### deque: insert
```python
dq.append(10)
dq.appendleft(20)
```
```cpp
dq.push_back(10)
dq.push_front(20)
```

### deque: remove
```python
dq.pop()
dq.popleft()
```
```cpp
dq.pop_front()
dq.pop_back()
```

### deque: benchmark
```python
from timeit import timeit
from collections import deque

def test():
    N = 1<<26

    dq = deque()

    for i in xrange(0, N):
        dq.append(i)
        dq.appendleft(i)

    for i in xrange(0, N):
        dq.pop()
        dq.popleft()

print(timeit("test()", number=1, setup="from __main__ import test"))

# 16.58 secs (python 2.7)
```
```cpp
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
```



## Dynamic Array

[declaration and definition](#dynamic-array-declaration-and-definition)

[initialize with values](#dynamic-array-initialize-with-values)

[access](#dynamic-array-access)

[insert](#dynamic-array-insert)

[remove](#dynamic-array-remove)

[benchmark](#dynamic-array-benchmark)

### dynamic-array: declaration and definition
```python
l = []
```
```cpp
#include<vector>
vector<int> v;
```

### dynamic-array: initialize with values
```python
l = [1,3,5,7,9]
```
```cpp
vector<int> v{1,3,5,7,9};
```

### dynamic-array: access
```python
l[0]  # first
l[-1] # last
l[3]  # random access O(1)
```
```cpp
v[0]          // first
v[v.size()-1] // last
v[3]          // random access O(1)
```

### dynamic-array: insert
```python
l.append(11) # (!) possible full reallocation
```
```cpp
v.push_back(11) // (!) possible full reallocation
```

### dynamic-array: remove
```python
l.pop()  # remove last; O(1)
l.pop(0) # remove first; prefer deque
```
```cpp
v.pop_back();       // remove last; O(1)
v.erase(v.begin()); // remove first; prefer deque or list
```

### dynamic-array: benchmark
```python
from timeit import timeit

def test():
    N = 1<<26

    l = []

    for i in xrange(0, N):
        l.append(i)

    while l:
        l.pop()

print(timeit("test()", number=1, setup="from __main__ import test"))

# 11.59 secs (python 2.7)
```
```cpp
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
```



## Map

[declaration and definition](#map-declaration-and-definition)

[initialize with values](#map-initialize-with-values)

[access](#map-access)

[insert](#map-insert)

[remove](#map-remove)

[benchmark](#map-benchmark)

### map: declaration and definition
```python
d = {}
```
```cpp
#include<map>
map<string, int> m;
```

### map: initialize with values
```python
d = {'c++': 10, 'python': 12, 'java': 5}
```
```cpp
map<string, int> m { {"c++", 10}, {"python", 12}, {"java", 5} };
```

### map: access
```python
d['erlang'] # raise KeyError for non-existing key
```
```cpp
m["erlang"] // returns default constructed element for non-existing key

m.at("erlang") // throws std::out_of_range for non-existing key
```

### map: insert
```python
d['rust'] = 50
```
```cpp
m["rust"] = 50;
```

### map: remove
```python
del d['scala'] # raise KeyError for non-existing key
```
```cpp
m.erase("scala"); // dunno for non-existing key
```

### map: benchmark
```python
from timeit import timeit

def test():
    N = 1<<20

    total = 0
    d = {}

    for i in xrange(0, N):
        d[i] = i

    for i in xrange(0, N):
        total += d[i]

    for i in xrange(0, N):
        del d[i]

    print total

print(timeit("test()", number=1, setup="from __main__ import test"))

# 0.25 secs (python 2.7)
```
```cpp
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
```



## Priority Queue

[declaration and definition](#priority-queue-declaration-and-definition)

[initialize with values](#priority-queue-initialize-with-values)

[access](#priority-queue-access)

[insert](#priority-queue-insert)

[remove](#priority-queue-remove)

[benchmark](#priority-queue-benchmark)

### priority-queue: declaration and definition
```python
import heapq
h = []

# or slower but with better interface
from Queue import PriorityQueue
h = PriorityQueue()
```
```cpp
#include<queue>
priority_queue<int> h;
```

### priority-queue: initialize with values
```python
h = [2,1,1,5,4]
heapq.heapify(h)
```
```cpp
vector<int> v{2,1,1,5,4};
priority_queue<int> h(v.begin(), v.end());
```

### priority-queue: access
```python
h[0] # first element. unable to access top element using heapq
```
```cpp
h.top() // top element
```

### priority-queue: insert
```python
heapq.heappush(h, 10)
```
```cpp
h.push(10)
```

### priority-queue: remove
```python
heapq.heappop(h)
```
```cpp
h.pop()
```

### priority-queue: benchmark
```python
from timeit import timeit
import heapq # faster than Queue.PriorityQueue

h = [4,5,3,10,6]
heapq.heapify(h)
print h
print h[0]
print h[-1]
x

def test():
    N = 1<<20

    h = []

    for i in xrange(0, N):
        heapq.heappush(h, i)

    for i in xrange(0, N):
        heapq.heappop(h)


print(timeit("test()", number=1, setup="from __main__ import test"))

# 5.38 secs (python 2.7)
```
```cpp
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
```



## Queue

[declaration and definition](#queue-declaration-and-definition)

[initialize with values](#queue-initialize-with-values)

[access](#queue-access)

[insert](#queue-insert)

[remove](#queue-remove)

[benchmark](#queue-benchmark)

### queue: declaration and definition
```python
from Queue import Queue
q = Queue()

# or simply list
q = []
```
```cpp
#include<queue>
queue<int> q;
```

### queue: initialize with values
```python
# not possible to initialize Queue with values
```
```cpp
queue<int> q {0,1,2,3,4};
```

### queue: access
```python
q.get() # return and remove
```
```cpp
q.front()
q.back()
```

### queue: insert
```python
s.put(10)
```
```cpp
q.push(10)
```

### queue: remove
```python
q.get()
q.pop(0) # if queue used as []
```
```cpp
q.pop()
```

### queue: benchmark
```python
from timeit import timeit
from Queue import Queue

def test():
    N = 1<<20

    # 1) orders of magnitue faster that queue as []
    # 2) thread safe
    q = Queue()

    for i in xrange(0, N):
        q.put(i)

    for i in xrange(0, N):
        q.get()


print(timeit("test()", number=1, setup="from __main__ import test"))

# 3.13 secs (python 2.7)
```
```cpp
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
```



## Set

[declaration and definition](#set-declaration-and-definition)

[initialize with values](#set-initialize-with-values)

[access](#set-access)

[insert](#set-insert)

[remove](#set-remove)

[benchmark](#set-benchmark)

### set: declaration and definition
```python
s = set()
```
```cpp
#include<set>
set<int> s;
```

### set: initialize with values
```python
s = {0, 1 ,2, 3, 4}
```
```cpp
set<int> s {0,1,2,3,4};
```

### set: access
```python
if 10 in s:
    pass
```
```cpp
if (s.find(10) != s.end()) {
}
```

### set: insert
```python
s.add('b')
```
```cpp
s.insert("b");
```

### set: remove
```python
s.remove(25)
```
```cpp
s.erase(25)
```

### set: benchmark
```python
from timeit import timeit

def test():
    N = 1<<20

    s = set()

    for i in xrange(0, N):
        s.add(i)

    for i in xrange(0, N):
        k = i in s

    for i in xrange(0, N):
        s.remove(i)

print(timeit("test()", number=1, setup="from __main__ import test"))

# 0.25 secs (python 2.7)
```
```cpp
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
```



## Stack

[declaration and definition](#stack-declaration-and-definition)

[initialize with values](#stack-initialize-with-values)

[access](#stack-access)

[insert](#stack-insert)

[remove](#stack-remove)

[benchmark](#stack-benchmark)

### stack: declaration and definition
```python
s = [] # simply list
```
```cpp
#include<stack>
stack<int> s;
```

### stack: initialize with values
```python
s = {0, 1 ,2, 3, 4}
```
```cpp
stack<int> s {0,1,2,3,4};
```

### stack: access
```python
s[-1]
```
```cpp
s.top();
```

### stack: insert
```python
s.append(10)
```
```cpp
s.push(10)
```

### stack: remove
```python
s.pop()
```
```cpp
s.pop()
```

### stack: benchmark
```python
from timeit import timeit

def test():
    N = 1<<26

    s = []

    for i in xrange(0, N):
        s.append(i)

    for i in xrange(0, N):
        s.pop()

print(timeit("test()", number=1, setup="from __main__ import test"))

# 11.53 secs (python 2.7)
```
```cpp
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
```
