# 🐍 BỘ BÀI TẬP CODE PYTHON — Cho dân Java/C++ luyện tay

> Bám sát **Module B** của đề thi AICB (xử lý văn bản · công thức→Python/NumPy · broadcasting · metrics).  
> Mỗi nhóm có hộp **🔁 Java/C++ → Python** chỉ ra chỗ tư duy khác nhau.  
> **Cách dùng:** đọc đề → tự code → bung phần *Lời giải* để đối chiếu. Tất cả lời giải đã chạy kiểm tra.

---

## PHẦN 0 — Cheat-sheet: Java/C++ nói thế này, Python nói thế kia

| Việc cần làm | Java / C++ | Python |
|---|---|---|
| Khai báo biến | `int x = 5;` | `x = 5` (không cần kiểu, không `;`) |
| Khối lệnh | `{ ... }` | **thụt lề** (4 space), kết thúc dòng `if` bằng `:` |
| Vòng lặp đếm | `for(int i=0;i<n;i++)` | `for i in range(n):` |
| Duyệt mảng | `for(int i=0;i<a.length;i++) a[i]` | `for x in a:` (lấy thẳng phần tử) |
| Duyệt kèm chỉ số | `for(int i=...) a[i]` | `for i, x in enumerate(a):` |
| Duyệt 2 mảng song song | `for(i...) a[i], b[i]` | `for x, y in zip(a, b):` |
| Độ dài | `a.length` / `a.size()` | `len(a)` |
| Tăng biến | `i++` | `i += 1` (Python **không có** `++`) |
| Chia | `5/2 → 2` (int), `5.0/2` | `5/2 → 2.5` (luôn float), `5//2 → 2` (chia nguyên) |
| Lũy thừa | `Math.pow(x,2)` | `x ** 2` |
| Logic | `&&  ||  !` | `and  or  not` |
| Hằng | `true / false / null` | `True / False / None` |
| Đổi chỗ 2 biến | `tmp=a; a=b; b=tmp;` | `a, b = b, a` |
| HashMap | `map.get(k)` | `d[k]` hoặc `d.get(k, default)` |
| Thêm vào list | `list.add(x)` | `list.append(x)` |
| In có định dạng | `printf("%d", x)` | `print(f"{x}")` (f-string) |
| Phần tử cuối | `a[a.length-1]` | `a[-1]` |
| Cắt mảng con | vòng lặp/`subList` | `a[1:4]`, đảo ngược `a[::-1]` |

**3 cái bẫy hay sập nhất:**
1. **Thụt lề là cú pháp**, sai lề = lỗi (không phải làm đẹp như Java).
2. **List comprehension** thay cho vòng `for` + `append`: `[x*2 for x in a]`.
3. **Không khai báo kiểu** → đọc kỹ dữ liệu vào là `int`, `float`, hay `str`.

---

## PHẦN 1 — Làm quen cú pháp (warm-up)

### Bài 1.1 — FizzBuzz
In số từ 1 đến `n`. Chia hết 3 → in `"Fizz"`, chia hết 5 → `"Buzz"`, cả hai → `"FizzBuzz"`.

<details><summary>💡 Lời giải</summary>

```python
def fizzbuzz(n):
    for i in range(1, n + 1):          # range(1, n+1) = 1..n (n+1 KHÔNG lấy)
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(15)
```
> 🔁 Không có `else if`, dùng `elif`. Không có `switch`, dùng chuỗi `if/elif`.
</details>

### Bài 1.2 — Tổng & trung bình của list
Cho `nums = [4, 8, 15, 16, 23, 42]`, tính tổng và trung bình.

<details><summary>💡 Lời giải</summary>

```python
nums = [4, 8, 15, 16, 23, 42]
total = sum(nums)                 # không cần tự viết vòng lặp cộng dồn
avg = total / len(nums)
print(f"Tổng = {total}, TB = {avg:.2f}")   # :.2f = làm tròn 2 số lẻ
```
> 🔁 Java phải `for` cộng dồn; Python có sẵn `sum()`, `len()`, `max()`, `min()`.
</details>

### Bài 1.3 — Tìm max và vị trí của nó
Cho list, in giá trị lớn nhất và chỉ số của nó.

<details><summary>💡 Lời giải</summary>

```python
a = [3, 9, 2, 9, 5]
mx = max(a)
idx = a.index(mx)                 # vị trí xuất hiện đầu tiên
print(f"max={mx} tại index={idx}")

# Cách "Python" hơn, lấy chỉ số của max trực tiếp:
idx2 = max(range(len(a)), key=lambda i: a[i])
print(idx2)
```
</details>

### Bài 1.4 — Đảo ngược chuỗi & kiểm tra palindrome
Viết hàm `is_palindrome(s)` trả về `True/False`.

<details><summary>💡 Lời giải</summary>

```python
def is_palindrome(s):
    return s == s[::-1]           # s[::-1] = đảo ngược chuỗi, "thần chú" của Python

print(is_palindrome("radar"))    # True
print(is_palindrome("python"))   # False
```
> 🔁 Java cần `StringBuilder(s).reverse()`. Python: `s[::-1]`.
</details>

### Bài 1.5 — Fibonacci không cần biến tạm
In 10 số Fibonacci đầu tiên.

<details><summary>💡 Lời giải</summary>

```python
a, b = 0, 1
for _ in range(10):              # _ = biến "vứt đi", không dùng tới
    print(a, end=" ")
    a, b = b, a + b              # gán đồng thời, không cần tmp
```
> 🔁 `a, b = b, a + b` làm 1 phát; vế phải tính xong hết rồi mới gán.
</details>

---

## PHẦN 2 — Xử lý văn bản (đúng kiểu Câu Code 1 của đề)

### Bài 2.1 — Đếm tần suất ký tự
Đếm số lần xuất hiện mỗi ký tự trong `"banana"` (bỏ qua khoảng trắng).

<details><summary>💡 Lời giải</summary>

```python
def char_count(s):
    freq = {}
    for ch in s:
        if ch == " ":
            continue
        freq[ch] = freq.get(ch, 0) + 1   # get(key, default) tránh KeyError
    return freq

print(char_count("banana"))   # {'b': 1, 'a': 3, 'n': 2}
```
> 🔁 Java: `map.put(c, map.getOrDefault(c, 0) + 1)`. Python: `d.get(c, 0) + 1`.
</details>

### Bài 2.2 — Đếm tần suất từ + top-K *(sát đề)*
Làm sạch chuỗi (chữ thường, bỏ dấu câu), tách từ, trả về 2 từ xuất hiện nhiều nhất.

```python
raw = "The cat sat on the mat. The CAT ran!"
```

<details><summary>💡 Lời giải</summary>

```python
import re
from collections import Counter

def top_words(text, k=2):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)   # bỏ mọi thứ KHÔNG phải chữ/khoảng trắng
    words = text.split()                  # tách theo khoảng trắng
    return Counter(words).most_common(k)

raw = "The cat sat on the mat. The CAT ran!"
print(top_words(raw))    # [('the', 3), ('cat', 2)]
```
> 🔁 `Counter` thay cho việc tự dựng HashMap đếm. `.most_common(k)` trả top-k luôn.
</details>

### Bài 2.3 — Loại bỏ stopwords
Bỏ các từ trong tập stopwords khỏi câu.

```python
stopwords = {"the", "is", "a", "on", "of"}
sentence = "the model is a transformer on top of attention"
```

<details><summary>💡 Lời giải</summary>

```python
stopwords = {"the", "is", "a", "on", "of"}      # set: kiểm tra "in" cực nhanh
sentence = "the model is a transformer on top of attention"

result = [w for w in sentence.split() if w not in stopwords]
print(" ".join(result))   # model transformer top attention
```
> 🔁 Dùng `set` (như `HashSet`) cho `in`. List comprehension `[... for ... if ...]` thay vòng lọc.
</details>

### Bài 2.4 — Đảo thứ tự các từ
`"hello world foo"` → `"foo world hello"`.

<details><summary>💡 Lời giải</summary>

```python
def reverse_words(s):
    return " ".join(s.split()[::-1])

print(reverse_words("hello world foo"))   # foo world hello
```
> 🔁 `split()` → list các từ, `[::-1]` đảo list, `" ".join(...)` ghép lại bằng dấu cách.
</details>

### Bài 2.5 — Sinh bi-gram (cặp 2 từ liền nhau)
`"the cat sat on the mat"` → `[('the','cat'), ('cat','sat'), ...]`.

<details><summary>💡 Lời giải</summary>

```python
def bigrams(text):
    w = text.split()
    return list(zip(w, w[1:]))    # ghép phần tử i với i+1

print(bigrams("the cat sat on the mat"))
# [('the','cat'), ('cat','sat'), ('sat','on'), ('on','the'), ('the','mat')]
```
> 🔁 Mẹo kinh điển: `zip(w, w[1:])` ghép mỗi phần tử với phần tử kế tiếp. Khỏi viết vòng lặp index.
</details>

---

## PHẦN 3 — Công thức toán → Python / NumPy (đúng kiểu Câu Code 2 của đề)

### Bài 3.1 — Sigmoid
$\sigma(x) = \dfrac{1}{1 + e^{-x}}$. Viết bản Python thuần và bản NumPy.

<details><summary>💡 Lời giải</summary>

```python
import math
import numpy as np

def sigmoid_pure(x):
    return 1 / (1 + math.exp(-x))          # 1 số

def sigmoid_np(x):
    return 1 / (1 + np.exp(-np.array(x)))  # áp lên cả mảng

print(round(sigmoid_pure(0), 4))           # 0.5
print(np.round(sigmoid_np([-1, 0, 1]), 4)) # [0.2689 0.5 0.7311]
```
> 🔁 `math.exp` cho 1 số; `np.exp` cho cả mảng (vector hóa, không cần vòng lặp).
</details>

### Bài 3.2 — ReLU và Leaky ReLU
$\text{ReLU}(x)=\max(0,x)$; $\text{LeakyReLU}(x)=x$ nếu $x>0$, ngược lại $0.01x$.

<details><summary>💡 Lời giải</summary>

```python
import numpy as np

def relu(x):
    return np.maximum(0, np.array(x))

def leaky_relu(x, alpha=0.01):
    x = np.array(x, dtype=float)
    return np.where(x > 0, x, alpha * x)   # where(điều kiện, lấy nếu đúng, lấy nếu sai)

print(relu([-2, -1, 0, 3]))          # [0 0 0 3]
print(leaky_relu([-2, 0, 3]))        # [-0.02  0.    3.  ]
```
> 🔁 `np.where(cond, a, b)` = toán tử 3 ngôi áp cho cả mảng (giống `cond ? a : b` nhưng vector).
</details>

### Bài 3.3 — Softmax (chú ý ổn định số học)
$\text{softmax}(x_i)=\dfrac{e^{x_i}}{\sum_j e^{x_j}}$. Trừ max trước khi mũ để tránh tràn số.

<details><summary>💡 Lời giải</summary>

```python
import numpy as np

def softmax(x):
    x = np.array(x, dtype=float)
    e = np.exp(x - np.max(x))    # trừ max: kết quả KHÔNG đổi, tránh overflow
    return e / e.sum()

print(np.round(softmax([2.0, 1.0, 0.1]), 4))   # [0.659  0.2424 0.0986]
print(round(float(softmax([2, 1, 0.1]).sum()), 4))  # 1.0 (tổng xác suất = 1)
```
> ⚠️ Bẫy phỏng vấn: quên trừ `max` → `exp` của số lớn gây tràn. Luôn trừ max.
</details>

### Bài 3.4 — MAE và RMSE
$\text{MAE}=\frac{1}{n}\sum|y_i-\hat{y}_i|$, $\text{RMSE}=\sqrt{\frac{1}{n}\sum(y_i-\hat{y}_i)^2}$.

<details><summary>💡 Lời giải</summary>

```python
import numpy as np

def mae(y, yhat):
    y, yhat = np.array(y), np.array(yhat)
    return np.mean(np.abs(y - yhat))

def rmse(y, yhat):
    y, yhat = np.array(y), np.array(yhat)
    return np.sqrt(np.mean((y - yhat) ** 2))

y      = [3, -0.5, 2, 7]
yhat   = [2.5, 0.0, 2, 8]
print(round(mae(y, yhat), 4))    # 0.5
print(round(rmse(y, yhat), 4))   # 0.6124
```
</details>

### Bài 3.5 — Binary Cross-Entropy (Log Loss)
$\text{BCE}=-\frac{1}{n}\sum\big[y_i\log(p_i)+(1-y_i)\log(1-p_i)\big]$. Nhớ chặn (clip) `p` để tránh `log(0)`.

<details><summary>💡 Lời giải</summary>

```python
import math

def bce(y_true, y_pred, eps=1e-12):
    total = 0.0
    for t, p in zip(y_true, y_pred):
        p = min(max(p, eps), 1 - eps)      # clip về [eps, 1-eps]
        total += -(t * math.log(p) + (1 - t) * math.log(1 - p))
    return total / len(y_true)

print(round(bce([1, 0, 1], [0.9, 0.1, 0.8]), 4))   # 0.1446
```
> ⚠️ `log(0) = -inf`. Luôn clip xác suất trước khi `log`.
</details>

### Bài 3.6 — Khoảng cách giữa 2 vector (Euclidean, Manhattan, Cosine) *(sát Module A)*
Viết Python thuần (không NumPy) cho 3 độ đo.

<details><summary>💡 Lời giải</summary>

```python
import math

def euclidean(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))   # = L2

def manhattan(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))                # = L1

def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb)

a, b = [1, 0, 1], [1, 1, 0]
print(round(euclidean(a, b), 4))  # 1.4142
print(manhattan(a, b))            # 2
print(round(cosine(a, b), 4))     # 0.5
```
> 🔁 `sum(... for ... in zip(a,b))` = generator, gọn hơn nhiều so với vòng `for` cộng dồn của Java.
</details>

---

## PHẦN 4 — NumPy & Broadcasting

### Bài 4.1 — Dự đoán shape (không chạy, tính trong đầu)
Cho `A.shape = (3, 1)`, `B.shape = (1, 4)`, `C.shape = (3,)`, `D.shape = (2, 3)`.  
`(A + B)`? `(D + C)`? `(A + C)`?

<details><summary>💡 Lời giải</summary>

- `A + B`: `(3,1)` ⊕ `(1,4)` → **`(3, 4)`** (mỗi chiều "1" được kéo giãn).
- `D + C`: `(2,3)` ⊕ `(3,)` → coi `(3,)` thành `(1,3)` → **`(2, 3)`**.
- `A + C`: `(3,1)` ⊕ `(3,)`=`(1,3)` → **`(3, 3)`**.

**Quy tắc broadcasting:** so chiều **từ phải sang trái**; hai chiều hợp lệ khi **bằng nhau** hoặc **một trong hai bằng 1** (chiều 1 sẽ được nhân bản).
</details>

### Bài 4.2 — Chuẩn hóa từng hàng (z-score) bằng broadcasting
Cho ma trận `M (2x3)`, chuẩn hóa **mỗi hàng** về mean 0, std 1.

<details><summary>💡 Lời giải</summary>

```python
import numpy as np

M = np.array([[1., 2, 3], [4, 5, 6]])
means = M.mean(axis=1, keepdims=True)   # shape (2,1) — GIỮ chiều để broadcast
stds  = M.std(axis=1, keepdims=True)    # shape (2,1)
Z = (M - means) / stds                  # (2,3) - (2,1) -> broadcast theo cột
print(np.round(Z, 4))
# [[-1.2247  0.      1.2247]
#  [-1.2247  0.      1.2247]]
```
> ⚠️ `keepdims=True` là chìa khóa: giữ shape `(2,1)` để trừ được vào `(2,3)`. Nếu không, ra `(2,)` và broadcast sai.
</details>

### Bài 4.3 — Vector hóa: bỏ vòng lặp
Cho mảng `prices`, tăng mỗi giá lên 10% rồi làm tròn. Viết **không** dùng `for`.

<details><summary>💡 Lời giải</summary>

```python
import numpy as np

prices = np.array([100, 250, 99, 1500])
new_prices = np.round(prices * 1.1, 2)   # nhân cả mảng 1 phát
print(new_prices)   # [ 110.   275.   108.9 1650. ]
```
> 🔁 Java/C++ phải lặp từng phần tử; NumPy áp phép toán lên cả mảng (nhanh + gọn). Đây là "vector hóa".
</details>

### Bài 4.4 — Tích vô hướng & nhân ma trận: thủ công vs NumPy
So sánh tự viết dot product với toán tử `@`.

<details><summary>💡 Lời giải</summary>

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.dot(a, b))   # 32   (hoặc a @ b)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)          # nhân ma trận: [[19 22] [43 50]]
```
> 🔁 `@` là toán tử nhân ma trận. `*` trong NumPy là nhân **từng phần tử** (element-wise), KHÁC nhân ma trận — chỗ này hay nhầm.
</details>

---

## PHẦN 5 — Metrics & Đánh giá (gắn Module B + C)

### Bài 5.1 — Precision, Recall, F1, Accuracy từ TP/FP/FN/TN
Viết hàm trả về cả 4, có xử lý chia 0.

<details><summary>💡 Lời giải</summary>

```python
def metrics(tp, fp, fn, tn):
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall    = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
    accuracy = (tp + tn) / (tp + fp + fn + tn)
    return {
        "precision": round(precision, 3),
        "recall": round(recall, 3),
        "f1": round(f1, 3),
        "accuracy": round(accuracy, 3),
    }

print(metrics(tp=8, fp=5, fn=2, tn=85))
# {'precision': 0.615, 'recall': 0.8, 'f1': 0.696, 'accuracy': 0.93}
```
> 🔁 `a if cond else b` = biểu thức điều kiện 1 dòng (giống `cond ? a : b`). Dùng để tránh chia 0.
</details>

### Bài 5.2 — Tự dựng Confusion Matrix từ `y_true` / `y_pred`
Cho 2 list nhãn 0/1, đếm TP, FP, FN, TN.

```python
y_true = [1, 1, 0, 0, 1, 0]
y_pred = [1, 0, 0, 1, 1, 0]
```

<details><summary>💡 Lời giải</summary>

```python
def confusion(y_true, y_pred):
    tp = fp = fn = tn = 0
    for t, p in zip(y_true, y_pred):        # duyệt SONG SONG 2 list
        if   t == 1 and p == 1: tp += 1
        elif t == 0 and p == 1: fp += 1
        elif t == 1 and p == 0: fn += 1
        else:                   tn += 1
    return tp, fp, fn, tn

y_true = [1, 1, 0, 0, 1, 0]
y_pred = [1, 0, 0, 1, 1, 0]
print(confusion(y_true, y_pred))   # (2, 1, 1, 2)
```
> 🔁 `zip(y_true, y_pred)` ghép cặp `(t, p)` theo vị trí — không cần index thủ công như Java.
</details>

### Bài 5.3 — Accuracy đa lớp từ y_true/y_pred
Tính tỉ lệ đoán đúng cho nhãn nhiều lớp (vd 0,1,2).

<details><summary>💡 Lời giải</summary>

```python
def accuracy(y_true, y_pred):
    correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
    return correct / len(y_true)

print(accuracy([0, 1, 2, 2, 1], [0, 2, 2, 2, 1]))   # 0.8
```
> 🔁 `sum(1 for ... if cond)` = đếm số phần tử thỏa điều kiện. Pattern cực hay gặp.
</details>

---

## 🎯 Tự kiểm tra: bạn đã quen tay chưa?

Code 3 cái sau **không nhìn lời giải**, nếu làm trơn là ổn cho phòng thi:
1. Đếm tần suất từ trong 1 đoạn văn rồi in top-3.
2. Viết `sigmoid` và `mse` bằng NumPy.
3. Tính precision/recall/F1 từ TP/FP/FN.

### Những idiom Python phải thuộc lòng trước khi thi
```python
[x*2 for x in a]                 # list comprehension
{k: v for k, v in pairs}         # dict comprehension
for i, x in enumerate(a): ...    # duyệt kèm chỉ số
for x, y in zip(a, b): ...       # duyệt 2 list song song
a[::-1]                          # đảo ngược
d.get(key, 0)                    # tra dict có default
" ".join(list_of_str)            # ghép list thành chuỗi
a, b = b, a                      # hoán đổi
f"{x:.2f}"                       # định dạng số
np.array(x); np.mean; np.maximum; np.where; @   # NumPy cốt lõi
```

*Cần thêm bài nhóm nào (vd: regex nâng cao, đọc/ghi file, OOP class trong Python, hay luyện riêng NumPy) thì nói mình soạn tiếp nhé.*
