import streamlit as st
import matplotlib.pyplot as plt
from colorthief import ColorThief
import colorsys
from webcolors import hex_to_rgb
import matplotlib
import webcolors
import numpy as np

# Function to find the closest color match
def closest_color(rgb):
    differences = {}
    for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
        r, g, b = hex_to_rgb(color_hex)
        differences[sum([(r - rgb[0]) ** 2, (g - rgb[1]) ** 2, (b - rgb[2]) ** 2])] = color_name
    return differences[min(differences.keys())]

# Streamlit app
def main():
    st.title("Color Analysis with Streamlit")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Plotting Image
        image = matplotlib.image.imread(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Extracting 5 dominant colors
        ct = ColorThief(uploaded_file)
        palette = ct.get_palette(color_count=5)[:10]

        # Extracting the dominant color after displaying the uploaded image
        dominant_color = ct.get_color(quality=1)

        # Displaying the dominant color
        st.subheader("Dominant Color")
        dominant_color_array = np.full((100, 100, 3), dominant_color, dtype=np.uint8)
        st.image(dominant_color_array, caption="Dominant Color", use_column_width=True)

        # Displaying the color palette
        st.subheader("Color Palette")
        # Create a visualization of the color palette (e.g., using matplotlib)
        # ...

        # Displaying the color codes and information
        st.subheader("Color Information")
        for i, color in enumerate(palette):
            st.write(f"Color {i + 1}")
            st.write(f"RGB: {color}")
            st.write(f"Hex: #{color[0]:02x}{color[1]:02x}{color[2]:02x}")
            st.write(f"HSV: {colorsys.rgb_to_hsv(*color)}")
            st.write(f"HLS: {colorsys.rgb_to_hls(*color)}")
            st.write("---")

        # Finding the closest match
        st.subheader("Closest Color Match")
        try:
            cname = webcolors.rgb_to_name(dominant_color)
            st.write(f"The color is exactly {cname}")
        except ValueError:
            closest = closest_color(dominant_color)
            st.write(f"The color is closest to {closest}")

if __name__ == "__main__":
    main()

#cd "C:\Users\Arsh Electricals\Desktop\ENGE\7th_SEM\Mini_Project\New_folder\Frontend"

#streamlit run "C:\Users\Arsh Electricals\Desktop\ENGE\7th_SEM\Mini_Project\New_folder\Frontend\color_analysis_app.py"

#python "C:\Users\Arsh Electricals\Desktop\ENGE\7th_SEM\Mini_Project\New_folder\Frontend\color_analysis_app.py"
