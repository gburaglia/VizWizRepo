
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import random

def retrieve_data():
    loc_df = pd.read_csv('data/USGeoSpendUpdated.csv', index_col=0)
    targ_df = pd.read_csv('data/USTargetedSpend.csv', index_col=0)
    parties_df = pd.read_csv('data/PartyAffiliationByState.csv', index_col=0)
    polls_df = pd.read_csv('data/PresidentialPrimaryPolls.csv', index_col=False)
    kwords = pd.read_csv('data/google-political-ads-top-keywords-history.csv')

    return loc_df, targ_df, parties_df, polls_df, kwords

def splitListToRows(row,row_accumulator,target_column,separator):
    split_row = row[target_column].split(separator)
    for s in split_row:
        new_row = row.to_dict()
        new_row[target_column] = s
        row_accumulator.append(new_row)

def build_targ(targ_df):
    new_rows = []
    targ_df.apply(splitListToRows,axis=1,args = (new_rows,"Geo_Targeting_Included",","))
    new_df = pd.DataFrame(new_rows)
    new_df.head()

    #https://gist.github.com/jlln/338b4b0b55bd6984f883
    pivot_df = pd.pivot_table(new_df, index =['Geo_Targeting_Included'], values ="Ads_List",aggfunc=pd.Series.nunique)

    criteria = pivot_df.index.isin(['Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Minor Outlying Islands', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'U.S. Virgin Islands', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'])
    cleaned_pivot = pivot_df[criteria]
    cleaned_pivot.head()

    state_abbreviations = get_states()
    #https://gist.github.com/rogerallen/1583593

    cleaned_pivot.index = cleaned_pivot.index.map(state_abbreviations)
    return cleaned_pivot

def build_loc(loc_df):
    loc_tbl = pd.pivot_table(loc_df, index =['State'], values=['Spend_USD'], aggfunc={'Spend_USD':np.sum})
    return loc_tbl

def build_parties(parties_df):

    state_abbreviations = get_states()
    parties_df.index = parties_df.index.map(state_abbreviations)

    zarray = []
    for n in range(0,len(parties_df.index)):

        if parties_df['Classification'].iloc[n]=="Strong Democratic":
            zarray.append(1.0)
        elif parties_df['Classification'].iloc[n]=="Lean Democratic":
            zarray.append(2.0)
        elif parties_df['Classification'].iloc[n]=="Competitive":
            zarray.append(3.0)
        elif parties_df['Classification'].iloc[n]=="Lean Republican":
            zarray.append(4.0)
        elif parties_df['Classification'].iloc[n]=="Strong Republican":
            zarray.append(5.0)
    return parties_df,zarray

def build_polls(polls_df,start_date, end_date,poll_type=None):

    if poll_type != None:
        if int(poll_type) == 1:
            polls_df = polls_df[polls_df.party == 'DEM']
        elif int(poll_type) == 2:
            polls_df = polls_df[polls_df.party == 'REP']

    polls_df["State-Week"] = polls_df["state"] + "," + polls_df['Week Beginning']
    polls_grouped_df = polls_df.groupby(["State-Week",'candidate_name']).agg({'People Voting':['sum'],'state':['first'],'Week Beginning':['first']})
    polls_grouped_df.columns=['Votes',"State","Week"]
    polls_max_df = polls_grouped_df.groupby(level=0,group_keys=False).apply(lambda x: x.nlargest(1,['Votes'])).reset_index()
    polls_max_df["Week"] = pd.to_datetime(polls_max_df["Week"])
    polls_max_df = polls_max_df.sort_values(['State','Week'],ascending=True)

    state_abbreviations = get_states()
    polls_max_df["State"] = polls_max_df["State"].map(state_abbreviations)

    polls_max_filtered_df = polls_max_df[(polls_max_df["Week"]>=start_date) & (polls_max_df["Week"]<=end_date)]
    polls_max_filtered_df = polls_max_filtered_df.sort_values(['State','Week'],ascending=False)

    polls_regrouped_df =polls_max_filtered_df.groupby(["State"]).agg({'candidate_name':['first'],'Votes':['first'],'Week':['first']}).reset_index()
    polls_regrouped_df.columns=['State','Candidate Name','Votes','Week']

    polls_regrouped_df


    return polls_max_filtered_df,polls_regrouped_df

def generate_polls_mapped_z(polls_orgvotes_df, polls_zlist,polls_zarray):
    candidate_list = list((polls_orgvotes_df["Candidate Name"]))
    mapped_z = []
    for x in range(0,len(candidate_list)):
        for y in range(0,len(polls_zlist)):
            if candidate_list[x].strip() == polls_zlist[y].strip():
                mapped_z.append(polls_zarray[y])

    polls_orgvotes_df["Z Values"] = mapped_z
    return mapped_z

def build_polls_zarray(polls_orgvotes_df):
    polls_zarray_builder = []
    polls_zarray_builder = polls_orgvotes_df["Candidate Name"]
    polls_zlist = list(set(polls_zarray_builder))

    polls_zarray = []
    candidate_num = 0
    for i in range(0,len(polls_zlist)):
        polls_zarray.append(i+1)
    candidate_num = len(polls_zarray)
    return candidate_num,polls_zarray, polls_zlist

def generate_polls_colors(candidate_count):
    #Random color array based on number of candidates
    rgb = []
    #for a in range(0,len(lim_array)):
        #r = str(random.randint(0,255))
        #g = str(random.randint(0,255))
        #b = str(random.randint(0,255))
        #rgb.append([lim_array[a],"rgb" + "(" + r + ","+ g + "," + b + ")" ])

    rgb = sns.color_palette("Set2",candidate_count).as_hex()
    return rgb

def build_polls_limits(polls_orgvotes_df,polls_zarray,mapped_z):
    SD_limit = 0
    LD_limit = 0
    C_limit = 0
    LR_limit = 0
    SR_limit= 0

    lim_array = [0]
    lim_count = 0
    for c in range(0,len(polls_zarray)):
        for n in range(0,len(polls_orgvotes_df["Z Values"])):
            if polls_zarray[c] == mapped_z[n]:
                lim_count = lim_count + 1
        lim_array.append(round(lim_count/len(mapped_z),2))
    return lim_array

def create_parties_limits(parties_df,zarray):
    SD_limit = 0
    LD_limit = 0
    C_limit = 0
    LR_limit = 0
    SR_limit= 0
    for n in range(0,len(parties_df.index)):
        if parties_df['Classification'].iloc[n]=="Strong Democratic":
            SD_limit = SD_limit + 1
        elif parties_df['Classification'].iloc[n]=="Lean Democratic":
            LD_limit = LD_limit + 1
        elif parties_df['Classification'].iloc[n]=="Competitive":
            C_limit = C_limit + 1
        elif parties_df['Classification'].iloc[n]=="Lean Republican":
            LR_limit = LR_limit + 1
        elif parties_df['Classification'].iloc[n]=="Strong Republican":
            SR_limit = SR_limit + 1

    SD_limit = SD_limit/len(zarray)
    LD_limit = (LD_limit/len(zarray)) + SD_limit
    C_limit = (C_limit/len(zarray)) + LD_limit
    LR_limit = (LR_limit/len(zarray)) + C_limit
    SR_limit = (SR_limit/len(zarray)) + LR_limit
    return SD_limit, LD_limit, C_limit, LR_limit, SR_limit

def draw_polls_trace(myFig, data, polls_orgvotes_df,mycolorscale):
    polls_orgvotes_df["Week String"] = polls_orgvotes_df["Week"].dt.strftime("%x")
    #endpts = list(np.linspace(1, 12, len(mycolorscale) - 1))
    myFig = px.choropleth(polls_orgvotes_df,
                    locations=polls_orgvotes_df['State'],  # DataFrame column with locations
                    color=polls_orgvotes_df['Candidate Name'],  # DataFrame column with color values
                    hover_name = polls_orgvotes_df['Candidate Name'],
                    locationmode = 'USA-states',
                    color_discrete_sequence = mycolorscale,
                    )
    myFig.update_traces(
    hoverinfo = 'text + name + location',
    hovertemplate = None)

    return myFig,data

def draw_loc_trace(myFig,data,loc_tbl):
    #event_data = go.Choropleth(
    #    locations=loc_tbl.index,  # DataFrame column with locations
    #    z=loc_tbl["Spend_USD"],  # DataFrame column with color values
    #    hoverinfo='location+z', # DataFrame column hover info
    #    locationmode = 'USA-states',
        #visible=False
    loc_tbl = loc_tbl.rename(columns={"Spend_USD":"Spend in USD"})

    myFig = px.choropleth(loc_tbl,
                    locations=loc_tbl.index,  # DataFrame column with locations
                    color=loc_tbl["Spend in USD"],
                    locationmode = 'USA-states',
                    color_continuous_scale='deep'
                    )
    myFig.update_traces(
    hoverinfo = 'location+text+name+z',
    hovertemplate = None
        )
    #myFig.add_trace(event_data)
    #data.append(event_data)
    myFig.update_layout(title= {'text':'Political Ad Spending by State in Millions','x':0.5}, dragmode=False, geo_scope='usa', paper_bgcolor = 'rgb(244,231,215)', geo={'bgcolor': 'rgba(0,0,0,0)', 'lakecolor':'rgb(244,231,215)'},font =dict(
        color="Black",
        size = 14
    ))
    return myFig, data

def draw_targ_trace(myFig,data,cleaned_pivot):

    cleaned_pivot = cleaned_pivot.rename(columns={"Ads_List":"Number of Ads"})

    myFig = px.choropleth(cleaned_pivot,
                    locations=cleaned_pivot.index,  # DataFrame column with locations
                    color=cleaned_pivot["Number of Ads"],
                    locationmode = 'USA-states',
                    color_continuous_scale='dense'
                    )
    myFig.update_traces(
    hoverinfo = 'location+text+name+z',
    hovertemplate = None)
    myFig.update_layout(title= {'text':'Number of Targeted Ads by State','x':0.5}, dragmode=False, geo_scope='usa', paper_bgcolor = 'rgb(244,231,215)', geo={'bgcolor': 'rgba(0,0,0,0)', 'lakecolor':'rgb(244,231,215)'},font =dict(
        color="Black",
        size = 14
    ))


    return myFig, data

def draw_parties_trace(myFig,data,parties_df, zarray, SD_limit, LD_limit, C_limit, LR_limit, SR_limit):

    myFig = px.choropleth(parties_df,  # Input Pandas DataFrame
                    locations=parties_df.index,  # DataFrame column with locations
                    color=parties_df["Classification"],  # DataFrame column with color values
                    hover_name=parties_df["Classification"], # DataFrame column hover info
                    locationmode = 'USA-states', # Set to plot as US States
                    #color_discrete_sequence=px.colors.qualitative.G10,
                   color_discrete_sequence=['rgb(4,21,59)','rgb(139,195,236)', 'rgb(193,200,209)', 'rgb(247,190,192)','rgb(206,0,0)'],
                    )
    myFig.update_traces(
    hoverinfo = 'text + name + location',
    hovertemplate = None)
    myFig.update_layout(title= {'text':'Political Affiliation by State','x':0.5}, dragmode=False, geo_scope='usa',paper_bgcolor = 'rgb(244,231,215)',geo={'bgcolor': 'rgba(0,0,0,0)', 'lakecolor':'rgb(244,231,215)'}, font =dict(
        color="Black",
        size = 14
    ))
    return myFig, data

def map_layout(myText):
    layout = dict(
    title_text= myText,
    title_x = 0.5,
    font =dict(
        color="Black",
        size = 14
    ),
    #title_x=0.5,
    height = 600,
    geo_scope='usa',
    dragmode = False,
    paper_bgcolor = 'rgb(244,231,215)',
    geo={'bgcolor': 'rgba(0,0,0,0)', 'lakecolor':'rgb(244,231,215)'},
    #plot_bgcolor = 'rgb(244,231,215)',
    showlegend=True,
    legend=dict(
        x=0.9,
        y=0.5,
        traceorder="normal",
        font=dict(
            size=12,
            color="Black"
        ),
        bgcolor='rgb(244,231,215)',
        bordercolor="Black",
        borderwidth=1,
    )
    )
    return layout

def draw_map(num, loc_tbl, cleaned_pivot, parties_df, zarray, polls_orgvotes_df):
    num = int(num)
    if(num==1):
        data = []
        myFig = go.Figure()
        displayFig, displayData = draw_loc_trace(myFig,data,loc_tbl)
    elif(num==2):
        data = []
        myFig = go.Figure()
        displayFig, displayData = draw_targ_trace(myFig,data,cleaned_pivot)
    elif(num==3):
        data = []
        myFig = go.Figure()
        SD_limit, LD_limit, C_limit, LR_limit, SR_limit = create_parties_limits(parties_df,zarray) #Limits for parties df
        displayFig, displayData = draw_parties_trace(myFig,data,parties_df,zarray,SD_limit, LD_limit, C_limit, LR_limit, SR_limit)
        layout = map_layout('Political Party Identification by State')
        displayFig.update_layout(layout)
    elif(num==4):
        data = []
        myFig = go.Figure()
        candidate_num,polls_zarray, polls_zlist = build_polls_zarray(polls_orgvotes_df)
        mapped_z = generate_polls_mapped_z(polls_orgvotes_df,polls_zlist,polls_zarray)

        #lim_array = build_polls_limits(polls_orgvotes_df,polls_zarray,mapped_z)
        mycolorscale = generate_polls_colors(candidate_num)
        displayFig, displayData = draw_polls_trace(myFig,data,polls_orgvotes_df,mycolorscale)
        layout = map_layout('Poll Winners by State During Date Range')
        displayFig.update_layout(layout)

    return displayFig, displayData

def get_states():
	state_abbreviations={
		'Alabama': 'AL',
		'Alaska': 'AK',
		'Arizona': 'AZ',
		'Arkansas': 'AR',
		'California': 'CA',
		'Colorado': 'CO',
		'Connecticut': 'CT',
		'Delaware': 'DE',
		'District of Columbia': 'DC',
		'Florida': 'FL',
		'Georgia': 'GA',
		'Hawaii': 'HI',
		'Idaho': 'ID',
		'Illinois': 'IL',
		'Indiana': 'IN',
		'Iowa': 'IA',
		'Kansas': 'KS',
		'Kentucky': 'KY',
		'Louisiana': 'LA',
		'Maine': 'ME',
		'Maryland': 'MD',
		'Massachusetts': 'MA',
		'Michigan': 'MI',
		'Minnesota': 'MN',
		'Mississippi': 'MS',
		'Missouri': 'MO',
		'Montana': 'MT',
		'Nebraska': 'NE',
		'Nevada': 'NV',
		'New Hampshire': 'NH',
		'New Jersey': 'NJ',
		'New Mexico': 'NM',
		'New York': 'NY',
		'North Carolina': 'NC',
		'North Dakota': 'ND',
		'Northern Mariana Islands':'MP',
		'Ohio': 'OH',
		'Oklahoma': 'OK',
		'Oregon': 'OR',
		'Palau': 'PW',
		'Pennsylvania': 'PA',
		'Puerto Rico': 'PR',
		'Rhode Island': 'RI',
		'South Carolina': 'SC',
		'South Dakota': 'SD',
		'Tennessee': 'TN',
		'Texas': 'TX',
		'Utah': 'UT',
		'Vermont': 'VT',
		'Virgin Islands': 'VI',
		'Virginia': 'VA',
		'Washington': 'WA',
		'West Virginia': 'WV',
		'Wisconsin': 'WI',
		'Wyoming': 'WY',
	}
	return state_abbreviations

def draw_bars():
    names = ["Biden", "Bloomberg", "Sanders", "Warren", "Buttigieg"]
    url = []

    for i in range(0,len(names)):
        url.append("static/images/{}.png".format(names[i].title()))
        #print(names[i])
        print(url[i])
    myvalues = [10,20,30,15,5]

    mydata = go.Bar(
        y=myvalues,# DataFrame column with locations
        hovertext = names,
        hoverinfo = 'text + y',
        #x=names,
                )
    myFig = go.Figure()
    layout = dict(
        autosize = False,
        width=1000,
        height = 200,
        # top, bottom, left and right margins
        margin = dict(t = 2, b = 50, l = 2, r = 2),
        font = dict(color = '#FFFFFF', size = 11),
        dragmode = False,
        #plot_bgcolor= 'white',
        )
    myFig.update_layout(layout)
    img = []

    for i in range(0,len(names)):
        img.append(dict(source=url[i],
                        xref='x',
                        yref='paper',
                        x=i,
                        y=0,
                        sizex=1.0,
                        sizey=0.5,
                        xanchor='center',
                        yanchor='middle'))

    layout = go.Layout(images=img)
    myFig.update_layout(layout)
    myFig.add_trace(mydata)
    return myFig

def build_poll_ratings(polls_df,start_date, end_date, poll_type=None):

    if poll_type != None:
        if int(poll_type) == 1:
            polls_df = polls_df[polls_df.party == 'DEM']
        elif int(poll_type) == 2:
            polls_df = polls_df[polls_df.party == 'REP']

    polls_df['Week Beginning'] = pd.to_datetime(polls_df['Week Beginning'])
    polls_df = polls_df[polls_df['Week Beginning'] >= start_date]
    polls_df = polls_df[polls_df['Week Beginning'] <= end_date]
    polls_summary = polls_df.groupby('candidate_name').agg({'People Voting':['sum']})
    total = sum(polls_df['People Voting'])
    polls_summary['Vote Share'] = (polls_summary['People Voting'] / total) * 100
    polls_summary = polls_summary.round(2)
    polls_summary = polls_summary.sort_values(['Vote Share'],ascending=False).reset_index().head(5)
    names_list = [polls_summary.candidate_name[0], polls_summary.candidate_name[1], polls_summary.candidate_name[2], polls_summary.candidate_name[3], polls_summary.candidate_name[4]]
    nums_list = [polls_summary['Vote Share'][0], polls_summary['Vote Share'][1], polls_summary['Vote Share'][2], polls_summary['Vote Share'][3], polls_summary['Vote Share'][4]]

    return names_list, nums_list

def update_keywords(name, value, kw_stats):
    if name in kw_stats:
        kw_stats[name] = kw_stats[name] + value
    else:
        kw_stats[name] = value

    return kw_stats

def get_bar_data(type, start_date, end_date, polls_df, kwords, poll_type):
    #list of numbers(polling results or)
    nums_list =[]
    #list of names (candidates or keywords)
    names_list=[]
    if(type == 1):
        #filter polling data tto date Range
        # aggregate and sort
        # arrange
        polls_max_filtered_df, polls_orgvotes_df = build_polls(polls_df,start_date,end_date, poll_type)
        #Get top 5 candidates and number of states
        polls_count_df = polls_max_filtered_df.groupby(['candidate_name']).agg({'State':['count']})
        polls_count_df.columns=["State Count"]
        polls_count_final_df = polls_count_df.sort_values(['State Count'],ascending=False).reset_index().head(5)
        #list of polling numbers
        for n in range(1,6):
            try:
                nums_list.append(polls_count_final_df.iloc[n-1,1])
            except:
                nums_list.append(0)
         #list of candidate names
        for c in range(1,6):
            try:
                names_list.append(polls_count_final_df.iloc[c-1,0])
            except:
                names_list.append('')
    elif type == 2:
        kwords['Report_Date'] = pd.to_datetime(kwords['Report_Date'])
        kw = kwords[(kwords.Report_Date >= start_date) & (kwords.Report_Date < end_date)]
        kw_stats = {}

        for i,row in kw.iterrows():
            name1 = kw['Keyword_1'][i]
            value1 = kw['Spend_USD_1'][i]
            name2 = kw['Keyword_2'][i]
            value2 = kw['Spend_USD_2'][i]
            name3 = kw['Keyword_3'][i]
            value3 = kw['Spend_USD_3'][i]
            name4 = kw['Keyword_4'][i]
            value4 = kw['Spend_USD_4'][i]
            name5 = kw['Keyword_5'][i]
            value5 = kw['Spend_USD_5'][i]
            name6 = kw['Keyword_6'][i]
            value6 = kw['Spend_USD_6'][i]

            kw_stats = update_keywords(name1, value1, kw_stats)
            kw_stats = update_keywords(name2, value2, kw_stats)
            kw_stats = update_keywords(name3, value3, kw_stats)
            kw_stats = update_keywords(name4, value4, kw_stats)
            kw_stats = update_keywords(name5, value5, kw_stats)
            kw_stats = update_keywords(name6, value6, kw_stats)

        kw_stats = {k: v for k, v in sorted(kw_stats.items(), key=lambda item: item[1], reverse = True)}
        names_list = []
        names_list.append(list(kw_stats.keys())[0].title())
        names_list.append(list(kw_stats.keys())[1].title())
        names_list.append(list(kw_stats.keys())[2].title())
        names_list.append(list(kw_stats.keys())[3].title())
        names_list.append(list(kw_stats.keys())[4].title())

        nums_list = []
        nums_list.append(float('{0:.2f}'.format(list(kw_stats.values())[0]/1000000)))
        nums_list.append(float('{0:.2f}'.format(list(kw_stats.values())[1]/1000000)))
        nums_list.append(float('{0:.2f}'.format(list(kw_stats.values())[2]/1000000)))
        nums_list.append(float('{0:.2f}'.format(list(kw_stats.values())[3]/1000000)))
        nums_list.append(float('{0:.2f}'.format(list(kw_stats.values())[4]/1000000)))
    elif type == 3:
        names_list, nums_list = build_poll_ratings(polls_df,start_date,end_date, poll_type)


    return nums_list, names_list
