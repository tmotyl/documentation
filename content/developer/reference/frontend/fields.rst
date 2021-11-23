
======
Fields
======

In Odoo, the word *field* is mostly used to denote a part of a model, usually
represented by a column in a database. Fields are represented by components in
the user interface (mostly in the form, kanban and list view). In this page, we document
how these field components work and how to use them.

How to define a field
=====================

Fields are simply owl components registered in the fields registry.

.. code-block:: javascript

    import { registry } from "@web/core/registry";
    const { Component } = owl;
    const { xml } = owl.tags;

    class CounterField extends Component {
        increment() {
            if (!this.props.readonly) {
                this.props.update(this.props.value + 1);
            }
        }
    }
    CounterField.template = xml`
        <div t-on-click="increment">
            <t t-esc="props.value">
        </div>
    `;

    registry.category("fields").add("counter", CounterField);

The component of a field receives several props:

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - `archs`
     - `object?`
     - description...
   * - `attrs`
     - `object`
     - description...
   * - `id`
     - `string?`
     - description...
   * - `name`
     - `string`
     - The field's name
   * - `options`
     - `object`
     - description...
   * - `readonly`
     - `boolean`
     - description...
   * - `required`
     - `boolean`
     - description...
   * - `record`
     - `DataPoint`
     - description...
   * - `type`
     - `string`
     - The field's base type.
   * - `update`
     - `function`
     - description...
   * - `value`
     - `any`
     - description...


How to use a field
==================

.. code-block:: xml

    <Field name="'my_field'" record="getRecord()" type="'counter'" readonly="true" required="false" />

Reference List
==============

.. list-table::
   :widths: 15 20 20 45
   :header-rows: 1

   * - Name
     - Technical name
     - Type
     - Short Description
   * - :ref:`BooleanField <frontend/fields/boolean_field>`
     - `boolean`
     - `boolean`
     - Displays a checkbox

.. _frontend/fields/boolean_field:

BooleanField
------------

- Location: `@web/fields/boolean_field`
- Technical name: `boolean`
- Supported types: `boolean`

The `BooleanField` component represents a boolean value. It is the default field
for all fields of type `boolean`.

.. code-block:: xml

    <field name="my_field" widget="boolean" />

.. _frontend/fields/other_field:
