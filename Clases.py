# -*- coding: utf-8 -*-


class Group:
    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer


class Contact:
    def __init__(self, firstname, middlename, lastname, nickname, title, company, address, home,
                 mobile, work, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth,
                 ayear, address2, home2, notes):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday + 1
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday + 1
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.home2 = home2
        self.notes = notes
