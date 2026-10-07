from pico2d import *


# 화면 및 캐릭터 설정 상수
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
CHARACTER_WIDTH, CHARACTER_HEIGHT = 100, 100
SPEED = 5

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running, dir_x

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1


running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dir_x = 0
hide_cursor()


while running:
    clear_canvas()

    # fill here
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)


    update_canvas()
    handle_events()
    x += dir_x * SPEED
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()




