class DynamicStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            raise Exception("Stack Underflow")
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


def reverse_word_dynamic(word):
    stack = DynamicStack()

    # Push each character
    for ch in word:
        stack.push(ch)

    # Pop each character to reverse
    reversed_word = []
    while not stack.is_empty():
        reversed_word.append(stack.pop())

    return ''.join(reversed_word)


def reverse_each_word_dynamic(sentence):
    words = sentence.split()
    reversed_words = [reverse_word_dynamic(word) for word in words]
    return ' '.join(reversed_words)


# Example
input_str = "hello world"
output_dynamic = reverse_each_word_dynamic(input_str)
print("Dynamic Stack Output:", output_dynamic)
