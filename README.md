# Transcluent
Convert photographed objects to transcluent images automaticly. You need multiple Photos with different backgrounds.

The script bw_to_rgba.py converts two images to a new transcluent image.
It interprets the input-images as if they are made with a black and a white image.

   black     white
   [RGB]     [RGB]
     ||       ||
     \/       \/
    bw_to_rgba.py
          ||
          \/
      transcluent
        [RGBA]
