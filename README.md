# Lamp Visualizer
Inspired by [Mattbatwings](https://www.youtube.com/c/Mattbatwings)

## Usage
This is the code you will need to get started:
```py
from lamp_visualizer import LampVisualizer as LP

LP.init(900, 600) # width, height

# Toggle the 20th lamp the X axis and the 30th lamp on the Y axis
# ! MEASUREMENT IS NOT IN PIXELS !
LP.toggle(20, 30)

LP.run()
```