def main():
    f = open('d.txt', 'w')

    init_num = 19
    end_num = 2465
    dataset = 'q'

    for i in range(init_num, end_num + 1):
        data = f'{dataset}/{i:06d}.png\n'
        f.write(data)

    f.close()

if __name__ == "__main__":
    main()