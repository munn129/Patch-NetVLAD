import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def load_image_list(file_path):
    """
    텍스트 파일에서 이미지 파일 경로를 불러오는 함수.

    Parameters:
        file_path (str): 텍스트 파일 경로.

    Returns:
        list: 이미지 파일 경로 리스트.
    """
    image_list = []
    with open(file_path, 'r') as file:
        for line in file:
            image_list.append(line.strip())  # 각 줄의 개행 문자 제거 후 리스트에 추가
    return image_list

def update(frame):
    """
    애니메이션의 각 프레임을 업데이트하는 함수.

    Parameters:
        frame (int): 현재 프레임 인덱스.
    """
    l_img = cv2.imread(q_list[frame])
    r_img = cv2.imread(d_list[frame])

    l_img = cv2.cvtColor(l_img, cv2.COLOR_BGR2RGB)
    r_img = cv2.cvtColor(r_img, cv2.COLOR_BGR2RGB)

    combined_img = np.hstack((l_img, r_img))

    im.set_array(combined_img)
    return [im]

def main():
    global q_list, d_list, im

    # 이미지 경로 리스트 불러오기
    q_list = load_image_list('q_list.txt')
    d_list = load_image_list('d_list.txt')

    # 이미지 개수가 다를 경우 작은 쪽에 맞춤
    num_frames = min(len(q_list), len(d_list))

    # 첫 번째 이미지를 기반으로 플롯 초기화
    fig, ax = plt.subplots(figsize=(12, 6))
    l_img = cv2.imread(q_list[0])
    r_img = cv2.imread(d_list[0])
    l_img = cv2.cvtColor(l_img, cv2.COLOR_BGR2RGB)
    r_img = cv2.cvtColor(r_img, cv2.COLOR_BGR2RGB)
    combined_img = np.hstack((l_img, r_img))
    im = ax.imshow(combined_img)
    ax.axis('off')
    ax.set_title(f'Left: input                                                Right: retrieved')

    # 애니메이션 생성
    ani = FuncAnimation(fig, update, frames=num_frames, blit=True, interval=0.01)

    plt.show()

if __name__ == '__main__':
    main()
