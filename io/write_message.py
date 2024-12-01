filename = "test.txt"
# 在当前代码路径下生成文件
with open(filename, "w") as file_object:
    file_object.write("hello world\n")
    file_object.write("hello world\n")
    file_object.write("hello world\n")
    file_object.close()