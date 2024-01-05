import pygame
import sys
import random

# 初始化 Pygame
pygame.init()

# 設定遊戲視窗大小
window_size = (800, 600)

# 建立視窗
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("躲避障礙物遊戲")

# 設定顏色
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

# 設定角色和障礙物大小
player_size = 50
obstacle_size = 50

# 設定角色初始位置
player_x = window_size[0] // 2 - player_size // 2
player_y = window_size[1] - player_size - 10

# 設定障礙物初始位置和速度
obstacle_x = random.randint(0, window_size[0] - obstacle_size)
obstacle_y = 0
obstacle_speed = 5

# 設定遊戲迴圈
clock = pygame.time.Clock()
score = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 控制角色的移動
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < window_size[0] - player_size:
        player_x += 5

    # 移動障礙物
    obstacle_y += obstacle_speed
    if obstacle_y > window_size[1]:
        obstacle_y = 0
        obstacle_x = random.randint(0, window_size[0] - obstacle_size)
        score += 1

    # 檢查碰撞
    if (
        player_x < obstacle_x < player_x + player_size
        and player_y < obstacle_y < player_y + player_size
    ):
        game_over = True

    # 清空視窗
    window.fill(white)

    # 繪製角色
    pygame.draw.rect(window, blue, [player_x, player_y, player_size, player_size])

    # 繪製障礙物
    pygame.draw.rect(window, black, [obstacle_x, obstacle_y, obstacle_size, obstacle_size])

    # 顯示分數
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"分數: {score}", True, black)
    window.blit(score_text, (10, 10))

    # 更新視窗
    pygame.display.flip()

    # 控制更新速率
    clock.tick(60)

pygame.quit()
sys.exit()



