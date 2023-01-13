# Django Laboratory
A Django app for managing collections of scientific instruments

## About

Django Laboratory is a very simple app designed to help you keep track of your
 organisation's instruments. It is comprised of the following related models:

### `laboratory.Laboratory`
The `Laboratory` model stores information pertaining to a collection
of instruments. There is no requirement that this model is fixed to a permanent 
location such as a physical laboratory housed within a building! It simply 
refers to a (semi)-permanent collection of instruments that are typically
used together to measure one or more types of data.

Fields:

- name: `char`
- description: `text`
- contact_name: `char`
- contact_email: `email`
- outputs: M2M to `laboratory.DataType`

### `laboratory.Instrument`
The `laboratory.Instrument` model refers to unique physical instruments that 
are used either individually or within a collection to measure one or more 
data types.

Fields:

- internal_id: `char`
- type: FK to `laboratory.InstrumentType`
- laboratory: FK to `laboratory.Laboratory`

> **_NOTE:_** It's not totally clear yet whether laboratory field here should be
 a ForeignKey or a OneToOneField. Should an instrument be allowed to belong 
 to multiple labs?

### `laboratory.InstrumentType`
Stores information regarding the type of instrument. If manufacturers themselves
are part of your user base then you can allow them to create their own
instruments and allow laboratory users to select from predefined. Otherwise, 
allow lab users to fill in their own instrument types.

Fields:
- type: `char`
- model: `char`
- manufacturer: FK to `laboratory.Manufacturer`
- year_manufactured: `int`
- description: `text`

### `laboratory.Manufacturer`
Stores basic information regarding the manufacturer of an instrument.

Fields:
- name: `char`
- location: `char`

### `laboratory.DataType`
A simple model for storing data types.

Fields:
- name: `char`

## Installation

Django Laboratory is still in beta development so, if for some reason you stumble 
across this repository and wish to try it out, you will have to clone it direct
into your application.

Eventually we will release via PyPI once the package matures and testing coverage
becomes acceptable.

## Usage

Usage as a standalone application is really simple. Just add `laboratory` to your 
`INSTALLED_APPS` setting, then run `python manage.py makemigrations` and 
`python manage.py migrate` in order to create and apply migrations. Navigate
to your admin site and you will find your five new models listed under
Laboratory.

## Acknowledgements

This package is being jointly developed by the GeoForschungsZentrum, Potsdam
and Geoluminate.