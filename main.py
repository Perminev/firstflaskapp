from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hi, there are links with facts about technology addictions</h1><ul><a href="/stress">Stress</a></ul><ul><a href="/fifty">Fifty percent...</a></ul><ul><a href="/explore">Exploring</a></ul><ul><a href="/sixty">Sixty percent...</a></ul><ul><a href="/whatdid">What did</a></ul><ul><a href="/maskfirst">First Ilon Mask Fact</a></ul><ul><a href="/masksecond">Second Ilon Mask Fact</a></ul><ul><a href="/social">Social Sites</a></ul>'

@app.route("/stress")
def stress():
    return "<p>Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.</p>"

@app.route("/fifty")
def fiftypercent():
    return "<p>Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.</p>"

@app.route("/explore")
def exploring():
    return "<p>Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.</p>"

@app.route("/sixty")
def sixtypercent():
    return "<p>Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.</p>"


@app.route("/whatdid")
def whatdid():
    return "<p>Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.</p>"

@app.route("/maskfirst")
def maskfirst():
    return "<p>Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.</p>"

@app.route("/masksecond")
def masksecond():
    return "<p>Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением.</p>"

@app.route("/social")
def social():
    return "<p>Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ.</p>"

app.run(debug=True)