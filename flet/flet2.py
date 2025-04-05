
import flet as ft
import requests
import os

# Configuração da API Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Substitua ou use variável de ambiente
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Função para gerar a resposta do chatbot usando a API da Groq
def resposta_chatbot(mensagem, model="llama3-70b-8192", temperature=0.7):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "messages": [
            {
                "role": "system",
                "content": "Você é um assistente útil, prestativo e educado."
            },
            {
                "role": "user",
                "content": mensagem
            }
        ],
        "model": model,
        "temperature": temperature,
        "max_tokens": 1024
    }
    
    try:
        response = requests.post(GROQ_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        
        resposta_api = response.json()
        return resposta_api["choices"][0]["message"]["content"]
    
    except requests.exceptions.RequestException as e:
        return f"Erro ao conectar com a API Groq: {str(e)}"
    except (KeyError, IndexError) as e:
        return "Erro ao processar a resposta da API."

# Função principal da interface
def main(page: ft.Page):
    page.title = "ChatBot Groq"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Elementos da interface
    chat_box = ft.ListView(expand=True, spacing=10, auto_scroll=True)
    text_input = ft.TextField(
        label="Digite sua mensagem",
        autofocus=True,
        expand=True,
        on_submit=lambda e: enviar_mensagem(e)
    )
    
    # Botão de envio
    send_button = ft.ElevatedButton(
        "Enviar",
        icon=ft.icons.SEND,
        on_click=lambda e: enviar_mensagem(e)
    )
    
    # Função para enviar mensagem
    def enviar_mensagem(e):
        if not text_input.value.strip():
            return
            
        # Adiciona mensagem do usuário ao chat
        chat_box.controls.append(
            ft.Container(
                ft.Text(f"Você: {text_input.value}", color=ft.colors.BLUE_800),
                bgcolor=ft.colors.BLUE_100,
                padding=10,
                border_radius=10,
                alignment=ft.alignment.top_left
            )
        )
        
        user_message = text_input.value
        text_input.value = ""
        page.update()
        
        # Mostra indicador de digitação
        typing_indicator = ft.Text("Bot: digitando...", italic=True, color=ft.colors.GREY)
        chat_box.controls.append(typing_indicator)
        page.update()
        
        # Obtém resposta do bot
        bot_response = resposta_chatbot(user_message)
        
        # Remove indicador e adiciona resposta real
        chat_box.controls.remove(typing_indicator)
        chat_box.controls.append(
            ft.Container(
                ft.Text(f"Bot: {bot_response}", color=ft.colors.GREEN_800),
                bgcolor=ft.colors.GREEN_100,
                padding=10,
                border_radius=10,
                alignment=ft.alignment.top_left
            )
        )
        
        page.update()
    
    # Layout da interface
    input_row = ft.Row(
        controls=[text_input, send_button],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )
    
    page.add(
        ft.Container(
            content=chat_box,
            expand=True,
            padding=20,
            margin=10,
            border=ft.border.all(1, ft.colors.GREY_300),
            border_radius=10
        ),
        ft.Divider(),
        input_row
    )

# Executar o aplicativo
if __name__ == "__main__":
    ft.app(target=main)