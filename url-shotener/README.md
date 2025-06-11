# URL Shortener Service
A simple Flask-based URL shortener service that:
- Creates short URLs from long URLs
- Redirects users when they visit the short URL

## How to Run
1. Install requirements: `pip install flask`
2. Run the server: `python app.py`
3. Test with Postman or curl

## Endpoints
- POST /shorten - Create a short URL
- GET /<code> - Visit a short URL