from PIL import Image, ImageDraw, ImageFont

def is_valid_position(pos):
    # Проверяет, что длина ввода равна 2 символам
    # и что столбец и строка являются допустимыми значениями
    if len(pos) != 2:
        return False
    col, row = pos[0], pos[1]
    return col in 'abcdefgh' and row in '12345678'

def get_valid_position():
    # Запрашивает у пользователя позицию ферзя и проверяет ее допустимость
    while True:
        queen_pos = input("Enter the position of the queen (e.g. c4): ").strip().lower()
        if is_valid_position(queen_pos):
            return queen_pos
        else:
            print("Invalid input! Please enter a position in the format 'a-h' for columns and '1-8' for rows.")

def draw_board(queen_pos):
    # Создает изображение шахматной доски с указанной позицией ферзя
    board_size = 512  # Размер доски
    outline_size = 40  # Размер контура для букв и цифр a-h 1-8

    total_size = board_size + 2 * outline_size

    cell_size = board_size // 8

    board = Image.new('RGB', (total_size, total_size), color='white')
    draw = ImageDraw.Draw(board)

    # Рисует сетку на доске
    for i in range(9):
        draw.line([(outline_size, outline_size + i * cell_size),
                    (total_size - outline_size, outline_size + i * cell_size)], fill='black', width=2)
        draw.line([(outline_size + i * cell_size, outline_size),
                    (outline_size + i * cell_size, total_size - outline_size)], fill='black', width=2)

    # Рисует буквы 'a'-'h' с двух сторон
    font = ImageFont.load_default()
    for i in range(8):
        # Нижняя сторона
        draw.text((outline_size + i * cell_size + cell_size // 2 - 6, outline_size - 20),
                    chr(ord('a') + i), font=font, fill='black')
        # Верхняя сторона
        draw.text((outline_size + i * cell_size + cell_size // 2 - 6, total_size - outline_size + 10),
                    chr(ord('a') + i), font=font, fill='black')

    # Рисует цифры с двух сторон
    for i in range(8):
        # Левая сторона
        draw.text((outline_size // 2 , outline_size + i * cell_size + cell_size // 2), str(8 - i), font=font, fill='black')
        # Правая сторона
        draw.text((total_size - outline_size + outline_size // 2, outline_size + i * cell_size + cell_size // 2 ),
                    str(8 - i), font=font, fill='black')

    # Рисует ферзя на указанной позиции
    qx, qy = ord(queen_pos[0]) - ord('a'), 8 - int(queen_pos[1])

    qrect = (outline_size + qx * cell_size + 2, outline_size + qy * cell_size + 2, outline_size + (qx + 1) * cell_size - 2,
                outline_size + (qy + 1) * cell_size - 2)
    draw.rectangle(qrect, fill='#d2b8a2')
    draw.text((outline_size + qx * cell_size + cell_size // 2, outline_size + qy * cell_size + cell_size // 2),
                'Q', font=font, fill='white')

    # Рисует поля, атакуемые ферзем
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        x, y = qx + dx, qy + dy
        while 0 <= x < 8 and 0 <= y < 8:
            mrect = (outline_size + x * cell_size + 2, outline_size + y * cell_size + 2,
                        outline_size + (x + 1) * cell_size - 2, outline_size + (y + 1) * cell_size - 2)
            draw.rectangle(mrect, fill='#eccc94')
            draw.text((outline_size + x * cell_size + cell_size // 2, outline_size + y * cell_size + cell_size // 2),
                        '*', font=font, fill='white')
            x, y = x + dx, y + dy

    return board
