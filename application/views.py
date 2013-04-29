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


def survey():
    form = SurveyForm()
    if form.validate_on_submit():
        survey = Survey(
            sex=form.sex.data,
            gap_one=int(form.gap_one.data),
            importance_one=int(form.importance_one.data),
            gap_two=int(form.gap_two.data),
            importance_two=int(form.importance_two.data)
        )
        try:
            survey.put()
            flash(u'Thank you', 'success')
            return redirect(url_for('home'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'info')
            return redirect(url_for('list_examples'))
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


