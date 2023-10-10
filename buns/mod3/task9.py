def calculate_final_position(n):
    x, y = 0, 0
    step = 1
    step_count = 0
    direction = 2

    for i in range(1, n + 1):
        for j in range(step):
            if direction == 1:
                y += 1
            elif direction == 2:
                x -= 1
            elif direction == 3:
                y -= 1
            elif direction == 4:
                x += 1
            step_count += 1
            if step_count == n:
                break
        if step_count == n:
            break

        if i % 2 == 0:
            step += 1

        direction = (direction % 4) + 1

    return [x, y]


def main():
    n = int(input())
    final_position = calculate_final_position(n)
    print(*final_position)


if __name__ == "__main__":
    main()
