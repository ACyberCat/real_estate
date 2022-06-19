# Odoo ERP Documentation Examples and Explanations

## Chapter 1: Architecture Overview

- Odoo is a multitier application, meaning that it is composed of several modules. Each module is responsible for a specific part of the application. For example, the `base` module is responsible for the core of the application, while the `sale` module is responsible for sales.
- Odoo is composed of 3 main layers:
  - The Data Layer: The data layer is the main entry point to the database. It is responsible for the creation, modification, and deletion of data.
  - The Logic Layer: The Logic Layer coordinates the application, process commands, and performs calculations. It also is responsible for the creation, modification, and deletion of data.
  - The User Interface Layer: The User Interface Layer is responsible for the display of data. It translates the data into a format that is easy to read and easy to use.

## Chapter 2: Developer Environment setup

#### - Odoo's installer includes all the required dependencies to run the application and its accompanying modules and services, including but not limited to

- Python 3.7
- PostgreSQL
- Nginx
- Odoo
- Odoo Server
- Odoo Client
- Odoo Server Admin
- Odoo Server Worker
- Odoo Server Web

- Odoo's installer also includes a configuration file, `odoo.conf`, that contains the necessary information to run the application.

## Chapter 3: Creating a new application/module

> ##### - To create a new application, you must first create a new directory at C:\Program Files\odoo15\server\odoo\addons
>
> ##### - Then, you must create two new files in the new directory, and name them **`__init__.py`** and **`__manifest__.py`** accordingly
>
> ##### - The **`__init__.py`** file is required to call the base module, and the **`__manifest__.py`** file is required to contain the following information
>
> > - **name**: The name of the module.
> > - **version**: The version of the module.
> > - **author**: The author of the module.
> > - **description**: The description of the module.
> > - **depends**: The modules that the module depends on.
> > - **category**: The category of the module.
> > - **sequence**: The sequence of the module.
> > - **summary**: The summary of the module.
> > - **data**: The data files that the module contains.
> > - **application**: The application that the module contains.
> > - **installable**: Whether the module is installable or not.
> > - **auto_install**: Whether the module is auto-installable or not.

> ### Or you can do the following command in the terminal to create the basic skeleton for module creation
>
> ###### `> cd C:\Program Files\odoo15\server\python`
>
> ###### `> python.exe "C:\Program Files\odoo15\server\odoo" scaffold <module_name> "C:\Program Files\odoo15\server\odoo\addons"`

> ###### _note: When changing functions in the model it is more than enough to restart the Odoo service, but if you were editing the model data structure thereby editing the database it creates, then you must uninstall and reinstall the module since the previous records are now incompatible with the new model fields where it has null where the new columns have been added._
>
> _**Editing XML views can be seen after a simple upgrade to the already installed app module**_

## Chapter 4: Models and Basic Fields

- Models are the main data structure in Odoo. They are used to create and store data in tables in the database.

  > ###### _note: Odoo uses PostgreSQL for its database due to it being a relational database_

  > - Models are created by creating a new file in the `models` directory.
  > - **The `models` directory must include an `__init__.py` file.**
  > - Each model has model fields that are the actual columns in the database table.
  > - Each field has a type, which is a string that corresponds to the type of data that is stored in the field. For example, the `char` type is used to store strings, the `integer` type is used to store integers, and the `boolean` type is used to store booleans. These types directly correspond to SQL's data types.

### Start off by importing from Odoo the required dependencies
### > `from odoo import exceptions, api, fields, models`
> ###### _The `exceptions` module is used to throw exceptions._
> ###### _The `api` module is used to call Odoo's API. The `fields` module is used to create model fields._
> ###### _The `models` module is used to create models._
### Creating the module
>### Create the Class for the Model
>
> >#### `class <model_name>(models.Model):`
> ### Add the fields to the model
> > **`_name = '<model_name>'`**
> > **`_description = '<model_description>'`**
> > **`_inherit = '<model_inherit>'`**
> > **`_order = '<model_order>'`**
> > **`_sql_constraints = [('<model_constraint_name>', '<model_constraint_type>', '<model_constraint_message>')]`**
> >**`_inherits = {'<model_inherit_name>': '<model_inherit_field>'}`**
>>> ###### _note: The `_inherit` attribute is used to inherit fields from another model._
>>> ###### _Also, `inherit` results in a different config than `inherits`._

> ### Create the data fields depending on your requirements and needs, but the general format is
>
> > #### `<name_of_field> = fields.<type_of_field>(<field_attributes>)`
>
> #### Types of fields include but are not limited to
>
> > - **fields.Char**: Stores strings.
> > - **fields.Text**: Stores strings.
> > - **fields.Integer**: Stores integers.
> > - **fields.Float**: Stores floats.
> > - **fields.Boolean**: Stores booleans.
> > - **fields.Date**: Stores dates.
> > - **fields.Datetime**: Stores datetimes.
> > - **fields.Time**: Stores times.
> > - **fields.Binary**: Stores binary data.
> > - **fields.Many2one**: Stores a many-to-one relationship.
> > - **fields.One2many**: Stores a one-to-many relationship.
> > - **fields.Many2many**: Stores a many-to-many relationship.
> > - **fields.Reference**: Stores a reference to another model.
> > - **fields.Selection**: Stores a selection of values.
> > >##### _note: `fields.Many2One` require a corresponding `fields.One2Many` field in the other model and vice versa._
> #### Attributes for each field include but are not limited to
>
> > - _**default**_ = "(default value)" # default value for the field
> > - _**string**_ = "(String)" # name of the field that will be visible to user
> > - _**help**_ = "(String)" # help message for the field when it is displayed
> > - _**readonly**_ = "(Boolean)" # whether the field is readonly or not
> > - _**required**_ = "(Boolean)" # whether the field can be null or not
> > - _**selection**_ = "([Array])" # selection of values for the field
> > - _**copy**_ = "(Boolean)" # whether the field is copied or not
> > - _**compute**_ = "(lambda self: expression)" # compute function for the field
> > - _**store**_ = "(Boolean)" # whether the field is stored in the database or not

###### _This Documentation was created with the help of Github Copilot._
