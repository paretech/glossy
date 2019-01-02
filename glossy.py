"""Generate a glossary of acronyms"""

from openpyxl import load_workbook


def tokenize(value):
    return value.split(' ')

def count_true(function, iterable):
    return len(list(filter(function, iterable)))

def keep_alpha(iterable):
    return ''.join(list(filter(str.isalpha, iterable)))

def oddly_capitalized(iterable):
    alpha_length = count_true(str.isalpha, iterable)
    upper_length = count_true(str.isupper, iterable)
    
    if upper_length > 1:
        return True

    if ((upper_length == 1) and alpha_length == 2):
        return True

    return False

if __name__ == '__main__':
    wb = load_workbook('excel_2016.xlsx')
 
    ws = wb.get_active_sheet()

    acronym_candidates = set() 

    for row in ws.values:
        key, value = row
        acronym_candidates = acronym_candidates.union(
            [keep_alpha(token) for token in filter(oddly_capitalized, tokenize(value))])

    print(acronym_candidates)