from gtts import gTTS

tts = gTTS('Hello, welcome to Python Life', lang='en')
tts.save('hello.mp3')

print("Audio file saved successfully!")
