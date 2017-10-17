# Python 的資料型態(int, float, bool, str)

## int 和 float

在 Python 中宣告變數後可直接指定一個特定值, 其變數型態自動設定為設定值的型態. 
以下是設定數字型態變數的例子:

```javascript
# 宣告一個整數
a=100
print(a)
print(type(a))

# 宣告一個浮點數
b=10.25
print(b)
print(type(b))
```

以下是執行結果:
```
100
<class 'int'>
10.25
<class 'float'>
```


## str

在 Python 宣告字串可以使用 `單引號` 或 `雙引號`, 以下是一個例子:

```javascript
# 宣告一個字串
a='Hello'
print(a)
print(type(a))

# 宣告另一個字串
b="你好"
print(b)
print(type(b))
```

以下是執行結果:
```
Hello
<class 'str'>
你好
<class 'str'>
```


## bool

在 Python 宣告布林值可設定為 `True` 或 `False`, 或是一個邏輯運算結果, 以下是一個例子:

```javascript
# 宣告一個布林
a=True
print(a)
print(type(a))

# 宣告另一個布林
b=False
print(b)
print(type(b))

# 一個邏輯運算結果
c=10>5
print(c)
print(type(c))
```

以下是執行結果:
```
True
<class 'bool'>
False
<class 'bool'>
True
<class 'bool'>
```



## 型態轉換

在 Python 中可使用 int(), float() 及 str() 函式轉換 int, float 及 str 型態, 以下是一個例子:

```javascript
# 宣告一個整數
a=100
print(a)
print(type(a))

# 將整數轉為字串
b=str(a)
print(b)
print(type(b))

# 宣告一個浮點數
c=123.56
print(c)
print(type(c))

# 將浮點數轉為字串
d=str(c)
print(d)
print(type(d))

# 將浮點數轉為整數(小數捨去)
e=int(c)
print(e)
print(type(e))

# 將浮點數轉為整數(四捨五入)
f=round(c)
print(f)
print(type(f))
```

以下是執行結果:
```
100
<class 'int'>
100
<class 'str'>
123.56
<class 'float'>
123.56
<class 'str'>
123
<class 'int'>
124
<class 'int'>
```