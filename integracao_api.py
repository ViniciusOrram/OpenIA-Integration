import openai
import dotenv
import os

def categorizaProduto(nome_do_produto, categorias_validas):
  prompt_sistema = f"""
  Você é um categorizador de produtos.
  Você deve escolher uma categoria da lista abaixo:
  Se as categorias informadas não forem categorias válidas, responda com "Não posso ajudá-la(o) com isso!"
  #### Lista de categorias válidas
  {categorias_validas}
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
        "content" : {nome_do_produto}
        }
      ],
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
  )

  print(resposta.choices[0].message.content)

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

print("Digite as categorias validas:")
categorias_validas = input()
while True:
  print("Digite o nome do produto:")
  nome_do_produto = input()
  categorizaProduto(nome_do_produto, categorias_validas)