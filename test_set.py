# test_settopy.py
from settopy_bindings import SetToPy

def main():
    s = SetToPy()

    # Test adding elements
    s.add(1.0, 2.0, 3.0)
    s.add(4.0, 5.0, 6.0)
    print("After adding elements:")
    print("Contains (1.0, 2.0, 3.0):", s.contains(1.0, 2.0, 3.0))  # Should print: True
    print("Contains (4.0, 5.0, 6.0):", s.contains(4.0, 5.0, 6.0))  # Should print: True
    print("Size:", s.size())  # Should print: 2

    # Test removing elements
    s.remove(1.0, 2.0, 3.0)
    print("After removing (1.0, 2.0, 3.0):")
    print("Contains (1.0, 2.0, 3.0):", s.contains(1.0, 2.0, 3.0))  # Should print: False
    print("Size:", s.size())  # Should print: 1

    # Test getting all elements
    elements = s.get_elements()
    print("Remaining elements:", elements)

if __name__ == "__main__":
    main()
