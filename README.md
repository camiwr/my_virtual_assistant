# 💻 Assistente Virtual em Python

## 📖 Descrição
Este projeto é um assistente virtual desenvolvido em Python, capaz de interagir com o usuário através de consultas de hora/data, previsões do clima, 
envio de lembretes via WhatsApp e respostas a perguntas livres utilizando a Wikipedia. A integração com a API do Twilio permite o envio de mensagens de WhatsApp, 
enquanto o OpenWeatherMap fornece os dados meteorológicos. O assistente também utiliza a biblioteca pyttsx3 para conversão de texto em fala, proporcionando uma experiência interativa e envolvente.

## ✨ Funcionalidades
- Perguntar Hora/Data
- Consultar Clima
- Enviar Lembrete via WhatsApp
- Pergunta Livre (Wikipedia)
- Histórico de Consultas

## 🛠 Tecnologias Usadas
- Python 3.x
- Biblioteca `requests`
- Biblioteca `wikipedia`
- Biblioteca `pyttsx3`
- Biblioteca `twilio`
- API do OpenWeatherMap
- API do Twilio

## 🚀 Como utilizar
### **2. Faça um clone desse repositório na sua máquina:**

* Crie uma pasta no seu computador para esse programa
* Abra o `git bash` ou `terminal` dentro dessa pasta
* Copie a [URL](https://github.com/camiwr/my_virtual_assistant.git) do repositório
* Digite `git clone <URL copiada>` e pressione `enter`

- Instale as dependências: `pip install requests wikipedia pyttsx3 twilio`
caso apareça algum erro referente a alguma das bibliotecas importadas no programa, jogue o nome dela no Google e faça a instalação e passo a passo necessários

- Execute o script principal: `assistente.py`
- Interaja com o assistente através do menu no terminal.

## 🔑 Crie sua chave para as APIs:

**API de clima:**
* Acesse o [Open Wheather Map](https://openweathermap.org/) e faça seu cadastro
* Confirme o email recebido e em configurações, acesse suas API Keys
* Copie a chave e cole no `token` da função `clima()`, substituindo a frase `<suachaveapi>`
  
**API da Twilio:**
* Acesse o [Twilio](https://www.twilio.com/en-us) e crie uma conta.
* Verifique seu email e complete o cadastro.
* No painel da Twilio, vá até a seção de Account SID e Auth Token.
* Copie o Account SID e o Auth Token e cole nas variáveis TWILIO_ACCOUNT_SID e TWILIO_AUTH_TOKEN, respectivamente, no arquivo assistente.py.
* Pegue o número do WhatsApp do Twilio (TWILIO_WHATSAPP_FROM) e cole também no arquivo assistente.py.
* Coloque o seu numero ou o numero do qualquer mandar mensagens no site e faça a verificação via whatsApp.


## 🤝 Contribuindo
Contribuições são sempre bem-vindas! Para contribuir, por favor:
1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nome_da_feature`).
3. Faça suas alterações.
4. Envie um pull request.

## 👤 Autor
- Camilla Soares Sousa

## 📞 Contato
Para mais informações, entre em contato em camillasoares818@gmail.com, ou no meu [linkedIn](https://www.linkedin.com/in/camilla-soares-sousa-a790b3196?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) .
