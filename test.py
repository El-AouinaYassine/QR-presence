import  qrcode

def generateQrCode(sessionId , token):
    if sessionId and token:
        img = qrcode.make(f"https://qrcode/presence?session_id={sessionId}&token={token}")
        return img
    else:
        return 0


