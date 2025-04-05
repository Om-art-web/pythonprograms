import cv2
import numpy as np

def om_edge_detection(image_path):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        print("Error: Could not open or find the image.")
        return
    
    # Apply Sobel filter in X and Y direction
    om_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    om_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    
    # Compute the gradient magnitude
    om_magnitude = np.sqrt(om_x**2 + om_y**2)
    om_magnitude = np.uint8(255 * om_magnitude / np.max(om_magnitude))
    
    # Display results
    cv2.imshow('Original Image', image)
    
    cv2.imshow('Om Magnitude', om_magnitude)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = 'images/Whi.jpg'  # Change this to your image file path
om_edge_detection(image_path)