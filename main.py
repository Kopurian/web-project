from website import create_app

app = create_app()

# only runs when the file is run directly

if __name__ == '__main__':
    app.run(debug = True)