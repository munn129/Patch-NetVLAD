def main():

    file_names = [i for i in range(0,455)]

    with open('webcam.txt', 'w') as file:
        for name in file_names:
            file.write(f'webcam_dataset/{name:06d}.png\n')

if __name__ == '__main__':
    main()