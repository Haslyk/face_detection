from PIL import Image, ImageDraw
import os

def draw_faces(image_array, face_locations, matches, distances, names, tolerance=0.6):
    pil_image = Image.fromarray(image_array)
    draw = ImageDraw.Draw(pil_image)

    for (top, right, bottom, left), match, distance, name in zip(face_locations, matches, distances, names):
        if match and distance <= tolerance:
            draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0), width=3)
            text = f"{name} ({round((1 - distance) * 100, 2)}%)"
            draw.text((left, bottom + 5), text, fill=(255, 255, 255))

    return pil_image
