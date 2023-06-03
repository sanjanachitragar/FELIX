import speech_recognition as sr
import wave
def get_command():
    rec = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 3
        audio = rec.listen(source, timeout=2, phrase_time_limit=5)
        print("Processing...")

    # Save the audio to a WAV file
    with wave.open("output.wav", "wb") as file:
        file.setnchannels(4)  # Mono channel
        file.setsampwidth(2)  # 2 bytes per sample
        file.setframerate(11000)  # Sample rate of 16 kHz
        file.writeframes(audio.get_wav_data())

    return audio

get_command()
