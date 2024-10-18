from settings import *


pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
IMAGE = pygame.image.load('assets/image.jpg').convert()

def detect_collision(dx, dy, ball, rect):
    # ? Horizontal collisions
    if dx > 0: 
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    
    # ? Vertical collisions
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top
    
    # ? Diagonal collisions
    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx 
        
    return dx, dy

# * MAIN LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    SCREEN.blit(IMAGE, (0, 0))
            
    # * DRAW THE OBJECTS
    [pygame.draw.rect(SCREEN, COLOR_LIST[color], BLOCK) for color, BLOCK in enumerate(BLOCK_LIST)]
    pygame.draw.rect(SCREEN, pygame.Color('#e55381'), PADDLE)
    pygame.draw.circle(SCREEN, pygame.Color('#fcf300'), BALL.center, BALL_RADIUS)
    
    # * BALL MOVE
    BALL.x += BALL_SPEED * DX
    BALL.y += BALL_SPEED * DY
    
    ### * BALL COLLISIONS
    ### * Left right
    if BALL.centerx < BALL_RADIUS or BALL.centerx > WIDTH - BALL_RADIUS:
        DX = -DX 
    ### * top
    if BALL.centery < BALL_RADIUS:
        DY = -DY
    ### * Paddle
    if BALL.colliderect(PADDLE) and DY > 0:
        DX, DY = detect_collision(DX, DY, BALL, PADDLE)
    ### * Blocks
    hit_index = BALL.collidelist(BLOCK_LIST)
    if hit_index != -1:
        hit_rect = BLOCK_LIST.pop(hit_index)
        hit_color = COLOR_LIST.pop(hit_index)
        DX, DY = detect_collision(DX, DY, BALL, hit_rect)
        # ? SPECIAL EFFECT
        hit_rect.inflate_ip(BALL.width * 3, BALL.height * 3)
        pygame.draw.rect(SCREEN, hit_color, hit_rect)
        FPS += 1
    
    # * WIN OR GAME OVER
    if BALL.bottom > HEIGHT:
        print("GAME OVER !!!")
        exit()
    elif not len(BLOCK_LIST):
        print("WIN !!!")
        exit()
    
    # * CONTROL THE PADDLE
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and PADDLE.left > 0:
        PADDLE.left -= PADDLE_SPEED
    if key[pygame.K_RIGHT] and PADDLE.right < WIDTH:
        PADDLE.right += PADDLE_SPEED
            
    # * UPDATE SCREEN
    pygame.display.flip()
    CLOCK.tick(FPS)