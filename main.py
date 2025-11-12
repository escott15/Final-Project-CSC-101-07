###

# Given an input float and a threshold float, return True if the input is larger
# than the threshold and False otherwise
def over_threshold(value: float, threshold: float) -> bool:
    if value > threshold:
        return True
    else:
        return False