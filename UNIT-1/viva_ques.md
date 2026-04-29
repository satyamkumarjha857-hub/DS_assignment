
#  🎯 VIVA QUESTIONS 


## ➡️ StackADT

## 1. What is an ADT?

**Answer** ADT (Abstract Data Type) is a mathematical model that defines data + operations on that data without specifying implementation details.
**Stack ADT defines:**
**DATA:** Collection of items
**OPERATIONS:** push(), pop(), peek(), isEmpty(), size()


## 2. Why push/pop can be O(1)?

**Answer** Push and pop operations have O(1) time complexity because they work only at the array's END using direct index access, requiring a constant number of steps (2-3 operations) regardless of stack size.


## 3. One real-world use of stack?

**Answer** Browser back button uses a stack for navigation history. Every page you visit gets pushed onto the stack, and the back button pops the most recent one.


## ➡️ Complexity Drill

## 1. Big-O vs Big-Theta difference?

**Answer**  **Big-O vs Big-Theta**
- **Big-O**: Upper bound only (≤ some function)  
- **Big-Theta**: Tight bound (= exactly that growth rate)  
- **O(f(n))**: "Never worse than f(n)"  
- **Θ(f(n))**: "Always exactly f(n)"  
- **Merge sort**: O(n log n) = worst-case guarantee  
- **Merge sort**: Θ(n log n) = exact runtime  
- **Stack push**: Θ(1) = exactly 2-3 steps always  
- **If Θ proven → O automatically true**  
- **O proven → Θ not guaranteed**  
- **Ex: O(n²) might actually be n runtime**

## 2. What does worst-case represent?

**Answer**  **Worst-case represents the MAXIMUM time/space an algorithm takes for ANY possible input.**
- **Definition**: Slowest possible execution across all input scenarios  
- **Purpose**: Guarantees "even in worst input, won't exceed this"  
- **Linear Search Example**:  
  - Best: item at position 1 → 1 comparison  
  - Worst: item at end OR absent → n comparisons  
  - **Worst-case = O(n)**  
- **Stack Push Example**:  
  - Every case identical → 2 operations  
  - **Worst-case = Θ(1)** (same as best)  
- **Why Care?**:  
  - **Safety guarantee** for production code  
  - "My app won't freeze even on bad data"  
- **Real Meaning**:  
  - **O(n)** worst-case = "might need to check all n items"  
  - Protects against adversarial/malicious inputs

## 3. Why complexity matters in real systems?

**Answer**  Algorithm complexity determines if your system scales or crashes under real load.
**Real-World Impact**
1M users → O(n²) = 10¹² operations = freeze
1M users → O(n log n) = 2×10⁷ operations = smooth
Google search: O(n²) would take years per query
**Instagram feed:** Bad complexity = loading forever


## ➡️ Recursive Factorial

## 1. What is recursion depth?

**Answer**  Recursion depth is the maximum number of recursive calls stacked before hitting base case.
**Definition:** Count of nested function calls on call stack
**Example:** factorial(5) → 5→4→3→2→1→base = depth 5
**Stack usage:** Each call adds 1 stack frame
**Limit:** Python default = 1000 calls 
**Problem:** Depth > limit → Stack Overflow crash
**Stack Push Connection:** Each recursive call = stack.push(context)

## 2. Why recursion uses stack memory?

**Answer** Recursion uses stack memory because each recursive call creates a new function frame pushed onto the call stack.
**Function call =** stack frame creation (parameters, return address, local vars)
**Recursive call =** nested stack frames (each call pushes new frame)
**factorial(5) →** 5 stack frames created before base case
stack.pop() each return removes top frame
**LIFO perfect match:** Last called function finishes first
**No recursion →** no deep stack usage (just normal function calls)
**Stack overflow =** too many nested frames (recursion depth limit hit)

## 3. When iteration is better than recursion?

**Answer**  Iteration beats recursion when performance + safety matters most.
**Large inputs:** No stack overflow risk (recursion limited ~1000 calls)
**Performance critical:** No function call overhead (10-50x faster loops)
**Memory tight:** O(1) space vs O(n) stack frames
**Simple loops:** Factorial, sum, array processing
**Production code:** Guaranteed no crashes under heavy load


## ➡️ Fibonacci

## 1. Why naive Fibonacci is slow?

**Answer** Naive Fibonacci is slow due to massive redundant calculations creating exponential time complexity.

## 2. Memoization relates to DP ?

**Answer**  Yes, memoization is a core technique of Dynamic Programming (top-down approach).
**Memoization:** Cache recursive results to avoid recomputation
**DP:** Solve subproblems once, store results, build solution
**Memoization =** Recursive DP (top-down with cache)
**Tabulation =** Iterative DP (bottom-up with table)
**Both solve:** Same subproblem → same answer (overlapping subproblems)

## 3. Space impact of memoization?

**Answer** Memoization trades time for space - adds O(n) memory overhead.
**Cache storage:** O(n) array/dict for all subproblem results
**Recursion stack:** O(n) frames (depth = n for Fibonacci)
**Total:** O(n) extra space beyond input

## ➡️ Tower Of Hanoi

## 1. Why moves are 2n-1?
**Answer**

## 2. What is recursion tree idea?

**Answer**  Tower of Hanoi needs exactly 2^n - 1 moves minimum.
To move n disks from A→C using B:
1. Move n-1 disks A→B: T(n-1) moves
2. Move largest disk A→C: 1 move  
3. Move n-1 disks B→C: T(n-1) moves
T(n) = 2*T(n-1) + 1
T(1) = 1
**Solution:** T(n) = 2^n - 1 


## 3. Practical risk of exponential algorithms?

**Answer**  Exponential algorithms crash real systems beyond tiny inputs.
**Practical Risks**
**n=30:** 1 billion operations = 10+ seconds (maybe OK)
**n=40:** 1 trillion operations = 10+ DAYS (dead)
**n=50:** 1 quadrillion = 30+ YEARS (impossible)
**Memory:** 2^n RAM → n=30 = 8GB, n=40 = 1TB+


## ➡️ Recursive Binary Search

## 1. Why sorted data is required?

**Answer**  Sorted data enables log n algorithms instead of linear n searches.
**Binary Search:** Unsorted = O(n), Sorted = O(log n)
**Merge operations:** Requires order to combine efficiently
**Kth smallest:** Direct index access O(1) after sort
**Duplicate removal:** Adjacent equals after sorting

## 2. Best/avg/worst case?

**Answer**  Best/Avg/Worst case measures algorithm performance across input scenarios.
**Best Case:** Minimum operations (ideal input)
**Linear search:** target at index 0 = 1 comparison
**Worst Case:** Maximum operations (bad input)
**Linear search:** target absent = n comparisons
**Average Case:** Expected operations (random input)
**Linear search:** target anywhere = n/2 comparisons avg

## 3. Divide & Conquer meaning?

**Answer** Divide & Conquer breaks big problems into smaller identical problems recursively.
**3-Step Process**
**Divide:** Split problem into 2+ subproblems (usually half size)
**Conquer:** Solve subproblems recursively (or directly if small)
**Combine:** Merge subproblem solutions into original answer


