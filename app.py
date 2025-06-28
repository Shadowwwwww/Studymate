import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Class page listing subjects
@app.route('/class/<int:class_number>')
def class_page(class_number):
    return render_template('class.html', class_number=class_number)

# Subject page showing notes and quiz links by chapter
@app.route('/class/<int:class_number>/<subject>')
def subject_page(class_number, subject):
    note_path = f"notes/{subject}_{class_number}_ch1.txt"
    if os.path.exists(note_path):
        with open(note_path, "r", encoding="utf-8") as f:
            note = f.read()
    else:
        note = "🚧 Notes for this subject will be added soon."

    return render_template('subject.html', class_number=class_number, subject=subject, note=note)

# Quizzes data structured by class, subject, chapter, difficulty
quizzes = {
    "8": {
        "science": {
            "ch1": {
                "easy": [
                    {"q": "What do plants need to make food?", "options": ["Sunlight", "Moonlight", "Water", "Soil"], "answer": "Sunlight"},
                    {"q": "Which part of the plant conducts water?", "options": ["Stem", "Root", "Leaves", "Flower"], "answer": "Stem"},
                    {"q": "Which gas do plants absorb from air?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
                    {"q": "Plants prepare food in which part?", "options": ["Roots", "Stem", "Leaves", "Flowers"], "answer": "Leaves"},
                    {"q": "What is the green pigment in leaves?", "options": ["Chlorophyll", "Carotene", "Xanthophyll", "Anthocyanin"], "answer": "Chlorophyll"},
                    {"q": "What process do plants use to make food?", "options": ["Photosynthesis", "Respiration", "Digestion", "Transpiration"], "answer": "Photosynthesis"},
                    {"q": "Water is transported by which plant tissue?", "options": ["Xylem", "Phloem", "Cambium", "Epidermis"], "answer": "Xylem"},
                    {"q": "Which part anchors the plant?", "options": ["Root", "Stem", "Leaves", "Flower"], "answer": "Root"},
                    {"q": "Which part is responsible for reproduction in plants?", "options": ["Roots", "Stem", "Leaves", "Flower"], "answer": "Flower"},
                    {"q": "Which is a Kharif crop?", "options": ["Wheat", "Mustard", "Paddy", "Gram"], "answer": "Paddy"},
                ],
                "medium": [
                    {"q": "Which part of the plant transports food?", "options": ["Phloem", "Xylem", "Root", "Leaf"], "answer": "Phloem"},
                    {"q": "What is the function of stomata?", "options": ["Gas exchange", "Absorption of water", "Support", "Reproduction"], "answer": "Gas exchange"},
                    {"q": "Which crop is grown in Rabi season?", "options": ["Maize", "Wheat", "Cotton", "Rice"], "answer": "Wheat"},
                    {"q": "Which process releases oxygen?", "options": ["Respiration", "Photosynthesis", "Transpiration", "Digestion"], "answer": "Photosynthesis"},
                    {"q": "What is the role of roots?", "options": ["Absorb water", "Make food", "Transport food", "Reproduce"], "answer": "Absorb water"},
                    {"q": "Which is a rabi crop?", "options": ["Gram", "Maize", "Rice", "Cotton"], "answer": "Gram"},
                    {"q": "Water loss from leaves is called?", "options": ["Transpiration", "Photosynthesis", "Respiration", "Evaporation"], "answer": "Transpiration"},
                    {"q": "Which organelle is responsible for photosynthesis?", "options": ["Chloroplast", "Mitochondria", "Nucleus", "Ribosome"], "answer": "Chloroplast"},
                    {"q": "What is manure?", "options": ["Natural fertilizer", "Chemical fertilizer", "Pesticide", "Insecticide"], "answer": "Natural fertilizer"},
                    {"q": "What protects plants from weeds?", "options": ["Weeding", "Mulching", "Manure", "Pesticides"], "answer": "Mulching"},
                ],
                "hard": [
                    {"q": "What is photosynthesis?", "options": ["Process of making food", "Breathing", "Water absorption", "Growth"], "answer": "Process of making food"},
                    {"q": "What is the role of xylem?", "options": ["Transport food", "Transport water", "Store food", "Support plant"], "answer": "Transport water"},
                    {"q": "Which season is Kharif crops grown?", "options": ["Winter", "Summer", "Rainy", "Autumn"], "answer": "Rainy"},
                    {"q": "What is the chemical formula of water used in photosynthesis?", "options": ["H2O", "CO2", "O2", "N2"], "answer": "H2O"},
                    {"q": "What is transpiration?", "options": ["Loss of water from leaves", "Absorption of water", "Photosynthesis", "Respiration"], "answer": "Loss of water from leaves"},
                    {"q": "Which part of plant is modified for climbing?", "options": ["Thorns", "Leaves", "Roots", "Tendrils"], "answer": "Tendrils"},
                    {"q": "What is the energy source for photosynthesis?", "options": ["Sunlight", "Electricity", "Heat", "Wind"], "answer": "Sunlight"},
                    {"q": "What do plants release during photosynthesis?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Methane"], "answer": "Oxygen"},
                    {"q": "Which part stores food in plants?", "options": ["Stem", "Root", "Leaf", "Fruit"], "answer": "Root"},
                    {"q": "What is a parasite plant?", "options": ["A plant that grows on others and harms them", "A plant that makes food", "A water plant", "A seed"], "answer": "A plant that grows on others and harms them"},
                ],
                "impossible": [
                    {"q": "Which pigment absorbs light energy for photosynthesis?", "options": ["Chlorophyll", "Carotene", "Xanthophyll", "Anthocyanin"], "answer": "Chlorophyll"},
                    {"q": "What is the function of phloem in plants?", "options": ["Transport water", "Transport food", "Absorb minerals", "Support plant"], "answer": "Transport food"},
                    {"q": "Which part of the plant anchors it in soil?", "options": ["Stem", "Root", "Leaf", "Flower"], "answer": "Root"},
                    {"q": "Which tissue transports water in plants?", "options": ["Xylem", "Phloem", "Cambium", "Epidermis"], "answer": "Xylem"},
                    {"q": "Photosynthesis primarily occurs in which cell organelle?", "options": ["Chloroplast", "Mitochondria", "Nucleus", "Ribosome"], "answer": "Chloroplast"},
                    {"q": "Which crop is a Kharif crop?", "options": ["Wheat", "Paddy", "Gram", "Mustard"], "answer": "Paddy"},
                    {"q": "Water loss from leaves is called?", "options": ["Transpiration", "Photosynthesis", "Respiration", "Evaporation"], "answer": "Transpiration"},
                    {"q": "Which gas do plants absorb for photosynthesis?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
                    {"q": "Which is a rabi crop?", "options": ["Gram", "Rice", "Maize", "Cotton"], "answer": "Gram"},
                    {"q": "What protects plants from weeds?", "options": ["Weeding", "Mulching", "Manure", "Pesticides"], "answer": "Mulching"},
                ],
            },
            # You can add more chapters like "ch2" here similarly
        }
        # Add other subjects if needed
    }
    # Add other classes if needed
}

@app.route('/quiz/<int:class_number>/<subject>/<chapter>/<difficulty>', methods=['GET', 'POST'])
def quiz(class_number, subject, chapter, difficulty):
    try:
        questions = quizzes[str(class_number)][subject][chapter][difficulty]
        if not questions:
            return "No questions available for this quiz yet.", 404
    except KeyError:
        return "Quiz not found.", 404

    if request.method == 'POST':
        score = 0
        for i, q in enumerate(questions):
            selected = request.form.get(f'question-{i}')
            if selected == q['answer']:
                score += 1
        return render_template('quiz_result.html', score=score, total=len(questions),
                               class_number=class_number, subject=subject,
                               chapter=chapter, difficulty=difficulty)

    return render_template('quiz.html', questions=questions,
                           class_number=class_number, subject=subject,
                           chapter=chapter, difficulty=difficulty)

if __name__ == '__main__':
    app.run(debug=True)
