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
        # Link ထဲကနေ ဗီဒီယို ID ၁၁ လုံးကို ဆွဲထုတ်ခြင်း
        video_id = url.split("v=")[-1].split("&")[0].split("/")[-1].split("?")[0]
        
        # YouTube ရဲ့ Player API ဆီကနေ ဒေတာ တိုက်ရိုက်တောင်းခြင်း
        data = client.player(video_id)
        
        streaming_data = data.get("streamingData", {})
        formats = streaming_data.get("formats", []) + streaming_data.get("adaptiveFormats", [])
        
        # ရနိုင်တဲ့ Link တွေထဲက ပထမဆုံးအဆင်ပြေတဲ့ Link ကို ယူမယ်
        download_link = ""
        for f in formats:
            if "url" in f:
                download_link = f["url"]
                break
                
        title = data.get("videoDetails", {}).get("title", "Unknown Title")
        
        return {
            "status": "success",
            "title": title,
            "download_link": download_link
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
