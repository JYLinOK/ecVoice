import whisper


def getHanWord(audio_F, model='l'):
    if model == 't':
        Model = whisper.load_model("tiny")  # VRAM  ~= 1GB -> 1-2GB
    elif model == 'b':
        Model = whisper.load_model("base")  # VRAM  ~= 1GB -> 1-2GB
    elif model == 's':
        Model = whisper.load_model("small")  # VRAM  ~= 2GB -> 2-4GB
    elif model == 'm':
        Model = whisper.load_model("medium")  # VRAM  ~= 5GB -> 6-8GB
    elif model == 'l':
        Model = whisper.load_model("large")  # VRAM  ~= 10GB -> >12GB

    Hanzi = Model.transcribe(audio_F, language='zh', verbose=False, initial_prompt="简体")
    return ", ".join([i["text"] for i in Hanzi["segments"] if i is not None])



if __name__ == "__main__":
    audio_F = './extractVoice/1_v1_(Vocals).wav'
    print(f'{getHanWord(audio_F, model="s") = }')