def name_surname(string, n, s):
    sample_data = string.replace("%N%", n)
    sample_data = sample_data.replace("%S%", s)
    return sample_data
