# Built-in imports

def reverse(text: str) -> str:
    """reverses the text and returns it"""
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]

def is_palindrome(text: str) -> bool:
    """checks if the text is palindromic"""
    if len(text) <= 1:
        return True
    return text[0] == text[-1] and is_palindrome(text[1:-1])
