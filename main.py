from flask import Flask, request, Response
from cowsay import custom_cowsay

app = Flask(__name__)



@app.route('/')
def say():
    message = request.args.get('msg', 'Hello from my custom cowsay!')
    cow_type = request.args.get('cow', 'default')
    rainbow = request.args.get('rainbow', '').lower() in ['1', 'true', 'yes']
    
    # Генерируем ответ с помощью нашей функции
    output = custom_cowsay(message, cow_type, rainbow)
    
    # Для браузеров преобразуем ANSI коды в HTML
    user_agent = request.headers.get('User-Agent', '')
    if 'Mozilla' in user_agent and rainbow:
        output = ansi_to_html(output)
        return Response(output, content_type='text/html; charset=utf-8')
    
    # Возвращаем как plain text для терминалов
    return Response(output, content_type='text/plain; charset=utf-8')

def ansi_to_html(text):
    """Преобразует ANSI escape codes в HTML теги"""
    # Простая реализация преобразования ANSI в HTML
    text = text.replace('\033[38;5;196m', '<span style="color: #ff0000;">')
    text = text.replace('\033[38;5;202m', '<span style="color: #ff5f00;">')
    text = text.replace('\033[38;5;226m', '<span style="color: #ffff00;">')
    text = text.replace('\033[38;5;46m', '<span style="color: #00ff00;">')
    text = text.replace('\033[38;5;21m', '<span style="color: #0000ff;">')
    text = text.replace('\033[38;5;93m', '<span style="color: #8700ff;">')
    text = text.replace('\033[38;5;201m', '<span style="color: #ff00ff;">')
    text = text.replace('\033[0m', '</span>')
    
    # Сохраняем переносы строк
    text = text.replace('\n', '<br>')
    text = text.replace(' ', '&nbsp;')
    
    # Добавляем моноширинный шрифт для правильного отображения
    return f'<html><body style="background-color: black; font-family: monospace; white-space: pre;">{text}</body></html>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)