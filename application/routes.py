from flask import render_template, redirect, url_for, jsonify, session
from flask_mail import Message, Mail
from application import application
from application.forms import FirstForm, SecondForm, ThirdForm, FourthForm, ExamplesForm, Contact
from application.tasks import launch_simulator, get_progress, graphing, full_simulator
from application.calculations import calculations, summary_results
from application.parameters import get_parameters
from application.reset_files import reset_files
from threading import Thread
import pandas as pd
from pandas import DataFrame
import os
import networkx as nx
import matplotlib.pyplot as plt
from shutil import copyfile

th = Thread()
finished = False
mail = Mail()
mail.init_app(application)

def dir_last_updated(folder):
    print('dir:', os.getcwd())
    return str(max(os.path.getmtime(os.path.join(root_path, f))
               for root_path, dirs, files in os.walk(folder)
               for f in files))

@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html', title='Home')

@application.route('/details')
def details():
    return render_template('details.html', title='Details')

@application.route('/instructions')
def instructions():
    return render_template('instructions.html', title='Instructions')

@application.route('/about')
def about():
    return render_template('about.html', title='About')

@application.route('/contact', methods=['GET', 'POST'])
def contact():
    form = Contact()
    if form.validate_on_submit():
        subject = form.subject.data
        session['subject'] = subject
        msg = Message('Conflict Website: '+form.subject.data, sender=form.email.data, recipients=['francessduffy@gmail.com'])
        msg.body = "You have received the following message from {} <{}>: {}".format(form.name.data, form.email.data, form.message.data)
        mail.send(msg)
        return redirect(url_for('thanks'))
    return render_template('contact.html', title='Contact', form=form)

@application.route('/thanks')
def thanks():
    subject = session.get('subject', None)
    return render_template('thanks.html', title='Thanks', subject=subject)

@application.route('/options')
def options():
    return render_template('options.html', title='Options')

@application.route('/restart')
def restart():
    reset_files()
    return render_template('restart.html', title='Restart')

@application.route('/examples', methods=['GET', 'POST'])
def examples():
    form = ExamplesForm()
    if form.validate_on_submit():
        threemil = form.threemil.data
        twomil = form.twomil.data
        if threemil and twomil == True:
            return redirect(url_for('examples'))
        if threemil == True:
            os.remove('application/static/form1.csv')
            copyfile('application/static/examples/threemil_form1.csv', 'application/static/form1.csv')

            os.remove('application/static/regionvalues.csv')
            copyfile('application/static/examples/threemil_regionvalues.csv', 'application/static/regionvalues.csv')

            os.remove('application/static/communityvalues.csv')
            copyfile('application/static/examples/threemil_communityvalues.csv', 'application/static/communityvalues.csv')

            os.remove('application/static/militantvalues.csv')
            copyfile('application/static/examples/threemil_militantvalues.csv', 'application/static/militantvalues.csv')

            os.remove('application/static/communitypercents.csv')
            copyfile('application/static/examples/threemil_communitypercents.csv', 'application/static/communitypercents.csv')

            os.remove('application/static/boxlist.csv')
            copyfile('application/static/examples/threemil_boxlist.csv', 'application/static/boxlist.csv')

            os.remove('application/static/boxmlist.csv')
            copyfile('application/static/examples/threemil_boxmlist.csv', 'application/static/boxmlist.csv')

            os.remove('application/static/militantregionlist.csv')
            copyfile('application/static/examples/threemil_militantregionlist.csv', 'application/static/militantregionlist.csv')

            parameters = get_parameters()
            communitynames = parameters[9]
            regionnames = parameters[10]
            militantnames = parameters[11]
            boxlist = parameters[12]
            boxmlist = parameters[13]
            session['communitynames'] = communitynames
            session['regionnames'] = regionnames
            session['militantnames'] = militantnames
            session['boxlist'] = boxlist
            session['boxmlist'] = boxmlist

        if twomil == True:
            os.remove('application/static/form1.csv')
            copyfile('application/static/examples/twomil_form1.csv', 'application/static/form1.csv')

            os.remove('application/static/regionvalues.csv')
            copyfile('application/static/examples/twomil_regionvalues.csv', 'application/static/regionvalues.csv')

            os.remove('application/static/communityvalues.csv')
            copyfile('application/static/examples/twomil_communityvalues.csv', 'application/static/communityvalues.csv')

            os.remove('application/static/militantvalues.csv')
            copyfile('application/static/examples/twomil_militantvalues.csv', 'application/static/militantvalues.csv')

            os.remove('application/static/communitypercents.csv')
            copyfile('application/static/examples/twomil_communitypercents.csv', 'application/static/communitypercents.csv')

            os.remove('application/static/boxlist.csv')
            copyfile('application/static/examples/twomil_boxlist.csv', 'application/static/boxlist.csv')

            os.remove('application/static/boxmlist.csv')
            copyfile('application/static/examples/twomil_boxmlist.csv', 'application/static/boxmlist.csv')

            os.remove('application/static/militantregionlist.csv')
            copyfile('application/static/examples/twomil_militantregionlist.csv', 'application/static/militantregionlist.csv')

            parameters = get_parameters()
            communitynames = parameters[9]
            regionnames = parameters[10]
            militantnames = parameters[11]
            boxlist = parameters[12]
            boxmlist = parameters[13]
            session['communitynames'] = communitynames
            session['regionnames'] = regionnames
            session['militantnames'] = militantnames
            print('militantnames:', militantnames)
            session['boxlist'] = boxlist
            session['boxmlist'] = boxmlist
        return redirect(url_for('summary'))

    return render_template('examples.html', title='Examples', form=form)

@application.route('/start', methods=['GET', 'POST'])
def start():
    form = FirstForm()
    if form.validate_on_submit():
        numberregions = form.numberregions.data
        numbercommunities = form.numbercommunities.data
        numbermilitants = form.numbermilitants.data
        session['numberregions'] = numberregions
        session['numbercommunities'] = numbercommunities
        session['numbermilitants'] = numbermilitants
        session['count'] = 0
        form1 = DataFrame({'totalpopulation': form.totalpopulation.data, 'numberregions': form.numberregions.data, 'numbercommunities': form.numbercommunities.data, 'numbermilitants': form.numbermilitants.data, 'l': form.l.data, 'm': form.m.data, 'h': form.h.data, 'extortionrate': form.extortionrate.data, 'civsupportrate': form.civsupportrate.data, 'terrorfactor': form.terrorfactor.data}, index=[0])
        form1 = form1[['totalpopulation', 'numberregions', 'numbercommunities', 'numbermilitants', 'l', 'm', 'h', 'extortionrate', 'civsupportrate', 'terrorfactor']]
        form1.to_csv('application/static/form1.csv', index=False)
        return redirect(url_for('page2'))
    return render_template('start.html', title='Start Simulator', form=form)

@application.route('/page2', methods=['GET', 'POST'])
def page2():
    numberregions = int(session.get('numberregions', None))
    numbercommunities = int(session.get('numbercommunities', None))
    numbermilitants = int(session.get('numbermilitants', None))
    count = session.get('count', None)
    form = SecondForm()
    if form.validate_on_submit():
        regiondata = form.regions.data
        communitydata = form.communities.data
        militantdata = form.militants.data
        regionvalues = []
        regionnames = []
        for i in regiondata:
            regionnames.append(i['regionname'])
            regionvalues.append([i['regionname'], i['regpercent'], i['weapons']])
        communityvalues = []
        communitynames = []
        for i in communitydata:
            communitynames.append(i['communityname'])
            communityvalues.append([i['communityname'], i['l'], i['m'], i['h']])
        militantvalues = []
        militantnames = []
        for i in militantdata:
            militantnames.append(i['militantname'])
            militantvalues.append([i['militantname'], i['extincome'], i['initstrength'], i['benefitcutoff'], i['terrorist']])
        regionvalues = pd.DataFrame(regionvalues, columns=['regionname', 'regpercent', 'weapons'], index=None)
        communityvalues = pd.DataFrame(communityvalues, columns=['communityname', 'l', 'm', 'h'], index=None)
        militantvalues = pd.DataFrame(militantvalues, columns=['militantname', 'extincome', 'initstrength', 'benefitcutoff', 'terrorist'], index=None)
        regionvalues.to_csv('application/static/regionvalues.csv')
        communityvalues.to_csv('application/static/communityvalues.csv')
        militantvalues.to_csv('application/static/militantvalues.csv')
        session['regionnames'] = regionnames
        session['communitynames'] = communitynames
        session['militantnames'] = militantnames
        session['count'] = 0
        return redirect(url_for('page3'))
    if count == 0:
        for i in range(numberregions):
            form.regions.append_entry()
            session['count'] = 1
        for i in range(numbercommunities):
            form.communities.append_entry()
        for i in range(numbermilitants):
            form.militants.append_entry()
    return render_template('page2.html', title='Second Page', form=form, numberregions=numberregions, numbercommunities=numbercommunities, numbermilitants=numbermilitants)

@application.route('/page3', methods=['GET', 'POST'])
def page3():
    regionnames = session.get('regionnames', None)
    communitynames = session.get('communitynames', None)
    militantnames = session.get('militantnames', None)
    count = session.get('count', None)

    region_percent_list = []
    for i in regionnames:
        for j in communitynames:
            region_percent_list.append('% population of ' + i + ' belonging to ' + j + ':')
    community_label_list = []
    for i in communitynames:
        for j in communitynames:
            if i != j:
                community_label_list.append(i + ' against ' + j + ':')
    affiliation_label_list = []
    for i in communitynames:
        for j in militantnames:
            affiliation_label_list.append(i + ' with ' + j + ':')
    region_label_list = []
    for i in militantnames:
        for j in regionnames:
            region_label_list.append(i + ' in ' + j + ':')

    form = ThirdForm()
    if form.validate_on_submit():
        try:
            data = form.regionpercent.data
            data2 = form.grievances.data
            data3 = form.affiliations.data
            data4 = form.milactive.data

            communitypercents = []
            x = 0
            while x < len(data):
                count = 0
                percents = []
                while count < len(communitynames):
                    percents.append(data[x]['x'])
                    count += 1
                    x += 1
                communitypercents.append(percents)
            boxlist = []
            x = 0
            while x < len(data2):
                count = 0
                boxes = []
                while count < (len(communitynames)-1):
                    boxes.append(data2[x]['box'])
                    count += 1
                    x += 1
                boxlist.append(boxes)
            boxmlist = []
            x = 0
            while x < len(data3):
                count = 0
                boxes = []
                while count < len(militantnames):
                    boxes.append(data3[x]['boxm'])
                    count += 1
                    x += 1
                boxmlist.append(boxes)
            militantregionlist = []
            x = 0
            while x < len(data4):
                count = 0
                milactive = []
                while count < len(regionnames):
                    milactive.append(data4[x]['reg'])
                    count += 1
                    x += 1
                militantregionlist.append(milactive)
            session['boxlist'] = boxlist
            session['boxmlist'] = boxmlist

            communitypercents = pd.DataFrame(communitypercents, columns=None, index=None)
            boxlist = pd.DataFrame(boxlist, columns=None, index=None)
            boxmlist = pd.DataFrame(boxmlist, columns=None, index=None)
            militantregionlist = pd.DataFrame(militantregionlist, columns=None, index=None)

            communitypercents.to_csv('application/static/communitypercents.csv')
            boxlist.to_csv('application/static/boxlist.csv')
            boxmlist.to_csv('application/static/boxmlist.csv')
            militantregionlist.to_csv('application/static/militantregionlist.csv')

        except ValueError:
            return redirect(url_for('error'))
        return redirect(url_for('summary'))
    if count == 0:
        for i in range(len(regionnames)*len(communitynames)):
            form.regionpercent.append_entry()
            session['count'] = 1
        for i in range(len(communitynames)*(len(communitynames)-1)):
            form.grievances.append_entry()
        for i in range(len(communitynames)*len(militantnames)):
            form.affiliations.append_entry()
        for i in range(len(regionnames)*len(militantnames)):
            form.milactive.append_entry()
    return render_template('page3.html', title='Third Page', form=form, region_percent_list=region_percent_list, community_label_list=community_label_list, affiliation_label_list=affiliation_label_list, region_label_list=region_label_list)

@application.route('/summary', methods=['GET', 'POST'])
def summary():
    try:
        print('entered summary')
        regionnames = session.get('regionnames', None)
        communitynames = session.get('communitynames', None)
        militantnames = session.get('militantnames', None)
        boxlist = session.get('boxlist', None)
        boxmlist = session.get('boxmlist', None)
        number_coms = len(communitynames)
        crop = False
        if number_coms == 2:
            crop = True
        grievances = []
        z = 0
        for i in boxlist:
            list = []
            x = 0
            for j in i:
                y = 0
                if j == True:
                    y = 1
                else:
                    y = 0
                if z == x:
                    list.append(0)
                    list.append(y)
                else:
                    list.append(y)
                x += 1
            grievances.append(list)
            z += 1
        grievances[len(grievances) - 1].append(0)
        grievances = pd.DataFrame(grievances, columns=communitynames, index=communitynames)
        grievances.transpose()
        numpy_grievances = grievances.values
        network = nx.DiGraph(numpy_grievances)
        pos = nx.circular_layout(network)
        x = 0
        keys = []
        for i in communitynames:
            keys.append(x)
            x += 1
        labels = dict(zip(keys, communitynames))
        pos_attrs = {}
        for node, coords in pos.items():
            pos_attrs[node] = (coords[0], coords[1] + .1)
        nx.draw_networkx_nodes(network, pos, node_color='orange')
        nx.draw_networkx_edges(network, pos, arrowsize=30, edge_color='gray')
        nx.draw_networkx_labels(network, pos, labels, font_size=12, font_weight='bold')
        plt.box(False)
        plt.savefig("application/static/network.png")
        plt.clf()
        affiliations = []
        for i in boxmlist:
            list = []
            for j in i:
                y = 0
                if j == True:
                    y = 1
                else:
                    y = 0
                list.append(y)
            affiliations.append(list)
        affiliations = pd.DataFrame(affiliations, columns=militantnames, index=communitynames)
        form = FourthForm()
    except ValueError:
        return redirect(url_for('error'))
    if form.validate_on_submit():
        form4 = DataFrame({'supported_militants': form.supported_militants.data, 'opposed_militants': form.opposed_militants.data, 'negotiate': form.negotiate.data, 'negotiate2': form.negotiate2.data, 'mil1': form.mil1.data, 'mil2': form.mil2.data, 'infocampaign': form.infocampaign.data, 'supportmilgov': form.supportmilgov.data, 'civwealth': form.civwealth.data, 'wealthregions': form.wealthregions.data, 'wealthcomms': form.wealthcomms.data, 'commbenefits': form.commbenefits.data, 'milbenefits': form.milbenefits.data, 'civbenefits': form.civbenefits.data, 'fundmil': form.fundmil.data, 'fundmilamt': form.fundmilamt.data, 'cutoff': form.cutoff.data, 'cutoffamt': form.cutoffamt.data, 'attack': form.attack.data, 'punish': form.punish.data, 'weapons': form.weapons.data, 'weaponsregions': form.weaponsregions.data, 'trainequip': form.trainequip.data, 'protect': form.protect.data}, index=[0])
        form4.to_csv('application/static/form4.csv')
        return redirect(url_for('results2'))
    return render_template('summary.html', last_updated=dir_last_updated('application/static'), title='Summary', table1=grievances.to_html(classes='grievances'), table2=affiliations.to_html(classes='affiliations'), form=form, regionnames=regionnames, communitynames=communitynames, militantnames=militantnames, crop=crop)

# @application.route('/processing')
# def processing():
#     global th
#     global finished
#     finished = False
#     th = Thread(target=launch_simulator())
#     th.start()
#     return render_template('processing.html', title='Processing')

@application.route('/results2')
def results2():
    try:
        from application.model.reset_variables import reset_variables
        from application.run_simulator_nonredis2 import simulator2
        reset_variables()
        data = simulator2()
    except:
        return redirect(url_for('error'))
    data.to_csv('test.csv', index=False)
    regionnames = session.get('regionnames', None)
    communitynames = session.get('communitynames', None)
    militantnames = session.get('militantnames', None)
    militants = len(militantnames)
    communities = len(communitynames)
    df = pd.read_csv('test.csv')
    results_dataframes = calculations(df, militants, communities, militantnames, communitynames)
    summary_data = summary_results(results_dataframes, militantnames)
    strength_df = results_dataframes[0]
    ranked_by_strength_df = results_dataframes[1]
    fighting_df = results_dataframes[2]
    defending_df = results_dataframes[3]
    strength_labels = results_dataframes[4]
    fighting_labels = results_dataframes[5]
    defending_labels = results_dataframes[6]
    strongest_militant_name = summary_data[0]
    strongest_militant_strength = summary_data[1]
    fighting_average_change = summary_data[2]
    defending_total_change = summary_data[3]
    fightingchange = summary_data[4]
    fightingpre = summary_data[5]
    fightingpost = summary_data[6]
    defendingchange = summary_data[7]
    try:
        graphing(df, strength_labels, fighting_labels, defending_labels)
    except:
        return redirect(url_for('error'))
    return render_template('results2.html', last_updated=dir_last_updated('/opt/python/current/app/application/static'), table1=ranked_by_strength_df.to_html(classes='rankedstrength'), table2=fighting_df.to_html(classes='fighting'), table3=defending_df.to_html(classes='defending'), strongestmname = strongest_militant_name, strongestm = strongest_militant_strength, fightingave = fighting_average_change, defendingtot = defending_total_change, fightingchange = fightingchange, fightingpre = fightingpre, fightingpost = fightingpost, defendingchange = defendingchange)

@application.route('/progress')
def check_progress():
    progress = get_progress()
    if progress == 100:
        finished = True
    return jsonify(dict(status=('finished' if finished else 'running')))

@application.route('/error')
def error():
    return render_template('error.html', title='Error')

@application.route('/results')
def results():
    regionnames = session.get('regionnames', None)
    communitynames = session.get('communitynames', None)
    militantnames = session.get('militantnames', None)
    militants = len(militantnames)
    communities = len(communitynames)
    df = pd.read_csv('test.csv')
    try:
        results_dataframes = calculations(df, militants, communities, militantnames, communitynames)
    except ValueError:
        return redirect(url_for('error'))
    try:
        summary_data = summary_results(results_dataframes, militantnames)
    except ValueError:
        return redirect(url_for('error'))
    strength_df = results_dataframes[0]
    ranked_by_strength_df = results_dataframes[1]
    fighting_df = results_dataframes[2]
    defending_df = results_dataframes[3]
    strength_labels = results_dataframes[4]
    fighting_labels = results_dataframes[5]
    defending_labels = results_dataframes[6]
    strongest_militant_name = summary_data[0]
    strongest_militant_strength = summary_data[1]
    fighting_average_change = summary_data[2]
    defending_total_change = summary_data[3]
    fightingchange = summary_data[4]
    fightingpre = summary_data[5]
    fightingpost = summary_data[6]
    defendingchange = summary_data[7]

    try:
        graphing(df, strength_labels, fighting_labels, defending_labels)
    except ValueError:
        return redirect(url_for('error'))
    reset_files()
    return render_template('results.html', last_updated=dir_last_updated('/opt/python/current/app/application/static'), table1=ranked_by_strength_df.to_html(classes='rankedstrength'), table2=fighting_df.to_html(classes='fighting'), table3=defending_df.to_html(classes='defending'), strongestmname = strongest_militant_name, strongestm = strongest_militant_strength, fightingave = fighting_average_change, defendingtot = defending_total_change, fightingchange = fightingchange, fightingpre = fightingpre, fightingpost = fightingpost, defendingchange = defendingchange)
