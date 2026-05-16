from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yt_dlp

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/download")
def download(url: str = None):
    if not url: 
        return {"status": "error", "message": "No URL provided"}
    
    try:
        # yt-dlp အတွက် settings ပြင်ဆင်ခြင်း
        ydl_opts = {
            'format': 'best',  # အသံရော ဗီဒီယိုရော ပါတဲ့ အကောင်းဆုံး format ကို ယူမယ်
            'quiet': True,
            'no_warnings': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # ဗီဒီယိုရဲ့ အချက်အလက်တွေကို လှမ်းယူခြင်း
            info = ydl.extract_info(url, download=False)
            
            title = info.get('title', 'YouTube Video')
            thumbnail = info.get('thumbnail', '')
            download_link = info.get('url', '') # တိုက်ရိုက် ဒေါင်းလုဒ်လင့်ခ်
            
            if not download_link:
                return {"status": "error", "message": "Could not find a direct download link"}
                
            return {
                "status": "success",
                "title": title,
                "thumbnail": thumbnail,
                "download_link": download_link
            }
            
    except Exception as e:
        return {"status": "error", "message": str(e)}
