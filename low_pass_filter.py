import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, filtfilt

import librosa

audio_file_path = 'WhatsApp Audio 2024-03-04 at 11.27.40_69e1065f.wav'
audio_data, sample_rate = librosa.load(audio_file_path, sr=None)


# Define the cutoff frequency for the low-pass filter (in Hz)
cutoff_frequency = 200  # Adjust this value according to your needs

# Design a low-pass Butterworth filter
order = 4  # Filter order
b, a = butter(order, cutoff_frequency, btype='low', fs=sample_rate)

# Apply the filter to the audio data
filtered_audio_data = filtfilt(b, a, audio_data)

# Plot the original and filtered signals
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(np.arange(len(audio_data)) / sample_rate, audio_data)
plt.title('Original Audio Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(np.arange(len(filtered_audio_data)) / sample_rate, filtered_audio_data)
plt.title('Filtered Audio Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
