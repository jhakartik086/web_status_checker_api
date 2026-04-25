# 🌐 Website Status Checker

A simple and efficient Python project that checks whether a website is **UP or DOWN** using HTTP requests.

This project is perfect for beginners learning Python, APIs, and automation.

---

## 🚀 Features

- ✅ Check if a website is online or offline
- ⚡ Fast response using HTTP requests
- 🌍 Supports any website URL
- 📊 Displays HTTP status codes
- 🧠 Beginner-friendly and easy to understand

---

## 🧠 How It Works

The script sends an HTTP GET request to a website:

- **200 OK** → Website is UP ✅  
- **Other status codes** → Website might have issues ⚠️  
- **Error / Timeout** → Website is DOWN ❌  

---

## 🛠️ Technologies Used

- Python 3
- requests library

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/jhakartik086/website-status-checker.git
2. Open project folder
cd website-status-checker
3. Install required library
pip install requests
▶️ Usage

Run the script:

python main.py
💻 Example Code
import requests

def check_website(url):
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print(f"{url} is UP ✅")
        else:
            print(f"{url} returned status code {response.status_code} ⚠️")

    except requests.exceptions.RequestException:
        print(f"{url} is DOWN ❌")


# Example usage
check_website("https://www.google.com")
📌 Example Output
https://www.google.com is UP ✅
🔮 Future Improvements
⏰ Automatic checking using scheduler
📧 Email alerts when a site goes down
📊 Logging system
🌐 Multiple website checker
📱 Android app version
🤝 Contributing

Contributions are welcome!
You can fork this repo and submit a pull request.

📄 License

This project is free to use and open-source.

👨‍💻 Author

Kartik Jha
