# Domain Model: plone.formwidget.ploneicons

## Glossary

### Icon Name
the short identifier for an icon in the Plone registry (e.g., `alarm`). Derived from registry keys starting with `plone.icon.`.

### Icon Class
The CSS class used to render the icon in the frontend (e.g., `bi-alarm`). Usually formed by prepending a prefix to the **Icon Name**.

### Icon Selector
The interactive UI component (Modal Gallery) used to browse and pick an icon.

### Icon Widget
The Plone/z3c.form component that bridges the backend field with the **Icon Selector**.
