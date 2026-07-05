class Node:
    def __init__(self, pasien):
        self.pasien = pasien
        self.left = None
        self.right = None


class BSTPasien:
    def __init__(self):
        self.root = None

    def insert(self, pasien):
        self.root = self._insert(self.root, pasien)

    def _insert(self, root, pasien):

        if root is None:
            return Node(pasien)

        if pasien.id_pasien < root.pasien.id_pasien:
            root.left = self._insert(root.left, pasien)

        elif pasien.id_pasien > root.pasien.id_pasien:
            root.right = self._insert(root.right, pasien)

        else:
            print("ID Pasien sudah ada!")

        return root

    def search(self, id_pasien):
        return self._search(self.root, id_pasien)

    def _search(self, root, id_pasien):

        if root is None:
            return None

        if root.pasien.id_pasien == id_pasien:
            return root.pasien

        if id_pasien < root.pasien.id_pasien:
            return self._search(root.left, id_pasien)

        return self._search(root.right, id_pasien)
    
    def delete(self, id_pasien):
        self.root = self._delete(self.root, id_pasien)

    def _delete(self, root, id_pasien):

        if root is None:
            return None

        if id_pasien < root.pasien.id_pasien:
            root.left = self._delete(root.left, id_pasien)

        elif id_pasien > root.pasien.id_pasien:
            root.right = self._delete(root.right, id_pasien)

        else:
            if root.left is None and root.right is None:
                return None
            
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left
            
            temp = self._min_value(root.right)

            root.pasien = temp.pasien

            root.right = self._delete(
                root.right,
                temp.pasien.id_pasien
            )
            
        return root
    
    def _min_value(self, node):

        current = node

        while current.left is not None:
            current = current.left

        return current
    
    def inorder(self):

        if self.root is None:
            print("\nData pasien kosong.")
            return

        print("\n========== DATA PASIEN ==========")
        self._inorder(self.root)

    def _inorder(self, root):

        if root is not None:

            self._inorder(root.left)

            p = root.pasien

            print(f"ID        : {p.id_pasien}")
            print(f"Nama      : {p.nama}")
            print(f"Umur      : {p.umur}")
            print(f"Keluhan   : {p.keluhan}")
            print(f"Prioritas : {p.prioritas}")
            print("-" * 35)

            self._inorder(root.right)

    def height(self):
        return self._height(self.root)

    def _height(self, root):

        if root is None:
            return 0

        kiri = self._height(root.left)
        kanan = self._height(root.right)

        return max(kiri, kanan) + 1
    
    def node_count(self):
        return self._node_count(self.root)

    def _node_count(self, root):

        if root is None:
            return 0

        return (
            1
            + self._node_count(root.left)
            + self._node_count(root.right)
        )