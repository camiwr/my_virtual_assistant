import pyttsx3
import wikipedia
import datetime
import requests
from twilio.rest import Client

# Configura o idioma padrão para português
wikipedia.set_lang("pt")

# Chave de API para o OpenWeatherMap
API_KEY = "3ec7e302c5eabb0234748dd6a03eedab"



def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_current_time():
    #Retorna a hora atual.
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def get_current_data():
    #Retorna a data atual.
    now = datetime.datetime.now()
    return now.strftime("%d-%m-%Y")

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
    print("=======================================")
    print("          Assistente Virtual           ")
    print("          Ola, Bem vindo(a)!            ")
    print("       Como posso ajudar você hoje?    ")
    print("=======================================")
    speak("Olá! Bem-vindo(a), Como posso ajudar você hoje?")
    
    query_history = []

    while True:
        print("\n=========== Menu de Opções ===========")
        print("1. Perguntar Data")
        print("2. Perguntar Hora")
        print("3. Consultar Clima")
        print("4. Enviar Lembrete")
        print("5. Pergunta Livre")
        print("6. Sair")
        print("=======================================")
        
        choice = input("Escolha uma opção (1-5): ")

        if choice == '6':
            print("Assistente: Até mais!")
            speak("Até mais!")
            break
        elif choice == '5':
            query = input("Qual é a sua pergunta? ")
            query_history.append(query)
            response = respond_to_query(query)
            print(f"Assistente: {response}")
            speak(response)
        elif choice == '4':
            query_history.append('lembrete')
            handle_reminder()
        elif choice == '3':
            query_history.append('clima')
            city = request_city_name()
            response = get_weather(city)
            print(f"Assistente: {response}")
            speak(response)
        elif choice == '2':
            query_history.append('hora')
            response = get_current_time()
            print(f"Assistente: {response}")
            speak(response)
        elif choice == '1':
            query_history.append('data')
            response = get_current_data()
            print(f"Assistente: {response}")
            speak(response)
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    # Exibir histórico de consultas ao final da sessão
    show_history(query_history)

if __name__ == "__main__":
    main()
