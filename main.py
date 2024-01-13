from pygame.locals import QUIT, MOUSEBUTTONDOWN
from settings import *
from utils import *
import sys


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            row = y // CELL_SIZE
            col = x // CELL_SIZE

            if is_valid_move_position(board, row, col):
                board[row][col] = -1
                depth = len(get_empty_cells(board))
                AI_move = minimax_algorithm(board, depth, AI)
                row, col = AI_move[0], AI_move[1]
                board[row][col] = 1

    screen.blit(bg_image, (0, 0))
    render_board(screen, board, AI_cir_image, human_cross_image, CELL_SIZE, MARGIN)
    pygame.display.update()

    if is_game_over(board):
        if evaluate_board(board) == 1:
            render_game_message(
                screen,
                "  AI won with MINMAX!  ",
                game_font,
                white,
                blue,
                SCREEN_WIDTH,
                SCREEN_HEIGHT,
            )
        else:
            render_game_message(
                screen,
                "  You won!  ",
                game_font,
                white,
                blue,
                SCREEN_WIDTH,
                SCREEN_HEIGHT,
            )

        pygame.display.update()
        pygame.time.delay(3000)
        board = np.zeros((3, 3))

    if len(get_empty_cells(board)) == 0 and evaluate_board(board) == 0:
        render_game_message(
            screen,
            "  It's a draw  ",
            game_font,
            white,
            blue,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
        )
        pygame.display.update()
        pygame.time.delay(3000)
        board = np.zeros((3, 3))
