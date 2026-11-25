import sys


class PriorityQueue:

    def __init__(self):
        self.heap = []
        self.pos = {}

    def _swap(self, i, j):
        h = self.heap
        h[i], h[j] = h[j], h[i]
        self.pos[h[i][1]] = i
        self.pos[h[j][1]] = j

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent][0] >= self.heap[i][0]:
                break
            self._swap(i, parent)
            i = parent

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            largest = i
            left = 2 * i + 1
            right = left + 1
            if left < n and self.heap[left][0] > self.heap[largest][0]:
                largest = left
            if right < n and self.heap[right][0] > self.heap[largest][0]:
                largest = right
            if largest == i:
                return
            self._swap(i, largest)
            i = largest

    def add(self, key, priority):
        self.heap.append([priority, key])
        self.pos[key] = len(self.heap) - 1
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        top = self.heap[0]
        last = self.heap.pop()
        del self.pos[top[1]]
        if self.heap:
            self.heap[0] = last
            self.pos[last[1]] = 0
            self._sift_down(0)
        return top

    def change(self, key, priority):
        i = self.pos[key]
        old = self.heap[i][0]
        self.heap[i][0] = priority
        if priority > old:
            self._sift_up(i)
        else:
            self._sift_down(i)


def main():
    queue = PriorityQueue()
    out = []
    for line in sys.stdin:
        cmd = line.split()
        if not cmd:
            continue
        if cmd[0] == "ADD":
            queue.add(cmd[1], int(cmd[2]))
        elif cmd[0] == "POP":
            priority, key = queue.pop()
            out.append(key + " " + str(priority))
        elif cmd[0] == "CHANGE":
            queue.change(cmd[1], int(cmd[2]))
    if out:
        sys.stdout.write("\n".join(out) + "\n")


main()
