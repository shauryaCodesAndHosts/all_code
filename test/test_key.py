from Xlib import X, display, XK

# Connect to the display
d = display.Display()

# Get the root window
root = d.screen().root

# Get the target window's ID (e.g., using xdotool or other methods)
window_id = your_window_id

# Get the target window
window = d.create_resource_object('window', window_id)

# Define the keycodes for the keys "a", "b", "c", and "d"
keycodes = [XK.XK_a, XK.XK_b, XK.XK_c, XK.XK_d]

# Simulate key press events for each key
for keycode in keycodes:
    event_type = X.KeyPress
    event = X.KeyPress
    detail = keycode
    time = X.CurrentTime

    window.send_event(event_type, detail, time, window, 0, 0)
    d.flush()

    event_type = X.KeyRelease
    event = X.KeyRelease

    window.send_event(event_type, detail, time, window, 0, 0)
    d.flush()

