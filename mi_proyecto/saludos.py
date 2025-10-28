# saludos.py
from utils.printer import print_message

def saludo_formal(name: str):
  """Genera un saludo formal."""
  message = f"Buenos días, {name}. Espero que tengas un excelente día."
  print_message(message)

def saludo_informal(name: str):
  """Genera un saludo informal."""
  message = f"¡Hey {name}! ¿Qué tal?"
  print_message(message)

def saludo(name: str, tipo: str = "informal"):
  """Genera un saludo basado en el tipo especificado."""
  if tipo == "formal":
  saludo_formal(name)
  else:
  saludo_informal(name)

    
def greet_in_english(name: str):
    """Genera un saludo simple en inglés."""
    message = f"Hello, {name}!"
    print_message(message)