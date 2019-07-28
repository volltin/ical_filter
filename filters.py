from icalendar import Calendar


class ICalFilter:
    def __init__(self, content):
        self.content = content

    def filtered(self):
        return self.content


class HideDetail(ICalFilter):
    SUMMARY_TEXT = 'Busy'
    DESCRIPTION_TEXT = ''
    LOCATION_TEXT = ''

    def filtered(self):
        cal = Calendar.from_ical(self.content)
        for e in cal.walk('vevent'):
            e['SUMMARY'] = self.SUMMARY_TEXT
            e['DESCRIPTION'] = self.DESCRIPTION_TEXT
            e['LOCATION'] = self.LOCATION_TEXT
        return cal.to_ical()
