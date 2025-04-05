import flet as ft

def main(page: ft.Page):
    page.title = "Chatbot com Flet"
    page.theme_mode = ft.ThemeMode.LIGHT  # Pode alternar para DARK se preferir
    page.bgcolor = "#F5F5F5"
    
    # Cabeçalho estilizado
    header = ft.Container(
        content=ft.Text("Chatbot", size=24, weight=ft.FontWeight.BOLD),
        alignment=ft.alignment.center,
        padding=10,
        bgcolor="#007BFF",
        border_radius=10,
        margin=10,
    )
    
    # Campo de entrada e área de conversa
    input_field = ft.TextField(label="Digite sua mensagem", width=300)
    chat_box = ft.Column([], scroll=ft.ScrollMode.AUTO, width=400, height=300, bgcolor="white", padding=10, border_radius=10)
    
    def on_send_click(e):
        # Pega a mensagem digitada pelo usuário
        user_message = input_field.value
        if user_message:
            # Adiciona a mensagem do usuário na caixa de chat
            chat_box.controls.append(ft.Text(f"Você: {user_message}", size=16, color="black"))
            
            # Resposta do chatbot (aqui você pode personalizar a lógica da resposta)
            bot_response = f"Eu sou um chatbot! Você disse: {user_message}"
            chat_box.controls.append(ft.Text(f"Chatbot: {bot_response}", size=16, color="#007BFF"))
            
            # Limpa o campo de entrada
            input_field.value = ""
            
            # Atualiza a tela
            page.update()

    send_button = ft.ElevatedButton("Enviar", on_click=on_send_click, bgcolor="#007BFF", color="white")
    
    # Layout
    content = ft.Column([
        header,
        chat_box,
        input_field,
        send_button
    ], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    page.add(content)

ft.app(target=main, view=ft.WEB_BROWSER)
