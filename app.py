import streamlit as st

from PIL import Image

import io

# Function to compress the image

def compress_image(image, quality):

    # Open the image using Pillow

    img = Image.open(image)

    # Create an in-memory buffer to store the compressed image

    img_buffer = io.BytesIO()

    # Save the image to the buffer with the specified quality

    img.save(img_buffer, format='JPEG', quality=quality)

    # Return the compressed image as bytes

    return img_buffer.getvalue()

# Streamlit app

def main():

    st.title("Image Compressor")

    # File uploader

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg"])

    if uploaded_file is not None:

        # Display the uploaded image

        st.image(uploaded_file, caption="Original Image", use_column_width=True)

        # Compression options

        quality = st.slider("Select compression quality", min_value=1, max_value=100, value=50)

        if st.button("Compress"):

            # Compress the image

            compressed_image = compress_image(uploaded_file, quality)

            # Display the compressed image

            st.image(compressed_image, caption="Compressed Image", use_column_width=True)

# Run the app

if __name__ == "__main__":

    main()

