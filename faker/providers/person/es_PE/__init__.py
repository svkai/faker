# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = (
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
    )

    first_names_male = (
           'Jose',
 'Daniel',
 'Diego',
 'Carlos',
 'Juan',
 'Juan Carlos',
 'Gabriel',
 'Michael',
 'Jesús',
 'Henry',
 'Andre',
 'Miguel',
 'H.',
 'Isac',
 'Victor',
 'Julio',
 'Richard',
 'Alexander',
 'Christian',
 'Jefry',
 'Piero',
 'Aaron',
 'Danny',
 'Luis',
 'Pedro',
 'A.',
 'Angel',
 'Alex',
 'Elmer',
 'Ricardo',
 'Colbert',
 'Cristopher Quispe',
 'Alois',
 'Percy',
 'Clegauth',
 'Eduardo',
 'William',
 'Mariano',
 'Ric',
 'Ozcar',
 'Yonatan',
 'Danii',
 'Roger',
 'Krloz',
 'Sebastian',
 'Patrick',
 'Hugo',
 'Andrew',
 'Jean Pier Ortega',
 'Farik',
 'Joaquin',
 'Jude',
 'Aldo',
 'Juli0',
 'Willian',
 'Bruce',
 'Luyis',
 'Luis Espinoza',
 'M.',
 'Renán',
 'Jorge Luis',
 'Darwin',
 'Rodrigo',
 'Ventanilla',


    )

    first_names_female = (
            'Andrea',



    )

    first_names = first_names_male + first_names_female

    last_names = (
          'Rodríguez',



    )

    prefixes_male = (

    )
    prefixes_female = (

    )

    suffixes = ()