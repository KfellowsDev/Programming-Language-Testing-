import random

respostas = {
    "olá": ["Oi!", "Olá! Como posso ajudar?", "E aí!"],
     "como vc esta?" : ["estou bem,e vc?"], 
    "adeus": ["Até mais!", "Tchau!", "Nos falamos depois!"]
}

def responder(mensagem):
    return random.choice(respostas.get(mensagem.lower(), ["Não entendi."]))

while True:
    mensagem = input("Você: ")
    if mensagem.lower() == "sair":
        break
    print("Bot:", responder(mensagem))
