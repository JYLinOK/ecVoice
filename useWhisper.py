import whisper


def getHanWord(audio_F, model='l'):
    if model == 't':
        Model = whisper.load_model("tiny")  # tiny ~= 1GB -> 1-2GB
    elif model == 'b':
        Model = whisper.load_model("base")  # tiny ~= 1GB -> 2-4GB
    elif model == 's':
        Model = whisper.load_model("small")  # tiny ~= 2GB -> 4-6GB
    elif model == 'm':
        Model = whisper.load_model("medium")  # tiny ~= 5GB -> 6-8GB
    elif model == 'l':
        Model = whisper.load_model("large")  # tiny ~= 5GB -> >12GB

    Hanzi = Model.transcribe(audio_F, language='zh', verbose=False, initial_prompt="简体")
    return ", ".join([i["text"] for i in Hanzi["segments"] if i is not None])



if __name__ == "__main__":
    audio_F = './extractVoice/1_v1_(Vocals).wav'
    print(f'{getHanWord(audio_F, model="s") = }')