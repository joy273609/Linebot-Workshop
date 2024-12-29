# Azure Speech
import azure.cognitiveservices.speech as speechsdk
# Get Audio Duration
import librosa

import os

speechConfig = speechsdk.SpeechConfig(
    subscription=os.getenv("AZURE_SPEECH_API_KEY"), 
    region=os.getenv("AZURE_SPEECH_API_REGION")
)
audioOutputConfig = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

def azure_text_to_speech(translated_text):
    # The language of the voice that speaks.
    speechConfig.speech_synthesis_voice_name='en-US-AndrewMultilingualNeural'

    file_config = speechsdk.audio.AudioOutputConfig(filename='speech.wav')
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speechConfig, audio_config=file_config)

    # Receives a text from console input and synthesizes it to wave file.
    result = speech_synthesizer.speak_text_async(translated_text).get()

    # Check result
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}], and the audio was saved to [{}]".format(translated_text, 'speech.wav'))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

azure_text_to_speech("Hello, World!")
duration = int(librosa.get_duration(path='speech.wav') * 1000)
print(f"Duration: {duration} ms")