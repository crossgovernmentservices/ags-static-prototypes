# ags-static-prototypes

Port of [flask_prototyping](https://github.com/colmjude/flask_prototyping)

A simple Python flask prototyping tool.

### Building blocks

To get some pages up and running quickly it make use of the 3 GOVUK frontend building blocks.

* [govuk_template](https://github.com/alphagov/govuk_template) - template containing the GOV.UK header and footer, and associated assets
* [govuk_frontend_toolkit](https://github.com/alphagov/govuk_frontend_toolkit) - collection of Sass & JS
* [govuk_elements](https://github.com/alphagov/govuk_elements) - design guide and example (adds some Sass components)

### Setup

Requires you to have Ruby 2.2.0 or higher

Running in a virtualenv is advised. To create one, with Python 3, run

```
mkvirtualenv --python=`which python3` <name>
```
(agsstatic might be a good name)

When returning run `workon <name>` to activate the virtualenv you just created.

Then install the dependencies

```
pip install -r requirements.txt
gem install bundle
```

We then need to fetch the latest GOVUK assets

```
python manage.py install_all_govuk_assets --app-dir application
```

Then you should be ready to run it

```
python manage.py runserver
```

Follow the instructions returned on the commandline to view it in your browser


### Deploying to Heroku

For basic heroku instructions [see here](https://github.com/alphagov/govuk_prototype_kit/wiki/Deploying-(getting-your-work-online\))

There are a couple of additional steps required to deploy this project.

Because it is a python app that also requires ruby to compile the .scss files it needs multiple buildpacks. Luckily someone has made this easy for us, we just need to use the [heroku-buildpack-multi](https://github.com/ddollar/heroku-buildpack-multi)

Add a `.buildpack` file containing the 2 buildpacks

And then let Heroku know we are using this. We do that by entering this on the commandline

```
heroku buildpacks:set https://github.com/ddollar/heroku-buildpack-multi.git
```
