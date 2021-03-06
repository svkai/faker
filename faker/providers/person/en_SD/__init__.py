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
         'Jean Paul',
 'Alghaliy',
 'Abdo',
 'Chriz',
 'Nanomi',
 'Mohammed',
 'Kariem',
 'Patrick',
 'Kamal',
 'Okot',
 'Ibrahim',
 'Suleyman',
 'Jordan',
 'Clinton',
 'Malse',
 'Shaker',
 'Mustafa',
 'Harun',
 'Abduk',
 'Yasin',
 'Adan',
 'ابن صومال',
 'Muniir',
 'Galaxy',
 'Abdiqani',
 'Mahad',
 'ناصر العازمي',
 'Ahmed',
 'Beraka',
 'Abuukar',
 'Abdi',
 'A.',
 'Mohamed',
 'Farhan',
 'Aakhiro',
 'Ali',
 'Mo',
 'Moscownikov',
 'Chriz',
 'Patrick',
 'Kamal',
 'Mohammed',
 'Alghaliy',
 'A.',
 'J.P.',
 'Suleyman',
 'Clinton',
 'Shaker',
 'Kariem',


    )

    first_names_female = (
         'Abrar',
 'Nadia',
 'Favor',
 'Uduru',
 'Anita',
 'Dabor',
 'Grace',
 'Talia',
 'Rita',
 'Hiba',
 'Nafy',
 'Joyce',
 'Minoo',
 'Rachael',
 'Yaya',
 'Ray',
 'Onnab',
 'Akong',
 'Jalila',
 'Balghis',
 'Hanan',
 'Hanan',
 'Magda',
 'Taghreed',
 'Awadiya',
 'Fahima',
 'Nour',
 'Gisma',
 'Muna',
 'Widad',
 'Nawal',
 'Mai',
 'Yassmin',
 'Leila',
 'Nahid',
 'Niema',
 'Zeinab Badawi',
 'Hania',
 'Siham',
 'Nesrine',
 'Salma',
 'Maisoon',
 'Niemat',
 'Asma',
 'Nahla',
 'N.',
 'Kamala',
 'Hadeel',
 'Dalia Haj Omer',
 'Irene',
 'Nancie',
 'Sarah',
 'Shiro',
 'Michelle',
 'Gloria',
 'Rachel',
 'Julie',
 'Nsulubi',
 'Florence',
 'Sandra',
 'Jay',
 'Marion',
 'Dorah',
 'Megan',

    )

    first_names = first_names_male + first_names_female

    last_names = (
         'Garang',
 'Garda',
 'Gelsthorpe',
 'Glaiati',
 'Gosh',
 'Gubara',
 'Gulwak',
 'Abdullah',
 'Aboulela',
 'Abubakr',
 'Adam',
 'Adikhalamani',
 'Aga',
 'Agab',
 'Agag',
 'Agar',
 'Ageeb',
 'Ahmad',
 'Ahmed',
 'Akhraten',
 'Akol',
 'Akot',
 'Babikir',
 'Badawi',
 'Badri',
 'Bakhiet',
 'Bakhit',
 'Bakhita',
 'Bakr',
 'Khan',
 'Byn',
 'B.',
 'A.',
 'Mursaal Xuseen',
 'Cell',
 'Gamure',
 'Muxhudin',
 'P.',
 'Yusif',
 'Haji',
 'H.',
 'Naasir',
 'Abdirahman',
 'Ise.',
 'Maruf',
 'Mahad',
 'Sacid',
 'Wardi',
 'Kellen',
 'Mugiza',
 'Masuku',
 'Ondaro',
 'Sakat',
 'Aims',
 'Baya',
 'Orsoro',
 'Ogutu',
 'Mangera',
 'Wanjawa',
 'K.',
 'Kimani',
 'Waweru',
 'S.',
 'O.',


    )

    prefixes_male = (

    )
    prefixes_female = (

    )

    suffixes = ()
