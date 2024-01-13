import pygame
import numpy as np
from math import inf


def is_valid_move_position(board, row, col):
    return board[row][col] == 0


def render_board(screen, board, AI_cir_image, human_cross_image, cell_size, margin):
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                screen.blit(
                    AI_cir_image,
                    ((col * cell_size) + margin, (row * cell_size) + margin),
                )
            elif board[row][col] == -1:
                screen.blit(
                    human_cross_image,
                    ((col * cell_size) + margin, (row * cell_size) + margin),
                )


def check_win(state, player):
    for row in state:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(state[row][col] == player for row in range(3)):
            return True

    if all(state[i][i] == player for i in range(3)) or all(
        state[i][2 - i] == player for i in range(3)
    ):
        return True

    return False


def is_game_over(state):
    return check_win(state, 1) or check_win(state, -1)


def evaluate_board(state):
    if check_win(state, 1):
        return 1
    elif check_win(state, -1):
        return -1
    else:
        return 0


def get_empty_cells(board):
    cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                cells.append([row, col])
    return cells


def render_game_message(
    screen, msg, font, text_color, background_color, screen_width, screen_height
):
    text = font.render(msg, True, text_color, background_color)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)


def minimax_algorithm(state, depth, player):
    if player == 1:
        best = [-1, -1, -inf]
    else:
        best = [-1, -1, inf]

    if is_game_over(state) or depth == 0:
        score = evaluate_board(state)
        return [-1, -1, score]

    for cell in get_empty_cells(state):
        row, col = cell
        state[row][col] = player
        score = minimax_algorithm(state, depth - 1, -player)
        state[row][col] = 0
        score[0], score[1] = row, col

        if player == 1:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best
