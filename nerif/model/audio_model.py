from pathlib import Path

from openai import OpenAI


class AudioModel:
    """
    A simple agent for audio tasks. (audio transcription, speech to text)
    """

    def __init__(self):
        self.client = OpenAI()

    def transcribe(self, file: Path):
        with open(file, "rb") as audio_file:
            transcription = self.client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
            )
        return transcription


class SpeechModel:
    """
    A simple agent for speech tasks. (speech model, text to speech)
    """

    def __init__(self):
        self.client = OpenAI()

    def text_to_speech(self, text: str, voice: str = "alloy"):
        response = self.client.audio.speech.create(
            model="tts-1",
            input=text,
            voice=voice,
        )
        return response
