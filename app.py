from MyApp import create_app

app = create_app()

#run server
if __name__ == "__main__":
    app.run(debug=True)

