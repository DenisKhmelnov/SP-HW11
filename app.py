from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

@app.route("/")
def show_all():
    return render_template("list.html", candidates=load_candidates_from_json())

@app.route("/candidate/<int:pk>/")
def show_candidate(pk):
    candidate = get_candidate(pk)
    return render_template("card.html", candidate=candidate)

@app.route("/search/<candidate_name>")
def show_by_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates, candidates_count=len(candidates))

@app.route("/skill/<skill_name>/")
def show_by_skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template("skill.html", candidates=candidates, skill=skill_name, candidates_count=len(candidates))

app.run()
