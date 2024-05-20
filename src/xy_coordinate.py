import cv2

# Global variables to store the coordinates of the two clicks
start_point = None
end_point = None

def Capture_Event(event, x, y, flags, params):
    global start_point, end_point

    if event == cv2.EVENT_LBUTTONDOWN:

        if start_point == None and end_point == None:
            start_point = (x, y)
            end_point = None
        elif start_point != None and end_point == None:
            end_point = (x, y)
            width = abs(end_point[0] - start_point[0])
            height = abs(end_point[1] - start_point[1])
            print(f"({start_point[0]}, {start_point[1]}, {width}, {height})")
            start_point = None
            end_point = None

            

if __name__ == "__main__":
    # Read the image
    img = cv2.imread('capture_0.jpg', 1)

    # Resize the image to the desired size
    resized_img = cv2.resize(img, (3280, 2464))


    # Show the resized Image
    cv2.imshow('image', resized_img)

    # Set the Mouse Callback function, and call
    # the Capture_Event function.
    cv2.setMouseCallback('image', Capture_Event)

    # Press any key to exit
    cv2.waitKey(0)

    # Destroy all the windows
    cv2.destroyAllWindows()
