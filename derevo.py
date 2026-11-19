class Node:
    def __init__(self, value):
        self.value = value    # Значення вузла
        self.left = None      # Посилання на лівого нащадка (null)
        self.right = None     # Посилання на правого нащадка (null)


class BinaryTree:
    def __init__(self):
        self.root = None      # Посилання на кореневий елемент

    # 1. Додати елемент
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        else:  # значення більше або рівне поточному вузлу
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    # 2. Видалити елемент
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current, value):
        if current is None:
            return None

        if value < current.value:
            current.left = self._delete_recursive(current.left, value)
        elif value > current.value:
            current.right = self._delete_recursive(current.right, value)
        else:
            # Випадок 1 і 2: немає нащадків або є лише один нащадок
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left

            # Випадок 3: є обидва нащадки — шукаємо найменший (найбільш лівий) у правому піддереві
            min_node = self._get_min_node(current.right)
            current.value = min_node.value
            current.right = self._delete_recursive(current.right, min_node.value)

        return current

    # 3. Перевірити наявність елемента (знайти)
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if current is None:
            return False
        if value == current.value:
            return True
        if value < current.value:
            return self._search_recursive(current.left, value)
        return self._search_recursive(current.right, value)

    # 4. Вивести всі елементи 
    def display(self):
        elements = []
        self._inorder_traversal(self.root, elements)
        if not elements:
            print("Дерево порожнє.")
        else:
            print("Елементи дерева:", " ".join(map(str, elements)))

    def _inorder_traversal(self, current, elements):
        if current is not None:
            self._inorder_traversal(current.left, elements)
            elements.append(current.value)
            self._inorder_traversal(current.right, elements)

    # 5. Вивести найбільший елемент
    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

    # 6. Вивести найменший елемент
    def find_min(self):
        if self.root is None:
            return None
        return self._get_min_node(self.root).value

    def _get_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # 7. Вивести кількість елементів
    def count(self):
        return self._count_recursive(self.root)

    def _count_recursive(self, current):
        if current is None:
            return 0
        return 1 + self._count_recursive(current.left) + self._count_recursive(current.right)



if __name__ == "__main__":
    tree = BinaryTree()

    # Додаємо елементи: 3, 1, 9, 1, 7, 10, 6, 8
    for num in [3, 1, 9, 1, 7, 10, 6, 8]:
        tree.insert(num)

    tree.display()
    print("Кількість елементів:", tree.count())
    print("Найменший елемент:", tree.find_min())
    print("Найбільший елемент:", tree.find_max())

    # Пошук елементів
    print("Чи є елемент 7 у дереві?:", tree.search(7))
    print("Чи є елемент 5 у дереві?:", tree.search(5))

    # Видалення кореневого елемента 3 (замінюється на 6 — найбільш лівий у правій частині)
    print("\nВидаляємо елемент 3...")
    tree.delete(3)
    tree.display()
    print("Кількість елементів після видалення:", tree.count())
