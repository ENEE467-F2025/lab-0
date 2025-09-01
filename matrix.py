class Matrix:

    def __init__(self, data):

        # ensure data is properly formatted
        n = len(data) # number of rows
        m = len(data[0]) # number of columns
        for row in data:
            if len(row) != m:
                raise Exception("All matrix rows must be of the same length!")
        
        self.data = data
        self.shape = (n, m)
        self.size = n * m

    def __getitem__(self, key):
        # access matrix elements by A[i, j]
        i, j = key
        return self.data[i][j]

    def __setitem__(self, key, value):
        # set matrix elements by A[i, j] = x
        i, j = key
        self.data[i][j] = value

    def __add__(self, B):
        # be sure that the matrices self and B have the same shape
        assert self.shape == B.shape

        # create a new, empty matrix
        data = [[0 for _ in range(self.shape[1])] for __ in range(self.shape[0])]
        X = Matrix(data) # zero matrix with shape self.shape

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                # use our custom indexing
                X[i, j] = self[i, j] + B[i, j]
        
        return X
    
    def __sub__(self, B):
        # implement the code to calculate X = self - B
        return
    
    def __mul__(self, B):
        # implement the code to calculate X = self * B

        if isinstance(B, Matrix):
            # matrix multiplication
            assert self.shape[1] == B.shape[0]
            return
        else:
            # B is a number, scalar multiplication
            return
    
    def __rmul__(self, B):
        # implement the code to calculate X = B * self

        if isinstance(B, Matrix):
            # matrix multiplication
            assert B.shape[1] == self.shape[0]
            return
        else:
            # B is a number, scalar multiplication
            return
    
    def __str__(self):
        # to string method, useful for printing matrices
        s=""
        for row in self.data:
            s+=str(row)+"\n"
        return s

#

def main():
    pass

if __name__ == "__main__":
    main()
