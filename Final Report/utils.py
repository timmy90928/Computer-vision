# utils.py 2023-12-24
# Copyright © 2023 WeiWen Wu  

from matplotlib import pyplot as plt
import cv2 
from typing import Literal,Union,Optional
from numpy import ndarray

class plot_from_matplotlib:
    """
    Make pictures from matplotlib.

    # Example
    ```
    plot = plot_from_matplotlib("title")
    plot.col_row = (2,2)
    plot.save = True
    plot("Original",img)
    plot_from_matplotlib.show()
    ```
    """
    n:int=1
    col_row:tuple[int,int]
    save:bool=False
    def __init__(self,name:str) -> None:
        fig = plt.figure()
        fig.canvas.manager.window.setWindowTitle(name)
        fig.tight_layout()
        # fig.subplots_adjust(top=0.95, bottom=0.05, left=0.0, right=1.0)
        self.fig = fig

    def __call__(self,name:str,dst,cmap:str='gray',save:bool=0):     # Make pictures.
        n = self.n
        col,row = self.col_row
        path = __file__.split("\\")[-2]
        plt.subplot(row,col,n), plt.imshow(dst,cmap), plt.title(name)
        plt.xticks([]), plt.yticks([])  # Do not show scale.
        if save or self.save: cv2.imwrite(f"./{path}/{name}.png",dst,[int(cv2.IMWRITE_PNG_COMPRESSION),0])
        self.n+=1

    # @staticmethod
    def show(self):
        """Display image."""
        self.fig.tight_layout()
        plt.show()
    
    @staticmethod
    def show():
        """Display image."""
        plt.show()

class histogram:
    """
    Imgage Histogram - Find, Plot and Analyze
    It which gives you an overall idea about the intensity distribution of an image.
    It distribute data along x and y axis.
    x - axis contain range of color vlaues.
    y - axis contain numbers of pixels in an image.
    With histogram to extrct information about contast, brigthness and intensity etc.
    plot histomgram using matplotlib

    # Example
    ```
    hist = histogram()
    histogram.plot(hist.calhist())
    imshow("hist",hist.equalization())
    ```
    """
    def __init__(self,img:Union[str,ndarray]="lena.jpg") -> None:
        if isinstance(img,str):
            img = cv2.imread(img)
            img = bgr2gray(img)
        self.img = img
        
        # img = cv2.resize(img,(500,650))
    
    @staticmethod
    def plot(img:ndarray):
        fig = plt.figure()
        fig.canvas.manager.window.setWindowTitle("Histogram")
        plt.plot(img)
        plt.show()

    def calhist(self,show_hist:bool=False) -> ndarray:
        """Plotting with calhist method."""
        # It accept parameters like ([img],[channel],mask,[histsize],range[0-255]).
        hist = cv2.calcHist([self.img], [0], None, [256], [0, 256])
        if show_hist: histogram.plot(hist)
        return hist

    def plot_bgr_hist(self):
        b, g, r = cv2.split(self.img)
        #cv2.imshow("img", img)
        # cv2.imshow("b", b)
        # cv2.imshow("g", g)
        # cv2.imshow("r", r)
        #Plotting different channel with hist
        plt.hist(b.ravel(), 256, [0, 256])
        plt.hist(g.ravel(), 256, [0, 256])
        plt.hist(r.ravel(), 256, [0, 256])
        plt.title("ColorFull Image")
        plt.show()

    def equalization(self) -> ndarray:
        """Histogram equalization is good when  of the image is confined to a particular region."""
        img_gray = self.img
        equ = cv2.equalizeHist(img_gray)
        # res = hstack((img_gray,equ)) #stacking images side-by-side
        return equ


def imshow(title:str,img:ndarray):
    """Show image."""
    cv2.imshow(title,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def bgr2gray(img:Union[str,ndarray],blur:bool=False) -> ndarray:
    """Convert bgr to gray and remove noise points."""
    if isinstance(img,str):img = cv2.imread(img)    # Read image.
    
    if blur:
        img = cv2.GaussianBlur(img, (3, 3),0)   # GaussianBlur
        img = cv2.medianBlur(img, 3)            # Median Filtering
        img = cv2.GaussianBlur(img, (3, 3),0)   # GaussianBlur
        img = cv2.medianBlur(img, 3)            # Median Filtering

    return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # BGR to gray.

def plot_histogram(img:ndarray) -> None:
    """Plot histogram."""
    fig = plt.figure()
    fig.canvas.manager.window.setWindowTitle("Histogram")
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.show()

def canny(img:ndarray,min:int=0,max:int=255) -> ndarray:
    """cv2.Canny (input gray)"""
    return  cv2.bitwise_not(cv2.Canny(bgr2gray(img),min,max))
    
def canny_edge(img:ndarray) -> tuple[int,int]:
    """Test Canny upper and lower values."""
    cv2.namedWindow("Canny")

    ### Create a track bar ### cv2.createTrackbar('Slider name', 'window name', min, max, fn)
    cv2.createTrackbar("minimum", "Canny", 0, 255, lambda _:_) 
    cv2.createTrackbar("maximum", "Canny", 0, 255, lambda _:_) 
    cv2.setTrackbarPos("minimum", "Canny", 0)
    cv2.setTrackbarPos("maximum", "Canny", 255)
    
    while True:
        ### Get trackbar position. ### cv2.setTrackbarPos('Slider name', 'window name', default)
        min= cv2.getTrackbarPos('minimum','Canny')
        max= cv2.getTrackbarPos('maximum','Canny')
        
        cv2.imshow("Canny",canny(img,min,max))
        key = cv2.waitKey(1)
        if  key == ord('q') or key == 27:
            break

    cv2.destroyAllWindows()
    return min,max

def medianBlur(img) -> ndarray:return cv2.medianBlur(img, 3)
def GaussianBlur(img) -> ndarray: return cv2.GaussianBlur(img, (3, 3),0)