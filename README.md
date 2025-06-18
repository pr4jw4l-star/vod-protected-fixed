# VOD-Only IPTV Playlist Host with Password Protection

This Flask app combines your IPTV Movies + Series M3U playlists and serves them as a password-protected `.m3u` endpoint.

## 🌐 Endpoint
After deployment on Render:
```
https://your-app-name.onrender.com/vod.m3u
```

## 🔐 Login
- Username: `Prajwal_07`
- Password: `prajwal@5211134`

## 🛠 Environment Variables
| Key         | Value                                                                 |
|-------------|-----------------------------------------------------------------------|
| `MOVIES_URL`| `http://starshare.fun:80/get.php?username=9833672656&password=5367837776&type=m3u&category_type=movie` |
| `SERIES_URL`| `http://starshare.fun:80/get.php?username=9833672656&password=5367837776&type=m3u&category_type=series` |

## 🚀 Deploy to Render
1. Push this code to a GitHub repo
2. Go to [https://render.com](https://render.com)
3. Click "New Web Service" > "Deploy from GitHub"
4. Set:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
   - Runtime: Python 3
5. Add environment variables above
6. Done!
