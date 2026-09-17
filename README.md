<div align="center">
    <h1 align="center">plone.formwidget.ploneicons</h1>
</div>
<div align="center">
[![PyPI](https://img.shields.io/pypi/v/plone.formwidget.ploneicons)](https://pypi.org/project/plone.formwidget.ploneicons/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/plone.formwidget.ploneicons)](https://pypi.org/project/plone.formwidget.ploneicons/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/plone.formwidget.ploneicons)](https://pypi.org/project/plone.formwidget.ploneicons/)
[![PyPI - License](https://img.shields.io/pypi/l/plone.formwidget.ploneicons)](https://pypi.org/project/plone.formwidget.ploneicons/)
[![PyPI - Status](https://img.shields.io/pypi/status/plone.formwidget.ploneicons)](https://pypi.org/project/plone.formwidget.ploneicons/)


[![PyPI - Plone Versions](https://img.shields.io/pypi/frameworkversions/plone/plone.formwidget.ploneicons)](https://pypi.org/project/plone.formwidget.ploneicons/)

[![CI](https://github.com/collective/plone.formwidget.ploneicons/actions/workflows/main.yml/badge.svg)](https://github.com/collective/plone.formwidget.ploneicons/actions/workflows/main.yml)
![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000)

[![GitHub contributors](https://img.shields.io/github/contributors/collective/plone.formwidget.ploneicons)](https://github.com/collective/plone.formwidget.ploneicons)
[![GitHub Repo stars](https://img.shields.io/github/stars/collective/plone.formwidget.ploneicons?style=social)](https://github.com/collective/plone.formwidget.ploneicons)

</div>

A widget for Plone that shows all available plone icons and can be selected to save its value in a field

## Features

- **Icon Selector**: A searchable modal gallery to pick icons from the Plone registry.
- **Plone 6 Integration**: Uses native Plone icon resolution and Patternslib.
- **DataGridField Compatible**: Works out-of-the-box inside `collective.z3cform.datagridfield`.

## Usage

### In a Schema

You can use the widget in your Dexterity content types or behaviors.

```python
from plone.autoform import directives
from plone.formwidget.ploneicons.widget import PloneIconsFieldWidget
from plone.supermodel import model
from zope import schema


class IMyContent(model.Schema):
    # Saves "alarm"
    directives.widget("icon_name", PloneIconsFieldWidget)
    icon_name = schema.TextLine(
        title="Icon Name",
        required=False,
    )
```

### Displaying the Icon

In your templates, you can render the icon using Plone's native icon resolver to get the icon's URL or SVG. See the [official Plone documentation on icons](https://6.docs.plone.org/classic-ui/icons.html#get-an-icon-s-url-via-python-expression) for more details.

## Installation

Install plone.formwidget.ploneicons with `pip`:

```shell
pip install plone.formwidget.ploneicons
```

And to create the Plone site:

```shell
make create-site
```

## Contribute

- [Issue tracker](https://github.com/collective/plone.formwidget.ploneicons/issues)
- [Source code](https://github.com/collective/plone.formwidget.ploneicons/)

### Prerequisites ✅

-   An [operating system](https://6.docs.plone.org/install/create-project-cookieplone.html#prerequisites-for-installation) that runs all the requirements mentioned.
-   [uv](https://6.docs.plone.org/install/create-project-cookieplone.html#uv)
-   [Make](https://6.docs.plone.org/install/create-project-cookieplone.html#make)
-   [Git](https://6.docs.plone.org/install/create-project-cookieplone.html#git)
-   [Docker](https://docs.docker.com/get-started/get-docker/) (optional)

### Installation 🔧

1.  Clone this repository, then change your working directory.

    ```shell
    git clone git@github.com:collective/plone.formwidget.ploneicons.git
    cd plone.formwidget.ploneicons
    ```

2.  Install this code base.

    ```shell
    make install
    ```

## Development 🛠️

### Building the JavaScript bundle

The JavaScript for the icon selector pattern is located in the `resources` directory and must be compiled into a bundle before it can be used by Plone.

1.  Ensure you have [Node.js](https://nodejs.org/) installed.
2.  Install the npm dependencies:

    ```shell
    npm install
    ```

3.  Build the bundle:

    ```shell
    npm run build
    ```

    This will create the compiled files in `src/plone/formwidget/ploneicons/browser/static/bundles`.

4.  For development, you can use the watch mode to automatically rebuild on changes:

    ```shell
    npm run watch
    ```

### Internationalization (i18n)

To update the translation files after changing strings in templates or Python code:

```shell
make i18n
```


### Add features using `plonecli` or `bobtemplates.plone`

This package provides markers as strings (`<!-- extra stuff goes here -->`) that are compatible with [`plonecli`](https://github.com/plone/plonecli) and [`bobtemplates.plone`](https://github.com/plone/bobtemplates.plone).
These markers act as hooks to add all kinds of subtemplates, including behaviors, control panels, upgrade steps, or other subtemplates from `plonecli`.

To run `plonecli` with configuration to target this package, run the following command.

```shell
make add <template_name>
```

For example, you can add a content type to your package with the following command.

```shell
make add content_type
```

You can add a behavior with the following command.

```shell
make add behavior
```

```{seealso}
You can check the list of available subtemplates in the [`bobtemplates.plone` `README.md` file](https://github.com/plone/bobtemplates.plone/?tab=readme-ov-file#provided-subtemplates).
See also the documentation of [Mockup and Patternslib](https://6.docs.plone.org/classic-ui/mockup.html) for how to build the UI toolkit for Classic UI.
```

## License

The project is licensed under GPLv2.

## Credits and acknowledgements 🙏

Generated using [Cookieplone (2.0.0)](https://github.com/plone/cookieplone) and [cookieplone-templates (4d90eb9)](https://github.com/plone/cookieplone-templates/commit/4d90eb9e774e500c643a0aabb140b3a158437a25) on 2026-09-17 11:08:19.887369. A special thanks to all contributors and supporters!
