# Transcluent
Converting photographed objects to transcluent images automaticly without cutting out the object by hand. You need multiple Photos with different backgrounds.

##bw_to_rgba.py

The script converts two images to a new transcluent image.
It interprets the input-images as if they are made with a black and a white background.

```
   black     white
   [RGB]     [RGB]
     ||       ||
     \/       \/
    bw_to_rgba.py
          ||
          \/
     transcluent
        [RGBA]
```
