import librosa.display
import matplotlib.pyplot as plt
import numpy as np

audio_file = '/content/WhatsApp Audio 2024-03-04 at 11.27.40_69e1065f.mp3'  # Replace with the actual path to your audio file

# Load the audio file using librosa
audio_data, sample_rate = librosa.load(audio_file, sr=None)

# Compute the spectrogram using librosa
spectrogram = librosa.feature.melspectrogram(y=audio_data, sr=sample_rate, n_fft=1024, hop_length=512, n_mels=128)

# Convert to decibels (log scale)
spectrogram_db = librosa.power_to_db(spectrogram, ref=np.max)

# Plot the spectrogram
plt.figure(figsize=(10, 4))
librosa.display.specshow(spectrogram_db, sr=sample_rate, hop_length=512, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram of the Audio Signal')
plt.show()
