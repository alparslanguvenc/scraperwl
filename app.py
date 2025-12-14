from flask import Flask, render_template, request, send_file, jsonify
from scraper import scrape_reviews_playwright, save_to_docx
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'No URL provided'}), 400
    
    print(f"Received request to scrape: {url}")
    try:
        # Scrape
        reviews = scrape_reviews_playwright(url)
        
        # Save
        filename = "Scraped_Reviews.docx"
        output_path = os.path.join(os.getcwd(), filename)
        save_to_docx(reviews, output_path)
        
        return jsonify({'message': 'Success', 'count': len(reviews), 'download_url': '/download'})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/download')
def download():
    path = os.path.join(os.getcwd(), "Scraped_Reviews.docx")
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    # Cloud (Render) provides PORT, locally we use 5001 to avoid AirPlay conflict
    port = int(os.environ.get('PORT', 5001))
    # Bind to 0.0.0.0 only if PORT env is set (Cloud), otherwise localhost (Safer/Faster locally)
    host = '0.0.0.0' if os.environ.get('PORT') else '127.0.0.1'
    app.run(debug=True, host=host, port=port)
