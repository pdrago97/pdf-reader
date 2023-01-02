import tempfile
import PyPDF3
import streamlit as st
from gtts import gTTS

def pdf_to_speech(pdf_file, audio_file):
    # Write the binary string to a temporary file
    with tempfile.NamedTemporaryFile() as temp:
        temp.write(pdf_file.getvalue())
        temp.flush()
        # Open the PDF file in binary mode
        with open(temp.name, 'rb') as file:
            # Create a PDF reader object
            reader = PyPDF3.PdfFileReader(file)
            # Initialize a list to store the text of all pages
            text = []
            # Get the total number of pages
            total_pages = reader.getNumPages()
            # Iterate over all the pages
            for page in range(total_pages):
                # Extract the text from the page
                text.append(reader.getPage(page).extractText())
            # Join all the pages into a single string
            text = '\n'.join(text)
            # Convert the text to speech
            tts = gTTS(text)
            # Set the audio file generation as a task
            with st.spinner('Generating audio file...'):
                # Write the audio data to the file
                tts.write_to_fp(audio_file)
            # Close the audio file
            audio_file.close()


# Create a main function
def main():
    # Set the page title
    st.title('PDF to Audio')
    # Add a file uploader widget
    pdf_file = st.file_uploader('Upload a PDF file')
    # Check if a file was uploaded
    if pdf_file is not None:
        # Open an audio file in write mode
        with open('output.mp3', 'wb') as audio_file:
            # Convert the PDF to speech
            pdf_to_speech(pdf_file, audio_file)
        # Embed an audio player
        st.audio('output.mp3')

        
# Run the main function
if __name__ == '__main__':
    main()
