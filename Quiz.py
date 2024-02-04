# Definiert eine Klasse namens 'Question'.
class Question:
    # Der Konstruktor __init__ wird aufgerufen, wenn ein neues 'Question'-Objekt erstellt wird.
    # Er initialisiert die Objekteigenschaften mit den spezifizierten Werten.
    def __init__(self, prompt, answer):
        # 'self' repräsentiert das Objekt, das gerade erstellt wird.
        # Hier weisen wir den übergebenen Werten den Eigenschaften des Objekts zu.
        
        self.prompt = prompt  # 'prompt' ist der Text der Frage, inklusive der Antwortmöglichkeiten.
        self.answer = answer  # 'answer' ist der Buchstabe, der die korrekte Antwort repräsentiert.
