from flask import Flask, render_template
from utils import *

app = Flask(__name__)

list_candidates = load_candidates()
candidates = get_all(list_candidates)


@app.route('/')
def get_all():
    return render_template('home_page.html', title='Главная страница', candidates=candidates)


@app.route('/candidates/<int:x>')
def get_candidate_by_pk(x):
    url = "http://mypictures.me/123"
    candidate = get_by_pk(candidates, x)
    return render_template('candidates.html', title='Кандидат', candidate=candidate, url=url)


@app.route('/skills/<x>')
def get_candidate_by_skills(x):
    skill = get_by_skill(candidates, x)
    return render_template('skills.html', title='Скиллы', skill=skill)


if __name__ == '__main__':
    app.run()
