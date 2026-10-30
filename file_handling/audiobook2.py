from pypdf import PdfReader
from gtts import gTTS

reader = PdfReader(r"C:\Users\HP\OneDrive\Documents\Desktop\pythonlife\NumPy.pdf")

text = ""
for page in reader.pages:
    text += page.extract_text() or ""

tts = gTTS(text=text, lang="en")
tts.save("NumPy.mp3")

print("Audio created successfully!")