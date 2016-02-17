from flask import Flask, render_template, Markup
import yaml
app = Flask(__name__)

skills = yaml.load(open('skills.yaml'))

GAMES = {"BORDERLANDS":    False,
         "BORDERLANDSTPS": False,
         "BORDERLANDS2":   True}

@app.route('/')
def hello_world():
    title = "Jeek's Borderlands Site"
    
    try:
        return render_template('index.html', title = title, GAMES = GAMES)
    except Exception, e:
        return str(e)

@app.route('/test/')
def images():
    return render_template('images.html')

@app.route('/skilltrees/<character>/')
def classpage(character):
    if character in skills:
        title = "Jeek's Borderlands Site: " + character
        page = character
        page = "<div class=\"container\">\n"
        for i in skills[character]["Treeorder"]:
            page += '<div class="col-md-4" style="background:' + ["green","blue","red"][skills[character]["Treeorder"].index(i)] + '"><center>'
            page += '<h1>' + i + '</h1>' + "<hr>"
            page += "<table>"
            for k in xrange(1, 7):
                page += "<tr>"
                for m in xrange(1, 4):
                    seenone = False
                    for l in skills[character]["Trees"][i]:
                        if skills[character]["Trees"][i][l]["Tier"] == k and skills[character]["Trees"][i][l]["Pos"] == m:
                            page += "<td height=63 width=63 align=center valign=center>"
                            page += "<img title=\"" + l + "\" src=\"/static/icons/" + skills[character]["Trees"][i][l]["Image"]  + "\">"
#                            page += "<br>" + l
                            page += "</td>"
                            seenone = True
                    if not seenone:
                        page += "<td></td>"
                page += "</tr>"
            page += "</table>"
            page += '</div>'
        page += "</div>"
        return render_template('character.html', title = title, character = character, page = Markup(page), GAMES = GAMES)

@app.route('/weaponparts/<weapon>/')
def weapons(weapon):
    weapons = {"Sniper": "sniper.jpg",
               "SMG": "smg.jpg",
               "AssaultRifle": "assaultrifle.jpg",
               "Pistols": "pistols.jpg",
               "Shotguns": "shotguns.jpg",
               "RocketLaunchers": "rocketlaunchers.jpg",
               "Lasers": "lasers.jpg"}
    if weapon in weapons:
        title = "Jeek's Borderlands Site: Weapon Parts: " + weapon.replace("tR","t R").replace("tL", "t L")
        image = weapons[weapon]
        return render_template('weapons.html', title = title, weapon = image, GAMES = GAMES)
    else:
        return abort(), 404

if __name__ == "__main__":
    print skills
    app.run(host='0.0.0.0', port=5001)