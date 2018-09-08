from app import app,render_template,pd
from variables import list_country_vente,list_country_loc,list_country_ratio,all_list_avg_vente,all_list_avg_loc,all_list_ratio ,data                 

@app.route("/next/<int:id>")
def next(id):
    i = 0
    list_obj_vente = list()
    list_obj_loc = list()
    data_points_ratio = list()
    data_points_mark_all = list()
    data_points_mark_vente = list()
    data_points_mark_loc = list()
    for a, b in zip(list_country_vente, all_list_avg_vente[id]):
        i += 1
        list_obj_vente.append(data(a, b, f'/detail/{i}'))

    for a, b in zip(list_country_loc, all_list_avg_loc[id]):
        i += 1
        list_obj_loc.append(data(a, b, f'/detail/{i}'))

    for a, b in zip(list_country_ratio, all_list_ratio[id]):
        i += 1
        data_points_ratio.append(data(a, b, f'/detail/{i}'))
    return render_template("next1.html",
                           data_points=list_obj_vente,
                           data_points_loc=list_obj_loc,
                           data_points_ratio=data_points_ratio,
                           #data_points_mark_vente=data_points_mark_vente,
                           #data_points_mark_all=data_points_mark_all,
                           #data_points_mark_loc=data_points_mark_loc,
                           max=17000)

# ****************************************************************************************************
list_country_vente_Banlieue=[""]

@app.route('/detail/<int:id>')
def detail(id):
    list_obj_vente = list()
    list_obj_loc = list()
    return render_template('detail.html',
        data_points=list_obj_vente,
        data_points_loc=list_obj_loc,
 )

# ****************************************************************************************************


"""@app.route('/')
def dash():
    list_obj_vente = list()
    list_obj_loc = list()
    data_points_ratio = list()

    for a, b, c in zip(list_country_vente, list_avg_vente, alpha_urls):
        list_obj_vente.append(data(a, b, c))

    for a, b, c in zip(list_country_loc, list_avg_loc, alpha_urls_loc):
        list_obj_loc.append(data(a, b, c))

    for a, b, c in zip(list_country_ratio, list_ratio, alpha_urls_ratio):
        data_points_ratio.append(data(a, b, c))
    pie_labels = ["Tayara", "Jumia"]
    pie_values = list_market_vente
    list_market_labels = ["Tayara", "Jumia", "Tunisie annonce"]
    pie_loc_labels = ["Tayara", "Tunisie annonce"]
    pie_loc_values = list_market_loc
    return render_template("dash.html", data_points=list_obj_vente, data_points_loc=list_obj_loc,
                           data_points_ratio=data_points_ratio, set=zip(
                               pie_values, pie_labels, colors_vente),
                           set2=zip(pie_loc_values,
                                    pie_loc_labels, colors_loc),
                           set3=zip(list_market_values, list_market_labels, cols), max=17000)

"""
@app.route('/click')
def click():
    return render_template("clickable.html")


@app.route('/learn')
def learn():
    return render_template('a.html')