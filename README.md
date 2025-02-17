# shwarsutils

Miscellaneous Python utilities by Dmitri Soshnikov, to be used in demos.

## Installation

```
pip install shwarsutils
```

## Usage

```
from shwars.utils import *

img = image_from_url("https://soshnikov.com/images/official/shwars_studio.jpg")
img = image_resize(img, 1024, keep_aspect=True)
display_images([img,img])
```


