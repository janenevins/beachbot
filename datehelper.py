def fix_date_string(datestring):  #this function transforms the date string into something that can be correctly sorted
    """
    datestring change from '04/05/1984' to
    '1984-05-04'
    """
    ds = datestring.split('/')
    return '-'.join([ds[2], ds[0], ds[1]])
