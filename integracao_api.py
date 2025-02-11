import openai
import dotenv
import os

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
prompt_sistema = """
Você é um categorizador de produtos.
Você deve escolher uma categoria da lista abaixo:
#### Lista de categorias válidas
Beleza
Entretenimento
Esportes
Outros
#### Exemplo
Bola de tênis
Esportes
"""

resposta = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k",
    messages = [
      {
       "role" : "system",
       "content" : prompt_sistema
      },
      {
       "role" : "user",
       "content" : "Bola de tênis de mesa"
      }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
for i in range(0, 5):
  print(resposta.choices[i].message.content)

