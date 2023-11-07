import torch

def expect_eq(name, actual, expected):
    if expected != actual:
        raise Exception(f"Expected {name} to be {expected}, was {actual}")

def expect_tensor_close(name, actual, expected, atol = 0.0001):
    if not torch.is_tensor(actual):
        raise Exception(f"Expected {name} to be a tensor, was {type(actual)}.")
    if not torch.isclose(expected, actual, rtol = 0.0, atol = atol).all():
        raise Exception(f"Expected {name} to be \n{expected}\n, was \n{actual}")
