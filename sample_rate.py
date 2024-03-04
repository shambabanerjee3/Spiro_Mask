def get_sample_rate_wav(audio_file_path):
    with open(audio_file_path,'rb') as wav_file:
        wav_file.seek(24)
        sample_rate_bytes=wav_file.read(4)
        sample_rate=int.from_bytes(sample_rate_bytes,byteorder='little')
    return sample_rate

audio_file_path='Breathing_data.wav'

sample_rate=get_sample_rate_wav(audio_file_path)

print(sample_rate)
