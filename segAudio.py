from pydub import AudioSegment


music = AudioSegment.from_wav('./audio/v2.wav')

out_wav = music[3*1000:8*1000]
out_wav.export(out_f='./audio/v2_short.wav')
