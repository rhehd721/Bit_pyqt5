from gtts import gTTS

tts_en = gTTS(text=text, lang='en')
tts_kr = gTTS(text='안녕하세요',lang='ko')

f = open(tempFileName,'wb')             
tts_en.write_to_fp(f)    # 영어로 네번 말하고
tts_en.write_to_fp(f)
tts_en.write_to_fp(f)
tts_en.write_to_fp(f)
tts_kr.write_to_fp(f)    # 한글로 한번 말하기
f.close()