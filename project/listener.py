#!/usr/bin/env python3
import speech_recognition as sr

def listen(r, m):

    with m as source:
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    response = {
            "success": True,
            "error": None,
            "trasnscription": None
            }
    try:
        response["transcription"] = r.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"
    return response


if __name__ == '__main__':

    #init Recognizer class
    r = sr.Recognizer()

    #list available microphones & find the logitech's index
    mics = sr.Microphone.list_microphone_names()
    for i, v in enumerate(mics):
        if (v.lower()).find('logitech') >= 0:
            index = i
            break

    m = sr.Microphone(device_index=index)


    print(listen(r,m))
    



