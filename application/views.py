"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""

import os
import logging

from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from google.appengine.ext import db

from application import app

from flask import render_template, flash, url_for, redirect, request

from werkzeug import secure_filename

from models import Survey
from decorators import admin_required
from forms import SurveyForm


def home():
    return render_template('home.html', nav='home')


def thankyou():
    return render_template('thankyou.html', nav='thankyou')


def survey():
    form = SurveyForm()
    if form.validate_on_submit():

        if form.purchase_online.data == 'false':
            last_purchase = 'none'
            purchase_frequency = 'none'
        else:
            last_purchase = form.last_purchase.data
            purchase_frequency = form.purchase_frequency.data

        survey = Survey(
            sex=form.sex.data,
            comment=form.comment.data,
            age=form.age.data,
            martial_status=form.martial_status.data,
            internet_usage=form.internet_usage.data,
            internet_frequency=form.internet_frequency.data,
            purchase_online=form.purchase_online.data,
            purchase_frequency=purchase_frequency,
            last_purchase=last_purchase,
            employment_status=form.employment_status.data,
            income_range=form.income_range.data,
            q01_1=int(form.q01_1.data),
            q01_2=int(form.q01_2.data),
            q02_1=int(form.q02_1.data),
            q02_2=int(form.q02_2.data),
            q03_1=int(form.q03_1.data),
            q03_2=int(form.q03_2.data),
            q04_1=int(form.q04_1.data),
            q04_2=int(form.q04_2.data),
            q05_1=int(form.q05_1.data),
            q05_2=int(form.q05_2.data),
            q06_1=int(form.q06_1.data),
            q06_2=int(form.q06_2.data),
            q07_1=int(form.q07_1.data),
            q07_2=int(form.q07_2.data),
            q08_1=int(form.q08_1.data),
            q08_2=int(form.q08_2.data),
            q09_1=int(form.q09_1.data),
            q09_2=int(form.q09_2.data),
            q10_1=int(form.q10_1.data),
            q10_2=int(form.q10_2.data),
            q11_1=int(form.q11_1.data),
            q11_2=int(form.q11_2.data),
            q12_1=int(form.q12_1.data),
            q12_2=int(form.q12_2.data),
            q13_1=int(form.q13_1.data),
            q13_2=int(form.q13_2.data),
            q14_1=int(form.q14_1.data),
            q14_2=int(form.q14_2.data),
            q15_1=int(form.q15_1.data),
            q15_2=int(form.q15_2.data),
            q16_1=int(form.q16_1.data),
            q16_2=int(form.q16_2.data),
            q17_1=int(form.q17_1.data),
            q17_2=int(form.q17_2.data),
            q18_1=int(form.q18_1.data),
            q18_2=int(form.q18_2.data),
            q19_1=int(form.q19_1.data),
            q19_2=int(form.q19_2.data),
            q20_1=int(form.q20_1.data),
            q20_2=int(form.q20_2.data),
            q21_1=int(form.q21_1.data),
            q21_2=int(form.q21_2.data),
            q22_1=int(form.q22_1.data),
            q22_2=int(form.q22_2.data),
            q23_1=int(form.q23_1.data),
            q23_2=int(form.q23_2.data),
            q24_1=int(form.q24_1.data),
            q24_2=int(form.q24_2.data),
            q25_1=int(form.q25_1.data),
            q25_2=int(form.q25_2.data),
            q26_1=int(form.q26_1.data),
            q26_2=int(form.q26_2.data),
            q27_1=int(form.q27_1.data),
            q27_2=int(form.q27_2.data)
        )
        try:
            survey.put()
            flash(u'Thank you', 'success')
            return redirect(url_for('thankyou'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'info')
            return redirect(url_for('home'))
    return render_template('survey.html', form=form)

"""
@admin_required
def list_apps():
    apps = AdNetwork.all()
    form = AppForm()
    if form.validate_on_submit():
         file = request.files['app_url']
         if file:
            filedata = file.read()
            ext = file.filename.rsplit('.', 1)[1]
            content_type = file.content_type
            app_filename = file.filename
            applist = AdNetwork(
                app_title = request.form['app_title'],
                app_category = request.form['app_category'],
                app_name = app_filename,
                app_url = db.Blob(filedata),
                ext = ext,
                content_type = content_type,
                app_link = request.form['app_link'],
                new = form.new.data,
                exclusive =  form.exclusive.data
            )
            try:
                applist.put()
                app_id = applist.key().id()
                flash(u'App Profile is %s successfully saved.' % app_id, 'success')
                return redirect(url_for('apps'))
            except CapabilityDisabledError:
                flash(u'App Engine Datastore is currently in read-only mode.', 'info')
                return redirect(url_for('apps'))
         return render_template('list_apps.html', apps=apps, form=form)
    return render_template('list_apps.html', apps=apps, form=form)

@admin_required
def delete_app(app_id):
    "Delete an example object""
    app = AdNetwork.get_by_id(app_id)
    try:
        app.delete()
        flash(u'App %s successfully deleted.' % app_id, 'success')
        return redirect(url_for('apps'))
    except CapabilityDisabledError:
        flash(u'App Engine Datastore is currently in read-only mode.', 'info')
        return redirect(url_for('apps'))


@admin_required
def delete_newsletter(newsletter_id):
    "Delete an example object""
    newsletter = Newsletter.get_by_id(newsletter_id)
    try:
        newsletter.delete()
        flash(u'Newsletter %s successfully deleted.' % newsletter_id, 'success')
        return redirect(url_for('list_newsletters'))
    except CapabilityDisabledError:
        flash(u'App Engine Datastore is currently in read-only mode.', 'info')
        return redirect(url_for('list_newsletters'))


@admin_required
def list_examples():
    "List all examples""
    examples = ExampleModel.all()
    form = ExampleForm()
    if form.validate_on_submit():
        example = ExampleModel(
            example_name = form.example_name.data,
            example_description = form.example_description.data,
            added_by = users.get_current_user()
        )
        try:
            example.put()
            example_id = example.key().id()
            flash(u'Example %s successfully saved.' % example_id, 'success')
            return redirect(url_for('list_examples'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'info')
            return redirect(url_for('list_examples'))
    return render_template('list_examples.html', examples=examples, form=form)


@admin_required
def delete_example(example_id):
    "Delete an example object""
    example = ExampleModel.get_by_id(example_id)
    try:
        example.delete()
        flash(u'Example %s successfully deleted.' % example_id, 'success')
        return redirect(url_for('list_examples'))
    except CapabilityDisabledError:
        flash(u'App Engine Datastore is currently in read-only mode.', 'info')
        return redirect(url_for('list_examples'))


@admin_required
def admin_only():
    return redirect(url_for('list_newsletters'))
"""


def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''


