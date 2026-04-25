# 📰 Smart News Fetcher CLI (Python + NewsAPI)

A simple yet powerful command-line application built with Python that fetches the latest news based on user queries using NewsAPI. It displays top headlines in a clean format and saves results to a JSON file for later use.

---

## 🚀 Features

* 🔍 Search news by any topic
* 📰 Displays top latest headlines in terminal
* 📅 Automatically fetches recent news (dynamic date)
* 💾 Saves full results to a JSON file
* ⚡ Fast and lightweight CLI tool

---

## 🛠️ Tech Stack

* Python
* Requests (API handling)
* NewsAPI

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/news-fetcher-cli.git
cd news-fetcher-cli
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Get your free API key from: https://newsapi.org

### 👉 For Windows (PowerShell):

```powershell
$env:NEWS_API_KEY="your_api_key"
```

### 👉 For Windows (CMD):

```bash
set NEWS_API_KEY=your_api_key
```

### 👉 For Linux/Mac:

```bash
export NEWS_API_KEY=your_api_key
```

---

## ▶️ Usage

Run the program:

```bash
python main.py
```

Enter your desired topic when prompted:

```text
🔍 Which topic of news are you interested in: technology
```

---

## 📂 Output

* 📺 Displays top 10 news articles in terminal
* 📁 Saves all fetched data to:

```
news_results.json
```

---

## ⚠️ Error Handling

* Handles API errors gracefully
* Shows message if no articles found
* Validates API key presence

---

## 🔮 Future Improvements

* 🌐 GUI version (Tkinter / Web app)
* 🎨 Colored CLI output
* 📊 Category-based filtering
* 🔔 Notification system
* 🤖 AI-based news summarizer

---
## Demo video 
 link - 

## 🤝 Contributing

Feel free to fork this repo and improve it. Pull requests are welcome!

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 💡 Author

Made with ❤️ by Nikhil
