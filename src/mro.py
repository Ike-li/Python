class A:
    """
    A class
    """

    def __init__(self):
        print("A init")


class B(A):
    """
    B class
    """

    def __init__(self):
        super().__init__()
        print("B init")


class C(A):
    """C class"""

    def __init__(self):
        super().__init__()
        print("C init")


class D(B, C):
    """
    D class
    """

    def __init__(self):
        print("D init")
        super().__init__()
