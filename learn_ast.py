def decade_counter(years):
    decades = 0
    while years > 10:
        decades += 1
        years -= 10
    return decades

print(decade_counter(23))