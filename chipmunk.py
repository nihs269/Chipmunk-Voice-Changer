import librosa
import soundfile


def chipmunk_audio(audio_path: str, save_chipmunk_path: str, level: float):
    data, sr = librosa.load(audio_path)
    new_data = librosa.effects.pitch_shift(data, sr=sr, n_steps=level)
    soundfile.write(save_chipmunk_path, new_data, int(sr))
