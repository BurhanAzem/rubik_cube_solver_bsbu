import cube_status
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)  # Use the appropriate serial port
time.sleep(2)

cube = cube_status.CubeStatus()
controler = control.RubicControler()
# controler.prepare()
current_status = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'
side_to_color = {'U': 'O', 'R': 'B', 'F': 'W', 'D': 'R', 'L': 'G', 'B': 'Y'}  # default side_to_color

moves = ''

def detect():
    global current_status, side_to_color
    current_status, side_to_color = cube.detect_status()


def solve_with_kociemba():
    global current_status, side_to_color, moves
    print(current_status)
    moves = kociemba.solve(current_status).split()
    print(moves)
    current_status = cube.change_status(current_status, moves)
    
    
def optimal_sol():
    detect()
    solve_with_kociemba()

def mid_sol():
    detect()
    solve_with_kociemba()
    
def slow_sol():
    detect()
    solve_with_kociemba()
    
def default_case():
    return "Invalid case"

# Define a dictionary mapping case numbers to functions
switch = {
    'A': optimal_sol,
    'B': mid_sol,
    'C': slow_sol
}

def main():
    global current_status, side_to_color, moves
    default_side_to_color = {'U': 'O', 'R': 'B', 'F': 'W', 'D': 'R', 'L': 'G', 'B': 'Y'}
    cube = cube_status.CubeStatus()
    moves = []
    while True:
        command = ser.readline()
        if command:
            fun = switch.get(command, default_case)
            fun()
        command = None

if __name__ == "__main__":
    main()


