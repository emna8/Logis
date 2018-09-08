from views import pd

csv_files_NUMBER=2

colors_vente = [
    "#f01414", "#FFA500"]
colors_loc = [
    "#f01414", "#ABCABC"]

cols = ["#f01414", "#FFA500", "#ABCABC"]


# **********************************************List COUTRIES***************************************
list_country_vente = ['Bizerte', 'Banlieue Nord', 'Ariana', 'Ben arous', 'Mannouba', 'Nabeul', 'Sfax', 'Sousse',
                      'Monastir', 'Mahdia',  'Djerba'
                      ]

list_country_loc = ['Bizerte', 'Banlieue Nord', 'Ariana', 'Ben arous',  'Bardo', 'Mannouba', 'Nabeul',   'Sfax',
                    'Sousse',   'Mahdia', 'Monastir',
                    'Gabes',  'Jendouba']

list_country_ratio = list(
    set(list_country_vente).intersection(list_country_loc))

market_vente = ["Tayara", "Jumia"]
market_all = ["Tayara", "Jumia", "Tunisie annonce"]
market_lic = ["Tayara", "Tunisie annonce"]
#**************************************************************************************......


def dataframes(csv_file):
    return pd.read_csv(csv_file, encoding="Latin 1")

def fill_all_defs(vente_or_loc):#vente or loc
    list_to_fill=list()
    for i in range(csv_files_NUMBER):
        list_to_fill.append(dataframes(f"clear_csv_{vente_or_loc}_{i+1}.csv")) 
    return list_to_fill           

all_df_vente=list()
all_df_vente=fill_all_defs("vente")
all_df_loc=list()
all_df_loc=fill_all_defs("loc")
#***************************AVG Vente**********************************
def avg(str, df):
    return df[df["Country"] == str].Moy_prix_by_size.mean()

# *********************RATIO*************************************
def ratio(str, df_vente, df_loc):
    vente = avg(str, df_vente)
    loc = avg(str, df_loc)
    if(loc != 0):
        print(f"1 {loc}")
        return vente/loc
    else:
        print(f"2 {loc}")
        return vente

def list_avg(list_country_vente_or_loc,df):
    list_avg = list()
    for i in range(len(list_country_vente_or_loc)):
        list_avg.append(avg(list_country_vente_or_loc[i], df))
    return list_avg

def fill_all_avgs(list_df_vente_or_loc,list_country):
    all_list_avg=list()
    for df in list_df_vente_or_loc:    
        all_list_avg.append(list_avg(list_country, df))
    return all_list_avg   

def fill_all_ratio():
    all_ratio=list()
    sublist=list()
    for i in range(csv_files_NUMBER):
        sublist=list()
        for c in list_country_ratio:
            sublist.append(ratio(c,all_df_vente[i],all_df_loc[i]))
        all_ratio.append(sublist)    
    return all_ratio


def shape_market(csv_file):
    return pd.read_csv(csv_file, encoding='ISO-8859-1').shape[0]

"""def fill_all_market_values(market,status):#market is jumia , tayara or tunisie
    list_to_fill=list()
    for i in range(csv_files_NUMBER):
        list_to_fill.append(shape_market(f"{market}_{status}{i}"))
    return list_to_fill"""

#***************************************************************************
all_list_avg_vente=fill_all_avgs(all_df_vente,list_country_vente)
all_list_avg_loc=fill_all_avgs(all_df_loc,list_country_loc)            
all_list_ratio=fill_all_ratio()

# *********************RATIO***************************
# ************************************************************************************



"""j = shape_market("jumia_vente2.csv")
tay_v = shape_market("tayara_vente2.csv")
tay_l = shape_market("tayara_loc2.csv")
tu = shape_market("tunisie_loc2.csv")
list_market_vente1 = [j, tay_v]
list_market_loc1 = [tay_l, tu]
list_market_values1 = [tay_l+tay_v, j, tu]"""

# **********************************************************************************



class data(object):
    lable = ""
    y = 0
    url = ""

    def __init__(self, label, y, u):
        self.label = label
        self.y = y
        self.url = u


alpha_urls = ['/learn', "/detail/2", "http://bing.com/", "http://bing.com/",
              "http://bing.com/", "http://bing.com/", "http://bing.com/",
              "http://bing.com/", "http://bing.com/", "http://bing.com/", "http://bing.com/"]  # "{{ url_for('learn') }}"
alpha_urls_loc = ["http://bing.com/", "http://bing.com/", "http://bing.com/", "http://bing.com/",
                  "http://bing.com/", "http://bing.com/", "http://bing.com/",
                  "http://bing.com/", "http://bing.com/", "http://bing.com/", "http://bing.com/", "http://bing.com/", "http://bing.com/"]
alpha_urls_ratio = ["http://bing.com/", "http://bing.com/", "http://bing.com/", "http://bing.com/",
                    "http://bing.com/", "http://bing.com/", "http://bing.com/",
                    "http://bing.com/", "http://bing.com/", "http://bing.com/", "http://bing.com/", "http://bing.com/", "http://bing.com/", "http://bing.com/"]


# IF YOU ADD ANOTHER NEXT (You don't really add an html file, but you rerender the current one with different data)
"""tab_market_vente = [list_market_vente1]
tab_market_loc = [list_market_loc1]
tab_list_market_values = [list_market_values1]"""

# ****************************************************************************************************


