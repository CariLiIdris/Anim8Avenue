from flask import Flask # type: ignore

app = Flask(__name__)

app.secret_key = "Koifish"

DB = 'anim8AveSchema'