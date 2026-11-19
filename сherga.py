class ArrayQueue:
    def __init__(self, capacity=13):
        # Виділяємо масив фіксованого розміру 
        self.capacity = capacity
        self.data = [None] * capacity
        # Якщо head == tail, черга порожня
        self.head = 0
        self.tail = 0

    def is_empty(self):
        """Перевірка, чи порожня черга."""
        return self.head == self.tail

    def is_full(self):
        """Перевірка, чи заповнена черга."""
        return (self.tail + 1) % self.capacity == self.head

    def enqueue(self, value):
        """Додавання нового елемента в кінець черги (Tail)."""
        if self.is_full():
            print("Помилка: черга переповнена!")
            return
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity

    def dequeue(self):
        """Видалення та повернення першого елемента з початку черги (Head) за правилом FIFO."""
        if self.is_empty():
            print("Помилка: черга порожня!")
            return None
        value = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % self.capacity
        return value

    def size(self):
        """Повертає кількість елементів у черзі."""
        return (self.tail - self.head + self.capacity) % self.capacity

    def display(self):
        """Виводить усі елементи черги від Head до Tail."""
        if self.is_empty():
            print("Черга порожня.")
            return
        elements = []
        for i in range(self.size()):
            index = (self.head + i) % self.capacity
            elements.append(str(self.data[index]))
        print("Елементи черги (FIFO):", " -> ".join(elements))



if __name__ == "__main__":
    q_arr = ArrayQueue(capacity=13)

    # Додаємо елементи 
    for num in [6, 4, 6, 2, 7]:
        q_arr.enqueue(num)

    q_arr.display()
    print("Кількість елементів:", q_arr.size())

    # Видаляємо елементи за правилом FIFO
    print("Видалено елемент:", q_arr.dequeue())
    print("Видалено елемент:", q_arr.dequeue())

    q_arr.display()
    print("Кількість елементів після видалення:", q_arr.size())
