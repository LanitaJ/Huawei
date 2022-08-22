# Task 3. Treasure map

# solution is dancing links algorithm

class DLX():
    def __init__(self, n, m) -> None:
        self.n = n
        self.m = m
        self.size = m
        self.ansd = 0
        self.row = [0] * m ** 2
        self.col = [0] * m ** 2
        self.H = [0] + [-1] * n
        self.S = [0] * (m + 1)
        self.U = [x for x in range(0, m + 1)]
        self.D = [x for x in range(0, m + 1)]
        self.L = [m] + [x for x in range(0, m)]
        self.R = [x for x in range(1, m + 1)] + [0]

    def link(self, r, c):
        self.size += 1
        self.col[self.size] = c
        self.S[c] += 1
        self.row[self.size] = r

        self.D.insert(self.size, self.D[c])
        self.U[self.D[c]] = self.size
        self.U.insert(self.size, c)
        self.D[c] = self.size
        if (self.H[r] < 0):
            self.H[r] = self.size
            self.L.insert(self.size, self.size)
            self.R.insert(self.size, self.size)
        else:
            self.R.insert(self.size, self.R[self.H[r]])
            self.L[self.R[self.H[r]]] = self.size
            self.L.insert(self.size, self.H[r])
            self.R[self.H[r]] = self.size

    def remove(self, c):
        self.L[self.R[c]] = self.L[c] 
        self.R[self.L[c]] = self.R[c]

        i = self.D[c]
        while i != c:
            j = self.R[i]
            while j != i:
                self.U[self.D[j]] = self.U[j]
                self.D[self.U[j]] = self.D[j]
                self.S[self.col[j]] -= 1
                j = self.R[j]
            i = self.D[i]

    def resume(self, c):
        i = self.U[c]
        while i != c:
            j = self.L[i]
            while j != i:
                self.U[self.D[j]] = self.D[self.U[j]] = j
                self.S[self.col[j]] += 1
                j = self.L[j]
            i = self.U[i]
        self.L[self.R[c]] = self.R[self.L[c]] = c

    def dance(self, d):
        if (self.ansd != -1 and self.ansd <= d):
            return
        if (self.R[0] == 0):
            if(self.ansd == -1):
                self.ansd = d
            else:
                if(d < self.ansd):
                   self.ansd = d
                return
        c = self.R[0]
        i = self.R[0]
        while i != 0:
            if (self.S[i] < self.S[c]):
                c = i
            i = self.R[i]
        self.remove(c)
        i = self.D[c]
        while i != c:
            j = self.R[i]
            while j != i:
                self.remove(self.col[j])
                j = self.R[j]
            self.dance(d + 1)
            jj = self.L[i]
            while jj != i:
                self.resume(self.col[jj])
                jj = self.L[jj]
            i = self.D[i]
        self.resume(c)


t = int(input())
while (t):
    t -= 1
    n, m, p = [int(x) for x in input().split()]
    g = DLX(p, n * m)
    for k in range(1, p + 1):
        x1, y1, x2, y2 = [int(x) for x in input().split()]
        for i in range(x1 + 1, x2 + 1):
            for j in range(y1 + 1, y2 + 1):
                g.link(k, j + (i - 1) * m)
    g.ansd = -1
    g.dance(0)
    print(f"{g.ansd}\n",)
