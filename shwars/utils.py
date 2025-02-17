import matplotlib.pyplot as plt
import requests
from PIL import Image
from io import BytesIO
import numpy as np

def display_images(l, titles=None, fontsize=12):
    """
    Display a list of images in a single row.

    Parameters:
    l (list): A list of images to be displayed.
    titles (list, optional): A list of titles corresponding to each image. Defaults to None.
    fontsize (int, optional): The font size for the titles. Defaults to 12.

    Returns:
    None
    """
    n = len(l)
    fig, ax = plt.subplots(1, n)
    for i, im in enumerate(l):
        ax[i].imshow(im)
        ax[i].axis('off')
        if titles is not None:
            ax[i].set_title(titles[i], fontsize=fontsize)
    fig.set_size_inches(fig.get_size_inches() * n)
    plt.tight_layout()
    plt.show()

# load image from url
def image_from_url(url):
    """
    Loads an image from a URL.

    Parameters:
    url (str): The URL of the image to be loaded.

    Returns:
    PIL.Image.Image: The loaded image.
    """
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

def image_resize(img, size, keep_aspect=True):
    """
    Resizes an image to a specified size.

    Parameters:
    img (PIL.Image.Image): The image to be resized.
    size (int or tuple): The size to which the image should be resized. If an integer is provided, the image will be resized to a square of that size. If a tuple is provided, the image will be resized to the specified width and height.
    keep_aspect (bool): If True, the aspect ratio of the image will be preserved. If False, the image will be resized to the exact dimensions specified, potentially distorting the aspect ratio.

    Returns:
    numpy.ndarray: The resized image as a numpy array.
    """
    if isinstance(size, int):
        w, h = size, size
    else:
        w, h = size
    if keep_aspect:
        img.thumbnail((w, h), Image.LANCZOS)
        img = np.array(img)
        x = np.zeros((h, w, 3), dtype=img.dtype)
        x[:img.shape[0], :img.shape[1], :] = img
        return x
    else:
        img = img.resize((w, h), Image.LANCZOS)
        return np.array(img)
