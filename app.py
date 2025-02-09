# app.py
@app.route('/')

def main():
    print("Hello, Jenkins! This is a simple Python app.")

if __name__ == "__main__":
    main()
    app.debug=True
    app.run(host = '0.0.0.0',port=5000,debug=True)
