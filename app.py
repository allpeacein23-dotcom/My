from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from innertube import InnerTube

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

client = InnerTube("WEB")

@app.get("/download")
def download(url: str = None):
    if not url: return {"status": "error", "message": "No URL"}
    try:
        # Link ထဲကနေ ဗီဒီယို ID ဆွဲထုတ်ခြင်း
        video_id = url.split("v=")[-1].split("&")[0].split("/")[-1].split("?")[0]
        data = client.player(video_id)
        
        # Video Details ယူခြင်း
        video_details = data.get("videoDetails", {})
        title = video_details.get("title", "YouTube Video")
        thumbnail = video_details.get("thumbnail", {}).get("thumbnails", [{}])[-1].get("url", "")
        
        # Streaming Data ထဲက Link တွေကို လိုက်ရှာခြင်း
        streaming_data = data.get("streamingData", {})
        formats = streaming_data.get("formats", []) + streaming_data.get("adaptiveFormats", [])
        
        download_link = ""
        
        # ပထမဆုံးအဆင့်: တိုက်ရိုက် 'url' ပါတဲ့ format ကို အရင်ရှာမယ်
        for f in formats:
            if "url" in f and f.get("url"):
                download_link = f["url"]
                break
        
        # ဒုတိယအဆင့်: အကယ်၍ url တိုက်ရိုက်မပါရင် signatureCipher ထဲက လိုက်ခွဲထုတ်မယ်
        if not download_link:
            for f in formats:
                if "signatureCipher" in f or "cipher" in f:
                    cipher = f.get("signatureCipher", f.get("cipher", ""))
                    import urllib.parse
                    cipher_data = urllib.parse.parse_qs(cipher)
                    if "url" in cipher_data:
                        download_link = cipher_data["url"][0]
                        break

        if not download_link:
            return {"status": "error", "message": "Could not extract download link."}
            
        return {
            "status": "success",
            "title": title,
            "thumbnail": thumbnail,
            "download_link": download_link
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
