import speech_recognition as sr
import os

def recognize_speech_from_file(file_path):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    print(f"Processing audio file: {file_path}...")

    # Load the audio file
    with sr.AudioFile(file_path) as source:
        # Record the audio data
        audio_data = recognizer.record(source)

        try:
            # Using google speech recognition
            print("Recognizing text...")
            text = recognizer.recognize_google(audio_data)
            print("-" * 30)
            print("Recognized Text:")
            print(text)
            print("-" * 30)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    # Path to the wav file
    audio_file = "the quick brown fox .wav"
    recognize_speech_from_file(audio_file)