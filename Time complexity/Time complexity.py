
# 🧠 The 30-Second Time Complexity Method (Google-Style)

When you see **any code**, do this **in order**:
---

## STEP 1️⃣ Ignore constants

```python
for i in range(5 * n):
```

➡️ Treat as `n`, not `5n`

---

## STEP 2️⃣ Find the *dominant* operation

Ask:

* What runs the **most times**?
* What grows **fastest** as `n` increases?

That term wins.

---

## STEP 3️⃣ Handle loops

| Pattern             | Complexity   |
| ------------------- | ------------ |
| One loop            | `O(n)`       |
| Nested loops        | multiply     |
| Loop halves/doubles | `O(log n)`   |
| Loop + log loop     | `O(n log n)` |

---

## STEP 4️⃣ Recursion rule of thumb

Ask:

* How many recursive calls?

* How deep?

> Use **Recurrence Relation** if needed

> `T(n) = aT(n/b) + f(n)`

---
# 🔥 Mock Interview (Answer Out Loud)

Try these **before reading answers**.
---

## Question 1

```python
def f(n):
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
```

### ✅ Answer

* Outer loop → `n`
* Inner loop doubles → `log n`

**Total:** `O(n log n)`

---

## Question 2

```python
def g(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            print(arr[i], arr[j])
```

### ✅ Answer

* Inner loop runs fewer times each iteration

* Still ≈ `n² / 2`

**Total:** `O(n²)`

---

## Question 3 (Google Favorite)

```python
def h(n):
    if n <= 1:
        return 1
    return h(n//2) + h(n//2)
```

### ✅ Answer

* Two recursive calls
* Depth: `log n`

**Total:** `O(n)`
(Important: NOT `O(2ⁿ)`!)

---

## Question 4 (Trick)

```python
def k(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
```

### ✅ Answer

`O(n + n)` → **`O(n)`**

---

## Question 5 (Real Interview Level)

```python
def m(n):
    i = 1
    while i <= n:
        j = 0
        while j <= i:
            j += 1
        i *= 2
```

### 🧠 Breakdown

* Outer loop → `log n`
* Inner loop → `i` (powers of 2)

Total work:
`1 + 2 + 4 + 8 + ... + n` = `2n`

### ✅ Answer

**`O(n)`**
