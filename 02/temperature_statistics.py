def temperature_statistics(temperature):
    if temperature == []:
        return {
            'avg': None,
            'min': None,
            'max': None,
            'above_avg': None,
            'above_avg_idx': None
        }
    avg = sum(temperature)/ len(temperature)
    min_tempreture = min(temperature)
    max_tempreture = max(temperature)
    above_avg_temperarue = []
    above_avg_temp_idx = []

    for i in range(len(temperature)):
        if temperature[i] > avg:
            above_avg_temperarue.append(temperature[i])
            above_avg_temp_idx.append(i)

    return {
        'avg': round(avg),
        'min': round(min_tempreture),
        'max': round(max_tempreture),
        'above_avg': above_avg_temperarue,
        'above_avg_idx': above_avg_temp_idx
    }
