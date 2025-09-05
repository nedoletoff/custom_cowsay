import textwrap
import time

def rainbow_text(text):
    """Генерирует текст с переливающимися цветами используя ANSI escape codes"""
    colors = [
        "\033[38;5;196m",  # красный
        "\033[38;5;202m",  # оранжевый
        "\033[38;5;226m",  # желтый
        "\033[38;5;46m",   # зеленый
        "\033[38;5;21m",   # синий
        "\033[38;5;93m",   # фиолетовый
        "\033[38;5;201m",  # розовый
    ]
    
    rainbow_str = ""
    for i, char in enumerate(text):
        color_index = (i + int(time.time() * 5)) % len(colors)
        rainbow_str += f"{colors[color_index]}{char}"
    
    rainbow_str += "\033[0m"  # сброс цвета
    return rainbow_str

def custom_cowsay(text, cow_type='default', rainbow=False):
    # Создаем "пузырь" с текстом
    lines = textwrap.wrap(text, width=40)
    if len(lines) == 1:
        # Однострочный пузырь
        bubble = f"< {lines[0]} >"
        top_border = " " + "_" * (len(lines[0]) + 2)
        bottom_border = " " + "-" * (len(lines[0]) + 2)
    else:
        # Многострочный пузырь
        max_len = max(len(line) for line in lines)
        top_border = " " + "_" * (max_len + 2)
        bottom_border = " " + "-" * (max_len + 2)
        
        bubble = ""
        for i, line in enumerate(lines):
            if i == 0:
                bubble += f"/ {line.ljust(max_len)} \\\n"
            elif i == len(lines) - 1:
                bubble += f"\\ {line.ljust(max_len)} /"
            else:
                bubble += f"| {line.ljust(max_len)} |\n"

    # Выбираем коровку
    if cow_type == 'default':
        cow = """
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
        """
    elif cow_type == 'dragon':
        cow = """
        \\                    / \\  //\\
         \\    |\\___/|      /   \\//  \\\\
              /0  0  \\__  /    //  | \\ \\    
             /     /  \\/_/    //   |  \\  \\  
             @_^_@'/   \\/_   //    |   \\   \\ 
             //_^_/     \\/_ //     |    \\    \\
          ( //) |        \\///      |     \\     \\
        ( / /) _|_ /   )  //       |      \\     _\\
      ( // /) '/,_ _ _/  ( ; -.    |    _ _\\.-~        .-~~~^-.
    (( / / )) ,-{        _      `-.|.-~-.           .~         `.
   (( // / ))  '/\\      /                 ~-. _ .-~      .-~^-.  \\
   (( / / ))     `.   {            }                   /      \\  \\
    (( / ))     .----~-.\\        \\-'                 .~         \\  `. \\^-.
               ///.----..>        \\             _ -~             `.  ^-`  ^-_
                 ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~
                                                                   /.-~
        """
    else:
        cow = f"""
        \\   Unknown cow type: {cow_type}
         \\  
        """

    result = top_border + "\n" + bubble + "\n" + bottom_border + cow
    
    # Применяем радужный эффект если нужно
    if rainbow:
        result = rainbow_text(result)
    
    return result

if __name__ == '__main__':
    text = input('Enter text: ')
    print(custom_cowsay(text))
    print(custom_cowsay(text, 'dragon', True))