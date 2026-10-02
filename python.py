from gtts import gTTS
text = "hi everyone welcome to my id,developer dot yuvraj"
tts = gTTS(text = text,lang = 'en')

tts.save("p.mp3")

print("speech saved as p.mp3")






