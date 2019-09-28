'''闭包'''


def make_printer(msg1, msg2):
    def printer():
        print
        msg1, msg2

    return printer



printer = make_printer('Foo', 'Bar')  # 形成闭包

# printer.__closure__  # 返回cell元组
#
# printer.__closure__[0].cell_contents  # 第一个外部变量
#
# printer.__closure__[1].cell_contents  # 第二个外部变量
