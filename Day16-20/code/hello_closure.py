bar = "Hello!"  # 自由变量 bar

print("1. hello_closure module bar: %s" % bar)


def foo():
    global bar  # 参见名字搜索规则 LEGB
    print("3. hello_closure module bar: %s" % bar)  # 开始引用外部的自由变量
    bar = bar + " Closure!"
    print("4. hello_closure module bar: %s" % bar)


if __name__ == "__main__":
    print("2. hello_closure module bar: %s" % bar)
    foo()
    print("5. hello_closure module bar: %s" % bar)
    foo()
    print("6. hello_closure module bar: %s" % bar)
    bar = "Hello!"
    print("7. hello_closure module bar: %s" % bar)
