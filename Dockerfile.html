# ၁။ ပေါ့ပါးပြီး တည်ငြိမ်တဲ့ Python Version ကို အခြေခံအဖြစ် သုံးမယ်
FROM python:3.10-slim

# ၂။ Linux update လုပ်ပြီး ဗီဒီယို/အသံ ပေါင်းစပ်ဖို့ လိုအပ်တဲ့ ffmpeg ကို သွင်းမယ်
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# ၃။ Server ထဲက ပင်မအလုပ်လုပ်မယ့် ပတ်ဝန်းကျင် (Directory) ကို သတ်မှတ်မယ်
WORKDIR /code

# ၄။ လိုအပ်တဲ့ Library စာရင်း (requirements.txt) ကို အရင်ကူးပြီး သွင်းမယ်
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# ၅။ ကျန်တဲ့ ဖိုင်အားလုံး (app.py နဲ့ cookies.txt) ကို ကူးထည့်မယ်
COPY . .

# ၆။ YouTube ကောင်းကောင်းအလုပ်လုပ်ဖို့ Cookie ဖိုင်ကို ဆာဗာက ဖတ်ခွင့်ပေးလိုက်မယ်
RUN chmod 644 /code/cookies.txt

# ၇။ Render ရဲ့ ပတ်ဝန်းကျင်အတိုင်း FastAPI ကို Port 10000 (သို့မဟုတ် Render သတ်မှတ်ချက်) မှာ Run မယ်
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "10000"]
