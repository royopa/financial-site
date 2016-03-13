# project/server/cdi/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, url_for, \
    redirect, flash, request

from project.server import bcrypt, db
from project.server.models import Cdi, User

import csv
import datetime

################
#### config ####
################

cdi_blueprint = Blueprint('cdi', __name__,)


################
#### routes ####
################

@cdi_blueprint.route('/cdi/load/<year>', methods=['GET', 'POST'])
def load(year=2016):
    ano = year
    path = 'C:/c090762/projects/flask-skeleton/project/server/cdi/CDI_'+str(ano)+'.csv'
    csvfile = open(path, "r")
    reader = csv.reader(csvfile)
    for row in reader:
        if row[1] == 'CDI':
            continue
        data = datetime.datetime.strptime(row[0], '%Y%m%d').date()
        taxa = row[1].strip()
        taxa = float(taxa[:7]+'.'+taxa[-2:])

        cdi = Cdi(
            data=data,
            taxa=taxa
        )

        db.session.add(cdi)
        db.session.commit()

    return render_template('cdi/loaded.html', cdi=reader)


@cdi_blueprint.route('/cdi/list', methods=['GET', 'POST'])
def list():
    list = Cdi.query.order_by(Cdi.data).all()
    list.reverse()

    return render_template('cdi/list.html', list=list)
