# saludos.py
from utils.printer import print_message

def saludo(name: str):
    """Genera un saludo informal."""
    message = f"¡Hey {name}! ¿Qué tal?"
    print_message(message)
    
def greet_in_english(name: str):
    """Genera un saludo simple en inglés."""
    message = f"Hello, {name}!"
    print_message(message)