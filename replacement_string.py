import random
import MeCab  # Mecabモジュールをロード

input = input("並べ替えたい文を入力してください: ")
output = list()

m = MeCab.Tagger()
node = m.parseToNode(input)
while node is not None:
    print('表層系 : ' + node.surface)
    output.append(node.surface)
    node = node.next

print(output)

for char in range(1000000):
    i = int((random.random() * 10000000000000000) % len(output))
    j = int((random.random() * 10000000000000000) % len(output))
    c = output[i]
    output[i] = output[j]
    output[j] = c

print(input)
print(''.join(output))
