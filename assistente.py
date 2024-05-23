import pyttsx3
import wikipedia
import datetime
import requests


# Configura o idioma padrão para português
wikipedia.set_lang("pt")

# Chave de API para o OpenWeatherMap
API_KEY = "3ec7e302c5eabb0234748dd6a03eedab"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_current_time():
    #Retorna a data e hora atual.
    now = datetime.datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")

def request_city_name():
    #Solicita o nome da cidade ao usuário.
    city = input("Digite o nome da cidade para a qual deseja saber o clima: ")
    return city

def get_weather(city):
    #Obtém informações sobre o clima de uma cidade
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + API_KEY + "&q=" + city + "&units=metric&lang=pt"
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temp = main["temp"]
        return f"Atualmente, em {city}, está {weather_desc} com temperatura de {temp}°C."
    else:
        return "Desculpe, não consegui encontrar informações sobre o clima dessa cidade."

def respond_to_query(query):
    # Responde a consulta do usuário.
    try:
        if 'hora' in query or 'data' in query:
            return get_current_time()
        elif 'clima' in query:
            city = request_city_name()
            return get_weather(city)
        else:
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
