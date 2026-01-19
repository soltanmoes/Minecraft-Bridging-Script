import minescript as ms
from minescript import EventQueue, EventType, KeyEvent
import time
import sys

# Key code for Left Alt (GLFW format, used by Minecraft)
KEY_ALT = 342  # Left Alt key

# Track Alt key state
alt_pressed = False
alt_held = False

# Wait for Alt key press to start using EventQueue
with EventQueue() as q:
    q.register_key_listener()
    
    print("Press Alt to start...")
    while True:
        try:
            # Use timeout to make it non-blocking for checking
            event = q.get(timeout=0.1)
            if event.type == EventType.KEY and event.key == KEY_ALT:
                if event.action == 1:  # Key pressed
                    alt_pressed = True
                    break
        except:
            # Timeout - continue waiting
            pass
        time.sleep(0.01)

ms.player_press_sneak(True)

# Wait until not targeting up or down
while ms.player_get_targeted_block().side in ("up", "down"):
    time.sleep(0.001)

# Get target block and calculate movement direction
target = ms.player_get_targeted_block()
side = target.side
axis = 2 if side in ("north", "south") else 0
delta = -1 if side in ("north", "west") else 1
prev = ms.player_position()[axis]
print("Started - Hold Alt to continue, release to stop")

# Main loop - runs while Alt key is held
with EventQueue() as q:
    q.register_key_listener()
    alt_held = True
    
    while alt_held:
        # Check for key events (non-blocking with timeout)
        try:
            event = q.get(timeout=0.01)
            if event.type == EventType.KEY and event.key == KEY_ALT:
                if event.action == 0:  # Key released
                    alt_held = False
                    break

        except:
            # Timeout - continue with main logic
            pass
        
        x, y, z = ms.player_position()
        curr = (x, y, z)[axis]
        
        if int(curr) == int(prev + delta):
            ms.player_press_sneak(True)
            while alt_held:
                # Check for Alt release during inner loop
                try:
                    event = q.get(timeout=0.01)
                    if event.type == EventType.KEY and event.key == KEY_ALT:
                        if event.action == 0:  # Key released
                            alt_held = False
                            break
                except:
                    pass
                
                if not alt_held:
                    break
                    
                time.sleep(0.01)
                x2, y2, z2 = ms.player_position()
                curr2 = (x2, y2, z2)[axis]
                
                if int(curr2) != int(prev + delta):
                    break
                
                t = ms.player_get_targeted_block()
                
                if t and t.distance < 2 and t.side not in ("up", "down"):
                    ms.player_press_use(True)
                    ms.player_press_use(False)
                    ms.player_press_sneak(False)
                    break
        
        prev = curr
        time.sleep(0.01)

ms.player_press_sneak(False)
print("Stopped")