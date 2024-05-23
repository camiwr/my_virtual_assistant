import pyttsx3
import wikipedia


# Configura o idioma padrão para português
wikipedia.set_lang("pt")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def respond_to_query(query):
    # Responde a consulta do usuário.
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return "Desculpe, sua consulta foi ambígua. Por favor, seja mais específico."
    except wikipedia.exceptions.PageError:
        return "Desculpe, não consegui encontrar informações sobre isso."
    except Exception as e:
        print(f"Erro: {e}")
        return "Desculpe, ocorreu um erro ao buscar informações."
    
def show_history(query_history):
    """Exibe o histórico de consultas."""
    print("\nHistórico de consultas:")
    for i, q in enumerate(query_history, 1):
        print(f"{i}. {q}")

def main():
    """Função principal do assistente."""
    print("Olá! Como posso ajudar você? (Digite 'sair' para encerrar)")
    speak("Olá! Como posso ajudar você?")
    
    query_history = []

    while True:
        try:
            query = input("Você: ").lower()
            
            if 'sair' in query:
                print("Assistente: Até mais!")
                speak("Até mais!")
                break
            else:
                query_history.append(query)
                response = respond_to_query(query)
                print(f"Assistente: {response}")
                speak(response)
        except Exception as e:
            print(f"Erro: {e}")

    # Exibir histórico de consultas ao final da sessão
    show_history(query_history)

if __name__ == "__main__":
    main()
