# Video Scrapper
This is a scrapper that uses PyTube and OpenAI Whisper. 

## File structure
```
Scrapper/
    |-- scrap_data.ipynb
    |-- Data.json
    |-- DrK.videos.csv
```

## Getting Started 
### Enviroment 
install Pytube 
```
pip install pytube
```

In a PyTorch env
```
pip install git+https://github.com/openai/whisper.git
```

### Scrapping location 

To scrap data, we created the ```Data.json``` file.
```json 
{
    "playlists": [
        {"Exploring your questions!":"https://www.youtube.com/playlist?list=PLYxtGyYUCbEHQVvJxcDFNAQswRDt4Rqgm"},
        {"Overcome the Loneliness Epidemic":"https://www.youtube.com/playlist?list=PLYxtGyYUCbEGYMo1tsf_q9NqGPrrzoqB0"},
        {"Survive and thrive in today's world!":"https://www.youtube.com/playlist?list=PLYxtGyYUCbEHePxU2X16q-MfWSpZjgDUz"},
        {"Best Lectures":"https://www.youtube.com/playlist?list=PLYxtGyYUCbEHA10I_hGYOxZW0nJTwIc_9"},
        {"Dating and Relationships":"https://www.youtube.com/playlist?list=PLYxtGyYUCbEF-Tlt8TUO-_M5ijkIqzc0C"},
        {"Motivation":"https://www.youtube.com/playlist?list=PLYxtGyYUCbEEHstX_Ya9K1C_n5GYiKDCX"},
        {"Sexuality and Porn":"https://www.youtube.com/playlist?list=PLYxtGyYUCbEEcbuWAXjOsqp8iB0Lf3K8_"},
        {"Anxiety":"https://www.youtube.com/playlist?list=PLYxtGyYUCbEGFt9XAJ4gro3LGNrgpkxVC"},
        {"Depression":"https://www.youtube.com/playlist?list=PLYxtGyYUCbEG3QKCGHFUNhragkTe588Uc"},
        {"Meditation":"https://www.youtube.com/playlist?list=PLYxtGyYUCbEFLejo3Hv1LLL1GX0fNpmcM"}
    ]
}
```








