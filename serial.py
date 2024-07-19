"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Initialize with the start number."""
        self.start = start
        self.current = start
    
    def generate(self):
        """Return the next serial number."""
        current = self.current
        self.current += 1
        return current
    
    def reset(self):
        """Reset the current number to the start number."""
        self.current = self.start

    def __repr__(self):
        """Return a useful representation of the object."""
        return f"<SerialGenerator start={self.start} next={self.current}>"