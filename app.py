



        import streamlit as st

import qrcode

def generate_qr_code(data, image_size=200):

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

    qr.add_data(data)

    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")

    qr_image = qr_image.resize((image_size, image_size))

    return qr_image

def main():

    st.title("QR Code Maker")

    # User input for the data

    data = st.text_input("Enter the data to encode into QR code")

    # Generate QR code

    if st.button("Generate QR Code"):

        if data:

            qr_image = generate_qr_code(data)

            st.image(qr_image, caption="QR Code", use_column_width=True)

        else:

            st.warning("Please enter the data to encode")

if __name__ == "__main__":

    main()
