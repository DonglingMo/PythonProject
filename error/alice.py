filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    # 没有处理异常默认跳过
    print(f"File {filename} not found.")
else:
    words = content.split()
    counter = len(words)
    print(f"Found {counter} words in {filename}.")