from pico2d import *


# 화면 및 캐릭터 설정 상수
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
CHARACTER_WIDTH, CHARACTER_HEIGHT = 100, 100
SPEED = 5

# 스프라이트 시트 액션별 bottom y좌표 상수
ACTION_RUN_RIGHT = 100
ACTION_RUN_LEFT = 0
ACTION_IDLE_RIGHT = 200
ACTION_IDLE_LEFT = 300

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def clamp(val, min_val, max_val):
    return max(min_val, min(val, max_val))


def handle_events():
    global running, dir_x, dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dir_x = 0
dir_y = 0
look_dir = 1  # 1: 우측, -1: 좌측
is_moving = False
hide_cursor()


while running:
    action = ACTION_RUN_RIGHT
    if is_moving:
        if look_dir > 0:
            action = ACTION_RUN_RIGHT
        else:
            action = ACTION_RUN_LEFT

    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * CHARACTER_WIDTH, action, CHARACTER_WIDTH, CHARACTER_HEIGHT, x, y)

    update_canvas()
    handle_events()
    x += dir_x * SPEED
    y += dir_y * SPEED

    # 시선 방향 갱신: 좌우 이동 시 변경, 상하 이동 시에는 직전 좌우 시선(look_dir) 유지
    if dir_x > 0:
        look_dir = 1
    elif dir_x < 0:
        look_dir = -1
    # dir_x == 0인 경우(상하 이동 또는 정지) 기존 look_dir 유지

    # 이동 여부 판별 (IDLE 상태 또는 이동 애니메이션 결정)
    is_moving = (dir_x != 0 or dir_y != 0)

    # 화면 경계 제한 (clamp 함수 적용)
    half_w = CHARACTER_WIDTH // 2
    half_h = CHARACTER_HEIGHT // 2
    x = clamp(x, half_w, TUK_WIDTH - half_w)
    y = clamp(y, half_h, TUK_HEIGHT - half_h)

    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()




