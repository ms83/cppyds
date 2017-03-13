
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


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
from collections import deque
dq = deque()
</pre>
</td>
<td valign="top">
<pre lang="cpp">
#include<deque>
deque<int> dq;
</pre>
</td>
</tr>
</table>
    

### deque: initialize with values


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
dq = deque([0, 1 ,2, 3, 4])
</pre>
</td>
<td valign="top">
<pre lang="cpp">
deque<int> dq {0,1,2,3,4};
</pre>
</td>
</tr>
</table>
    

### deque: access


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
dq[0]
dq[-1]
dq[2] # raise IndexError if index of of range
</pre>
</td>
<td valign="top">
<pre lang="cpp">
dq.front();
dq.back();
dq[2];    // undefined behaviour if index out of range
dq.at(2); // throw std::out_of_range if index out of range
</pre>
</td>
</tr>
</table>
    

### deque: insert


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
dq.append(10)
dq.appendleft(20)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
dq.push_back(10)
dq.push_front(20)
</pre>
</td>
</tr>
</table>
    

### deque: remove


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
dq.pop()
dq.popleft()
</pre>
</td>
<td valign="top">
<pre lang="cpp">
dq.pop_front()
dq.pop_back()
</pre>
</td>
</tr>
</table>
    

### deque: benchmark


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
from timeit import timeit
from collections import deque

def test():
    N = 1<<26

    dq = deque()

    for i in range(0, N):
        dq.append(i)
        dq.appendleft(i)

    for i in range(0, N):
        dq.pop()
        dq.popleft()

print(timeit("test()", number=1, setup="from __main__ import test"))

# 16.58 secs (python 2.7)
# 19.25 secs (python 3.5)
#  7.57 secs (pypy, 2.7)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
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
</pre>
</td>
</tr>
</table>
    

[&uarr;top](#c-for-python-programmers)



## Dynamic Array

[declaration and definition](#dynamic-array-declaration-and-definition)

[initialize with values](#dynamic-array-initialize-with-values)

[access](#dynamic-array-access)

[insert](#dynamic-array-insert)

[remove](#dynamic-array-remove)

[benchmark](#dynamic-array-benchmark)

### dynamic-array: declaration and definition


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
l = []
</pre>
</td>
<td valign="top">
<pre lang="cpp">
#include<vector>
vector<int> v;
</pre>
</td>
</tr>
</table>
    

### dynamic-array: initialize with values


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
l = [1,3,5,7,9]
</pre>
</td>
<td valign="top">
<pre lang="cpp">
vector<int> v{1,3,5,7,9};
</pre>
</td>
</tr>
</table>
    

### dynamic-array: access


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
l[0]  # first
l[-1] # last
l[3]  # random access O(1)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
v[0]          // first
v[v.size()-1] // last
v[3]          // random access O(1)
</pre>
</td>
</tr>
</table>
    

### dynamic-array: insert


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
l.append(11) # (!) possible full reallocation
</pre>
</td>
<td valign="top">
<pre lang="cpp">
v.push_back(11) // (!) possible full reallocation
</pre>
</td>
</tr>
</table>
    

### dynamic-array: remove


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
l.pop()  # remove last; O(1)
l.pop(0) # remove first; prefer deque
</pre>
</td>
<td valign="top">
<pre lang="cpp">
v.pop_back();       // remove last; O(1)
v.erase(v.begin()); // remove first; prefer deque or list
</pre>
</td>
</tr>
</table>
    

### dynamic-array: benchmark


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
import sys
from timeit import timeit

def test():
    N = 1<<26

    l = []

    if sys.version_info >= (3, ):
        for i in range(0, N):
            l.append(i)
    else:
        for i in xrange(0, N):
            l.append(i)

    while l:
        l.pop()

print(timeit("test()",
             number=1,
             setup="from __main__ import test"))

# 11.59 secs (python 2.7)
# 13.03 secs (python 3.5)
#  1.81 secs (pypy, 2.7)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
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
</pre>
</td>
</tr>
</table>
    

[&uarr;top](#c-for-python-programmers)



## Map

[declaration and definition](#map-declaration-and-definition)

[initialize with values](#map-initialize-with-values)

[access](#map-access)

[insert](#map-insert)

[remove](#map-remove)

[benchmark](#map-benchmark)

### map: declaration and definition


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
d = {}
</pre>
</td>
<td valign="top">
<pre lang="cpp">
#include<map>
map<string, int> m;
</pre>
</td>
</tr>
</table>
    

### map: initialize with values


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
d = {'c++': 10, 'python': 12, 'java': 5}
</pre>
</td>
<td valign="top">
<pre lang="cpp">
map<string, int> m { {"c++", 10}, {"python", 12}, {"java", 5} };
</pre>
</td>
</tr>
</table>
    

### map: access


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
d['erlang'] # raise KeyError for non-existing key
</pre>
</td>
<td valign="top">
<pre lang="cpp">
m["erlang"] // returns default constructed element for non-existing key

m.at("erlang") // throws std::out_of_range for non-existing key
</pre>
</td>
</tr>
</table>
    

### map: insert


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
d['rust'] = 50
</pre>
</td>
<td valign="top">
<pre lang="cpp">
m["rust"] = 50;
</pre>
</td>
</tr>
</table>
    

### map: remove


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
del d['scala'] # raise KeyError for non-existing key
</pre>
</td>
<td valign="top">
<pre lang="cpp">
m.erase("scala"); // dunno for non-existing key
</pre>
</td>
</tr>
</table>
    

### map: benchmark


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
from timeit import timeit

def test():
    N = 1<<20

    total = 0
    d = {}

    for i in range(0, N):
        d[i] = i

    for i in range(0, N):
        total += d[i]

    for i in range(0, N):
        del d[i]

print(timeit("test()",
             number=1,
             setup="from __main__ import test"))

# 0.25 secs (python 2.7)
# 0.27 secs (python 3.5)
# 0.15 secs (pypy, 2.7)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
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
</pre>
</td>
</tr>
</table>
    

[&uarr;top](#c-for-python-programmers)



## Priority Queue

[declaration and definition](#priority-queue-declaration-and-definition)

[initialize with values](#priority-queue-initialize-with-values)

[access](#priority-queue-access)

[insert](#priority-queue-insert)

[remove](#priority-queue-remove)

[benchmark](#priority-queue-benchmark)

### priority-queue: declaration and definition


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
import heapq
h = []

# or slower but with better interface
from Queue import PriorityQueue
h = PriorityQueue()
</pre>
</td>
<td valign="top">
<pre lang="cpp">
#include<queue>
priority_queue<int> h;
</pre>
</td>
</tr>
</table>
    

### priority-queue: initialize with values


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
h = [2,1,1,5,4]
heapq.heapify(h)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
vector<int> v{2,1,1,5,4};
priority_queue<int> h(v.begin(), v.end());
</pre>
</td>
</tr>
</table>
    

### priority-queue: access


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
h[0] # first element. unable to access top element using heapq
</pre>
</td>
<td valign="top">
<pre lang="cpp">
h.top() // top element
</pre>
</td>
</tr>
</table>
    

### priority-queue: insert


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
heapq.heappush(h, 10)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
h.push(10)
</pre>
</td>
</tr>
</table>
    

### priority-queue: remove


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
heapq.heappop(h)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
h.pop()
</pre>
</td>
</tr>
</table>
    

### priority-queue: benchmark


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
from timeit import timeit
import heapq # faster than Queue.PriorityQueue

def test():
    N = 1<<20

    h = []

    for i in range(0, N):
        heapq.heappush(h, i)

    for i in range(0, N):
        heapq.heappop(h)


print(timeit("test()",
             number=1,
             setup="from __main__ import test"))

# 5.38 secs (python 2.7)
# 0.75 secs (python 3.5)
# 0.37 secs (pypy, 2.7)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
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
</pre>
</td>
</tr>
</table>
    

[&uarr;top](#c-for-python-programmers)



## Queue

[declaration and definition](#queue-declaration-and-definition)

[initialize with values](#queue-initialize-with-values)

[access](#queue-access)

[insert](#queue-insert)

[remove](#queue-remove)

[benchmark](#queue-benchmark)

### queue: declaration and definition


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
from Queue import Queue
q = Queue()

# or simply list
q = []
</pre>
</td>
<td valign="top">
<pre lang="cpp">
#include<queue>
queue<int> q;
</pre>
</td>
</tr>
</table>
    

### queue: initialize with values


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
# not possible to initialize Queue with values
</pre>
</td>
<td valign="top">
<pre lang="cpp">
queue<int> q {0,1,2,3,4};
</pre>
</td>
</tr>
</table>
    

### queue: access


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
q.get() # return and remove
</pre>
</td>
<td valign="top">
<pre lang="cpp">
q.front()
q.back()
</pre>
</td>
</tr>
</table>
    

### queue: insert


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
s.put(10)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
q.push(10)
</pre>
</td>
</tr>
</table>
    

### queue: remove


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
q.get()
q.pop(0) # if queue used as []
</pre>
</td>
<td valign="top">
<pre lang="cpp">
q.pop()
</pre>
</td>
</tr>
</table>
    

### queue: benchmark


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
import sys
from timeit import timeit

if sys.version_info >= (3,):
    from queue import Queue
else:
    from Queue import Queue

def test():
    N = 1<<20

    # 1) orders of magnitue faster than queue as []
    # 2) thread safe
    q = Queue()

    for i in range(0, N):
        q.put(i)

    for i in range(0, N):
        q.get()


print(timeit("test()",
             number=1,
             setup="from __main__ import test"))

# 3.13 secs (python 2.7)
# 5.09 secs (python 3.5)
# 0.22 secs (pypy, 2.7)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
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
</pre>
</td>
</tr>
</table>
    

[&uarr;top](#c-for-python-programmers)



## Set

[declaration and definition](#set-declaration-and-definition)

[initialize with values](#set-initialize-with-values)

[access](#set-access)

[insert](#set-insert)

[remove](#set-remove)

[benchmark](#set-benchmark)

### set: declaration and definition


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
s = set()
</pre>
</td>
<td valign="top">
<pre lang="cpp">
#include<set>
set<int> s;
</pre>
</td>
</tr>
</table>
    

### set: initialize with values


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
s = {0, 1 ,2, 3, 4}
</pre>
</td>
<td valign="top">
<pre lang="cpp">
set<int> s {0,1,2,3,4};
</pre>
</td>
</tr>
</table>
    

### set: access


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
if 10 in s:
    pass
</pre>
</td>
<td valign="top">
<pre lang="cpp">
if (s.find(10) != s.end()) {
}
</pre>
</td>
</tr>
</table>
    

### set: insert


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
s.add('b')
</pre>
</td>
<td valign="top">
<pre lang="cpp">
s.insert("b");
</pre>
</td>
</tr>
</table>
    

### set: remove


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
s.remove(25)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
s.erase(25)
</pre>
</td>
</tr>
</table>
    

### set: benchmark


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
from timeit import timeit

def test():
    N = 1<<20

    s = set()

    for i in range(0, N):
        s.add(i)

    for i in range(0, N):
        k = i in s

    for i in range(0, N):
        s.remove(i)

print(timeit("test()",
             number=1,
             setup="from __main__ import test"))

# 0.25 secs (python 2.7)
# 0.31 secs (python 3.5)
# 0.10 secs (pypy, 2.7)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
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
</pre>
</td>
</tr>
</table>
    

[&uarr;top](#c-for-python-programmers)



## Stack

[declaration and definition](#stack-declaration-and-definition)

[initialize with values](#stack-initialize-with-values)

[access](#stack-access)

[insert](#stack-insert)

[remove](#stack-remove)

[benchmark](#stack-benchmark)

### stack: declaration and definition


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
s = [] # simply list
</pre>
</td>
<td valign="top">
<pre lang="cpp">
#include<stack>
stack<int> s;
</pre>
</td>
</tr>
</table>
    

### stack: initialize with values


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
s = {0, 1 ,2, 3, 4}
</pre>
</td>
<td valign="top">
<pre lang="cpp">
stack<int> s {0,1,2,3,4};
</pre>
</td>
</tr>
</table>
    

### stack: access


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
s[-1]
</pre>
</td>
<td valign="top">
<pre lang="cpp">
s.top();
</pre>
</td>
</tr>
</table>
    

### stack: insert


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
s.append(10)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
s.push(10)
</pre>
</td>
</tr>
</table>
    

### stack: remove


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
s.pop()
</pre>
</td>
<td valign="top">
<pre lang="cpp">
s.pop()
</pre>
</td>
</tr>
</table>
    

### stack: benchmark


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
from timeit import timeit

def test():
    N = 1<<26

    s = []

    for i in range(0, N):
        s.append(i)

    for i in range(0, N):
        s.pop()

print(timeit("test()",
             number=1,
             setup="from __main__ import test"))

# 13.53 secs (python 2.7)
# 14.11 secs (python 2.7)
#  1.68 secs (pypy, 2.7)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
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
</pre>
</td>
</tr>
</table>
    

[&uarr;top](#c-for-python-programmers)
