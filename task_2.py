import matplotlib.pyplot as plt

def koch_snowflake(order, ax, p1, p2):
    if order == 0:
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'b')
    else:
        # Розрахунок нових точок
        x1, y1 = p1
        x2, y2 = p2
        dx, dy = x2 - x1, y2 - y1
        
        p3 = (x1 + dx / 3, y1 + dy / 3)
        p5 = (x1 + 2 * dx / 3, y1 + 2 * dy / 3)
        
        # Вершина трикутника
        p4 = (0.5 * (x1 + x2) - (3**0.5 / 6) * (y2 - y1),
              0.5 * (y1 + y2) + (3**0.5 / 6) * (x2 - x1))
        
        # Рекурсія для кожного сегмента
        koch_snowflake(order - 1, ax, p1, p3)
        koch_snowflake(order - 1, ax, p3, p4)
        koch_snowflake(order - 1, ax, p4, p5)
        koch_snowflake(order - 1, ax, p5, p2)

def draw_snowflake(order):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    # Вершини рівностороннього трикутника
    p1 = (0, 0)
    p2 = (1, 0)
    p3 = (0.5, 3**0.5 / 2)

    # Малювання трьох сторін сніжинки
    koch_snowflake(order, ax, p1, p2)
    koch_snowflake(order, ax, p2, p3)
    koch_snowflake(order, ax, p3, p1)

    plt.show()

if __name__ == "__main__":
    order = int(input("Введіть рівень рекурсії: "))
    draw_snowflake(order)
